#!/usr/bin/env pybricks-micropython

# This loads the micropython code for sensors, motors, ports, etc.

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import threading
from multiprocessing import Process
import time

# This tells the brick where we have the motors and sensors plugged in.
left_motor = Motor(Port.D, Direction.CLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
med_motor = Motor(Port.A, Direction.CLOCKWISE)
med_motorB = Motor(Port.C, Direction.CLOCKWISE)
gyro = GyroSensor(Port.S4)
gyro_V = GyroSensor(Port.S1)
colorL = ColorSensor(Port.S2)
touch = TouchSensor(Port.S3)
gyro.reset_angle(0)
gyro_V.reset_angle(0)

# This function tells the robot to move forward and backward.
# myInches tells the robot how many inches to move.
# mySpeedPercent tells the robot how fast to move in percent.
def moveInches(myInches, mySpeedPercent = 75):
    wheel_circ = 52
    speed = 10.5 * mySpeedPercent
    print("moveInches(" + str(myInches) + ", " + str(mySpeedPercent) + ")")
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    print(str(gyro.angle()),str(left_motor.angle()), str(right_motor.angle()))
    left_motor.run_target(speed, wheel_circ*myInches, Stop.COAST, False)
    right_motor.run_target(speed, wheel_circ*myInches, Stop.COAST, True)
    stopDriveMotors()
    print(str(gyro.angle()),str(left_motor.angle()), str(right_motor.angle()))

# This function tells the robot to turn using one wheel or the other.
# myAngle tells the robot how far to turn in degrees.
# mySpeedPercent tells the robot how fast to turn in percent.
# whichWheel tells the robot which wheel to use to turn.
def pivotTurn(myAngle, mySpeedPercent, whichWheel):
    speed = 10.5 * mySpeedPercent
    if myAngle > gyro.angle() and whichWheel == 1:  # Turn Right
        left_motor.run(speed)
        while gyro.angle() <= myAngle:
            pass
        print("End Turn" + str(gyro.angle()))
        stopDriveMotors()

    elif myAngle > gyro.angle() and whichWheel == 2:  # Turn Right
        right_motor.run(-1 * speed)
        while gyro.angle() <= myAngle:
            pass
        print("End Turn" + str(gyro.angle()))
        stopDriveMotors()

    elif myAngle < gyro.angle() and whichWheel == 2:  # Turn Left
        right_motor.run(speed)
        while gyro.angle() >= myAngle:
            pass
        print("End Turn" + str(gyro.angle()))
        stopDriveMotors()

    elif myAngle < gyro.angle() and whichWheel == 1:  # Turn Left
        left_motor.run(-1 * speed)
        while gyro.angle() >= myAngle:
            pass
        print("End Turn" + str(gyro.angle()))
        stopDriveMotors()

    else:
        pass

# This function tells the robot to turn using both wheels.
# myAngle tells the robot how far to turn in degrees.
# mySpeedPercent tells the robot how fast to turn in percent.
def spinTurn(myAngle, mySpeedPercent):
    if myAngle > gyro.angle(): # turn Right
        left_motor.dc(mySpeedPercent)     
        right_motor.dc(-1*mySpeedPercent)
        while gyro.angle() <= myAngle: # and gyro.speed() > 5:
            pass
        print("End Turn" + str(gyro.angle()))
        stopDriveMotors()

    elif myAngle < gyro.angle(): # turn Left
        left_motor.dc(-1*mySpeedPercent)            
        right_motor.dc(mySpeedPercent)
        while gyro.angle() >= myAngle: # and gyro.speed() < -5:
            pass
        print("End Turn" + str(gyro.angle()))
        stopDriveMotors()


# This makes the robot turn right or left.
# myAngle tells the robot how far to turn in degrees.
# mySpeed tells the robot how fast to turn in percent.
# myType tells the robot to do either 0 = Spin Turn, 1 = Left Wheel, and 2 = Right Wheel.
def moveAngle(myAngle, mySpeedPercent, myType):
    acceptableError = 2
    print("moveAngle(" + str(myAngle) + ", " + str(mySpeedPercent) + ", " + str(myType) +")")

    leftWheel = 1
    rightWheel = 2

    # Adding a wait to see if it fixes the motor issue after a reset
    # wait(100)
    if myType == 0:
        spinTurn(myAngle, mySpeedPercent)

    elif myType == 1:
        pivotTurn(myAngle, mySpeedPercent, leftWheel)

    elif myType == 2:
        pivotTurn(myAngle, mySpeedPercent, rightWheel)
    stopDriveMotors()
    print("End moveAngle" + str(gyro.angle()))

    error = abs(myAngle - gyro.angle())
    if error > acceptableError:
        moveAngle(myAngle, mySpeedPercent * .25, myType)
    else:
        # We are happy
        pass

def medium_motor_up(myAngle, myMotor = 0, mySpeedPercent = 100):
    if myMotor == 0:
        while med_motor.angle() <= myAngle * 24:
            med_motor.dc(mySpeedPercent)
            pass
        med_motor.dc(0)
        med_motor.stop(Stop.BRAKE)
    elif myMotor == 1: # Color Sensor Motor
        # if (med_motorB.angle() > myAngle): # Before turning on the motor make sure we aren't already there
        while med_motorB.angle() >= myAngle:
            med_motorB.dc(-1 * mySpeedPercent)
            pass
        med_motor.dc(0)
        med_motorB.stop(Stop.BRAKE)

def medium_motor_down(myAngle, myMotor = 0, mySpeedPercent = 100):
    if myMotor == 0:
        while med_motor.angle() >= myAngle * 24:
            med_motor.dc(-1 * mySpeedPercent)
            pass
        med_motor.dc(0)
        med_motor.stop(Stop.BRAKE)

    elif myMotor == 1: # Color Sensor Motor
        if (med_motorB.angle() < myAngle): # Before turning on the motor make sure we aren't already there
            while med_motorB.angle() <= myAngle:
                med_motorB.dc(mySpeedPercent)
                pass
            med_motor.dc(0)
            med_motorB.stop(Stop.BRAKE)
        
# This tells the medium motor to move either up or down.
# myAngle tells the medium motor how many degrees to either go up or down.
# This uses the gearbox ratio of 24 rotations per degree.
def med_attachment(myAngle, myMotor = 0, mySpeedPercent = 100):
    print("med_attachment")
    if myAngle * 24 > med_motor.angle():
        medium_motor_up(myAngle, myMotor, mySpeedPercent)

    elif myAngle * 24 < med_motor.angle():
        medium_motor_down(myAngle, myMotor, mySpeedPercent)

    med_motor.stop(Stop.BRAKE)  # Just in case the medium motor does not stop (micropython issue)

def colorMed(Up_Down):
    if Up_Down == 1:
        medium_motor_up(-90, 1, 50)
    elif Up_Down == 0:
        medium_motor_down(0, 1, 50)

# This displays the gyro angles and which missions are which button on the robot screen.
def gyroDrift():
    brick.display.clear()
    brick.display.text(str(gyro.angle()), (60, 45))
    brick.display.text(str(gyro_V.angle()),(100, 45))
    brick.display.text("1) Left: DB and Crane", (10, 55))
    brick.display.text("2) Center: Big Boy Drone", (10, 65))
    brick.display.text("3) Right: Traffic Swing", (10, 75))
    wait(500)

# This moves the robot FORWARD till the color sensor finds a white line.
def moveWhite():
    print("moveWhite")
    left_motor.run(135)       
    right_motor.run(135)
    while colorL.reflection() < 74:
       pass
    stopDriveMotors()

# This moves the robot FORWARD till the color sensor finds a black line.
def moveBlack():
    print("moveBlack")
    left_motor.run(100)            
    right_motor.run(100)
    while colorL.reflection() > 10:
       pass
    stopDriveMotors()

# This moves the robot BACKWARD till the color sensor finds a white line.
def moveWhiteB():
    print("moveWhiteB")
    left_motor.run(-135)            
    right_motor.run(-135)
    while colorL.reflection() < 74:
       pass
    stopDriveMotors()

# This moves the robot BACKWARD till the color sensor finds a black line.
def moveBlackB():
    print("moveBlackB")
    left_motor.run(-150)            
    right_motor.run(-150)
    while colorL.reflection() > 6:
       pass
    stopDriveMotors()

# This uses only the LEFT color sensors to follow the black line
# forHowLong tells how many seconds to follow the line
def followLeft(forHowLong):
    print("followLeft")
    startTime = time.time()
    currentTime = time.time()
    totalTime = currentTime - startTime
    expectedBlack = 6
    expectedWhite = 74
    powerMultiplier = 0.10
    maxMotorPower = 1100
    while (totalTime < forHowLong):
        color = colorL.reflection()
        left = (expectedWhite - color) * powerMultiplier + 20
        right = (color - expectedBlack) * powerMultiplier + 20
        right_motor.run(maxMotorPower * (left/100))
        left_motor.run(maxMotorPower * (right/100))
        currentTime = time.time()
        totalTime = currentTime - startTime
        print(totalTime)
    stopDriveMotors()

# This is the function called in the bridge program.
# This moves the robot up the bridge until the robot arrives flat on the top.
# This function uses the vertical gyro sensor to sense flatness.
def Bridge():
    gyro_V.reset_angle(0)
    moveInches(3, 50)
    while gyro_V.angle() > 0:
        left_motor.run(400)
        right_motor.run(400)
    stopDriveMotors()

# This is the utility mode that is accessed inside the sequencer program.
# This is used to move the medium motor up and down inside the sequencer.
# This also calibrates the medium motor to 0.
# This uses the touch sensor to enter and exit.
def SEQ_Touch():
    brick.sound.beep()
    wait(750)
    brick.display.clear()
    brick.display.text("Up: Med Up", (10, 55))
    brick.display.text("Down: Med Down", (10, 65))
    brick.display.text("Center: Set Med zero", (10,75))
    while True:
        if Button.LEFT in brick.buttons():
            colorMed(1)
        elif Button.RIGHT in brick.buttons():
            colorMed(0)
        elif Button.UP in brick.buttons():
            med_motor.dc(75)
        elif Button.DOWN in brick.buttons():
            med_motor.dc(-75)
        elif Button.CENTER in brick.buttons():
            med_motor.reset_angle(0)
            med_motorB.reset_angle(0)
            brick.sound.beep()
            wait(500)
        else:
            med_motor.stop(Stop.BRAKE)
            if touch.pressed() == True:
                brick.sound.beep()
                wait(750)
                break

# This is the function that we use to stop the drive motors.
def stopDriveMotors():
    print("Brake")
    left_motor.dc(0)
    right_motor.dc(0)
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
