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
import time

# This tells the brick where we have the motors and sensors plugged in.
left_motor = Motor(Port.B, Direction.CLOCKWISE)
right_motor = Motor(Port.D, Direction.CLOCKWISE)
med_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
med_motorB = Motor(Port.C, Direction.CLOCKWISE)
gyro = GyroSensor(Port.S4)
gyro_V = GyroSensor(Port.S1)
colorL = ColorSensor(Port.S2)
touch = TouchSensor(Port.S3)
gyro.reset_angle(0)
gyro_V.reset_angle(0)
# This function tells the robot to move forward and backward.
# myInches tells the robot how many inches to move.
# mySpeedPercent tells the robot how fast to move.
# mySteering tells the robot while moving forward or backward
# to turn to either the right or the left while moving.

def moveInches(myInches, mySpeedPercent = 75):
    wheel_circ = 52
    speed = 10.5 * mySpeedPercent
    print("moveInches(" + str(myInches) + ", " + str(mySpeedPercent))
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    print(str(gyro.angle()),str(left_motor.angle()), str(right_motor.angle()))
    left_motor.run_target(speed, wheel_circ*myInches, Stop.COAST, False)
    right_motor.run_target(speed, wheel_circ*myInches, Stop.COAST, True)
    stopDriveMotors()
    print(str(gyro.angle()),str(left_motor.angle()), str(right_motor.angle()))

    # Print debug (52*myInches vs actualAngle)


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
# myAngle tells the robot how many degrees to turn.
# mySpeed tells the robot how fast to turn.
# myType tells the robot to do either 1=spin turn or 0=pivot turn.
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


# This tells the medium motor to move either up or down.
# myAngle tells the medium motor how many degrees to either go up or down.
# gearbox tells the medium motor whether or not to use a ratio, used for the gearbox.
def med_attachment(myAngle):
    print("med_attachment")
    print("myAngle: " + str(myAngle))
    print(str(med_motor.angle()))

    if myAngle * 24 < med_motor.angle():
        med_motor.run(-1200)
        while med_motor.angle() > myAngle * 24:
            pass
        med_motor.stop(Stop.BRAKE)
        # The motor can go faster because it takes many rotations to move a little bit using the gearbox,
        # so we can go faster and it will still check enough to make it accurate.
    elif myAngle * 24 > med_motor.angle():
        med_motor.run(1200)
        while med_motor.angle() < myAngle * 24:
            pass
        med_motor.stop(Stop.BRAKE)
    print("med" + str(med_motor.angle()))
    med_motor.stop(Stop.BRAKE)  # Just in case the medium motor does not stop (micropython issue)

def med_attachmentB_parallel(myAngle):
    print("med_attachmentB_parallel")
    medThreadB = threading.Thread(target=med_attachmentB, args=(myAngle))
    medThreadB.start()

def med_attachmentB(myAngle):
    print("med_attachmentB")
    print(str(med_motorB.angle()))
    if myAngle * 24 < med_motorB.angle():
        med_motorB.run(-1200)
        while med_motorB.angle() > myAngle * 24:
            pass
        med_motorB.stop(Stop.BRAKE)
        # The motor can go faster because it takes many rotations to move a little bit using the gearbox,
        # so we can go faster and it will still check enough to make it accurate.
    elif myAngle * 24 > med_motorB.angle():
        med_motorB.run(1200)
        while med_motorB.angle() < myAngle * 24:
            pass
        med_motorB.stop(Stop.BRAKE)
    print("med" + str(med_motorB.angle()))
    med_motorB.stop(Stop.BRAKE)  # Just in case the medium motor does not stop (micropython issue)
# This runs med_attachment in a thread so that commands can run while the leverator changes position

def med_attachment_parallel(myAngle):
    print("med_attachment_parallel")
    try:
       # medThread = threading.Thread(med_attachment, myAngle)
        medThread = threading.Thread(target=med_attachment, args=(myAngle))
        medThread.start()
    except NameError:
        print("NameError")
    except Exception:
        print("Exception")
    else:
        print("Nothing Went Wrong")
    finally:
        print("finally triggered")

# This displays the gyro degrees on the robot screen.
def gyroDrift():
    brick.display.clear()
    brick.display.text(str(gyro.angle()), (60, 45))
    brick.display.text(str(gyro_V.angle()),(100, 45))
    brick.display.text("1) Left: DB and Crane", (10, 55))
    brick.display.text("2) Up: Elevator", (10, 65))
    brick.display.text("3) Right: Innovative Architecture", (10, 75))
    brick.display.text("4) Center: TJ Bridge", (10, 85))
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
    while colorL.reflection() > 6:
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
# We use different color sensors depening how the robot lines up
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

def motorReset():
    print("motorReset")
    left_motor.run_time(11, 10, Stop.BRAKE, True)
    right_motor.run_time(11, 10, Stop.BRAKE, True)
    med_motor.run_time(11, 10, Stop.BRAKE, True)

def Bridge():
   # med_attachment(30, 1)
    gyro_V.reset_angle(0)
    moveInches(3, 50)
    #med_attachment_parallel(20)
    while gyro_V.angle() > 0:
        left_motor.run(400)
        right_motor.run(400)
    stopDriveMotors()

def SEQ_Touch():
    brick.sound.beep()
    wait(750)
    brick.display.clear()
    brick.display.text("Up: Med Up", (10, 55))
    brick.display.text("Down: Med Down", (10, 65))
    brick.display.text("Right: MedB Up",(10, 75))
    brick.display.text("Left: MedB Down", (10, 85))
    brick.display.text("Center: Set Med zero")
    while True:
        if Button.UP in brick.buttons():
            med_motor.dc(75)
        elif Button.DOWN in brick.buttons():
            med_motor.dc(-75)
        elif Button.RIGHT in brick.buttons():
            med_motorB.dc(75)
        elif Button.LEFT in brick.buttons():
            med_motorB.dc(-75)
        elif Button.CENTER in brick.buttons():
            med_motor.reset_angle(0)
            med_motorB.reset_angle(0)
            brick.sound.beep()
            wait(500)
        else:
            med_motor.stop(Stop.BRAKE)
            med_motorB.stop(Stop.BRAKE)
            if touch.pressed() == True:
                brick.sound.beep()
                wait(750)
                break

def stopDriveMotors():
    print("Brake")
    left_motor.dc(0)
    right_motor.dc(0)
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
