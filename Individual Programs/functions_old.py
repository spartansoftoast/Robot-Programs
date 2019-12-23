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
left_motor = Motor(Port.C, Direction.CLOCKWISE)
right_motor = Motor(Port.D, Direction.CLOCKWISE)
med_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
gyro = GyroSensor(Port.S4)
colorR = ColorSensor(Port.S3)
colorL = ColorSensor(Port.S2)

# This creates a Drivebase so that if we call "robot" it will move both motors.
robot=DriveBase(left_motor, right_motor, 56, 104)

# This function tells the robot to move forward and backward.
# myInches tells the robot how many inches to move.
# mySpeed tells the robot how fast to move.
# mySteering tells the robot while moving forward or backward
# to turn to either the right or the left while moving.
def moveInches(myInches, mySpeed, mySteering):
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    if myInches > 0:
        robot.drive(mySpeed, mySteering)
        while left_motor.angle() < 52*myInches: # and not left_motor.stalled():
            pass
        robot.stop(Stop.BRAKE)

    elif myInches < 0:
        robot.drive(-1 * mySpeed, mySteering)
        while left_motor.angle() > 52*myInches: # and not left_motor.stalled():
            pass
        robot.stop(Stop.BRAKE)
        
    else:
        robot.stop(Stop.BRAKE)

# This makes the robot turn right or left.
# myAngle tells the robot how many degrees to turn.
# mySpeed tells the robot how fast to turn.
# myType tells the robot to do either a spin turn or a pivot turn.
def moveAngle(myAngle, mySpeed, myType):
    gyro.reset_angle(0)
    if myType == 1:
        if myAngle > 0:
            robot.drive(0, mySpeed)
            wait(100)
            while gyro.angle() < myAngle:# and gyro.speed() > 5:
                pass
            robot.stop(Stop.BRAKE)

        elif myAngle < 0:
            robot.drive(0, -1 * mySpeed)
            wait(100)
            while gyro.angle() > myAngle:# and gyro.speed() < -5:
                pass
            robot.stop(Stop.BRAKE)

        else:
            robot.stop(Stop.BRAKE)
            pass
    elif myType == 0:
        if myAngle > 0:
            left_motor.run(mySpeed)
            wait(100)
            while gyro.angle() < myAngle:
                pass
            robot.stop(Stop.BRAKE)

        elif myAngle < 0:
            right_motor.run(mySpeed)
            wait(100)
            while gyro.angle() > myAngle:
                pass
            robot.stop(Stop.BRAKE)
        
        else:
            robot.stop(Stop.BRAKE)
            pass

# This tells the medium motor to move either up or down.
# myAngle tells the medium motor how many degrees to either go up or down.
# gearbox tells the medium motor whether or not to use a ratio, used for the gearbox.
def med_attachment(myAngle, gearbox):
    med_motor.reset_angle(0)
    if gearbox == 1:
        if myAngle < 0:
            med_motor.run(-1440)
            while med_motor.angle() > myAngle * 24:
                pass
            med_motor.stop(Stop.BRAKE)
            # The motor can go faster because it takes many rotations to move a little bit using the gearbox,
            # so we can go faster and it will still check enough to make it accurate.
        elif myAngle > 0:
            med_motor.run(1440)
            while med_motor.angle() < myAngle * 24:
                pass
            med_motor.stop(Stop.BRAKE)

    if gearbox == 0:
        if myAngle < 0:
            med_motor.run(-360)
            while med_motor.angle() > myAngle:
                pass
            med_motor.stop(Stop.BRAKE)
            # We chose the slower speed so that the medium motor will have more time to check the angle.
        elif myAngle > 0:
            med_motor.run(360)
            while med_motor.angle() < myAngle:
                pass
            med_motor.stop(Stop.BRAKE)

    med_motor.stop(Stop.BRAKE)  # Just in case the medium motor does not stop (micropython issue)

# This runs med_attachment in a thread so that commands can run while the leverator changes position
def med_attachment_parallel(myAngle, gearbox):
    medThread = threading.Thread(target=med_attachment, args=(myAngle,gearbox))
    medThread.start()

# This displays the gyro degrees on the robot screen.
def gyroDrift():
    brick.display.clear()
    brick.display.text(str(gyro.angle()), (60, 45))
    brick.display.text("1) Left: DB and Crane", (10, 55))
    brick.display.text("2) Up: Elevator", (10, 65))
    brick.display.text("3) Right: Traffic Jam", (10, 75))
    brick.display.text("4) Down: Innovative Architecture", (10, 85))
    brick.display.text("5) Center: Bridge", (10, 95))
    wait(500)

# This moves the robot FORWARD till the color sensor finds a white line.
def moveWhite():
    robot.drive(200, 0)
    while colorR.reflection() < 32:
       pass
    robot.stop(Stop.BRAKE)

# This moves the robot FORWARD till the color sensor finds a black line.
def moveBlack():
    robot.drive(200, 0)
    while colorR.reflection() > 6:
       pass
    robot.stop(Stop.BRAKE)

# This moves the robot BACKWARD till the color sensor finds a white line.
def moveWhiteB():
    robot.drive(-200, 0)
    while colorR.reflection() < 32:
       pass
    robot.stop(Stop.BRAKE)

# This moves the robot BACKWARD till the color sensor finds a black line.
def moveBlackB():
    robot.drive(-200, 0)
    while colorR.reflection() > 6:
       pass
    robot.stop(Stop.BRAKE)

# This uses both color sensors to follow the white line
# forHowLong tells how many seconds to follow the line
def followWhite(forHowLong):
    startTime = time.time()
    currentTime = time.time()
    totalTime = currentTime - startTime

    while (totalTime < forHowLong):
        #totalTime < forHowLong
        #currentTime = time.clock
        

       #totalTime = currentTime - startTime
        if colorR.reflection() > 48:
            robot.drive(133, 90)
        elif colorL.reflection() > 48:
            robot.drive(133, -90)
        #else:
         #   robot.drive(1, 90)

        currentTime = time.time()
        totalTime = currentTime - startTime
        print(totalTime)
    robot.stop(Stop.BRAKE)   

# This uses both color sensors to follow the black line
# forHowLong tells how many seconds to follow the line
def followBlack(forHowLong):
    #Get Starting Time: startTime
    startTime = time.clock
    while True:
        # Get Current Time: currentTime

        # See how much time has passed

        # If timePassed < forHowLong continue the loop

        #robot.drive(101, 0)
        if colorR.reflection() < 8:
            moveAngle(2, 75, 1)
        elif colorL.reflection() < 8:
            moveAngle(-2, 75, 1)
        else:
            robot.drive(101, 0)

# This uses only the RIGTH color sensors to follow the black line
# forHowLong tells how many seconds to follow the line
def followRight(forHowLong):
    startTime = time.time()
    currentTime = time.time()
    totalTime = currentTime - startTime
    expectedBlack = 6
    expectedWhite = 50
    #powerMultiplier = 0.45
    powerMultiplier = 0.40
    maxMotorPower = 1100
    while (totalTime < forHowLong):
        print("While")
        color = colorR.reflection()
        left = (expectedWhite - color) * powerMultiplier + 10
        right = (color - expectedBlack) * powerMultiplier + 10
        left_motor.run(maxMotorPower * (left/100))
        right_motor.run(maxMotorPower * (right/100))
        currentTime = time.time()
        totalTime = currentTime - startTime
        print(totalTime)
    robot.stop(Stop.BRAKE)

# This uses only the LEFT color sensors to follow the black line
# forHowLong tells how many seconds to follow the line
# We use different color sensors depening how the robot lines up
def followLeft(forHowLong):
    startTime = time.time()
    currentTime = time.time()
    totalTime = currentTime - startTime
    expectedBlack = 6
    expectedWhite = 50
    powerMultiplier = 0.40
    maxMotorPower = 1100
    while (totalTime < forHowLong):
        print("While")
        color = colorL.reflection()
        left = (expectedWhite - color) * powerMultiplier + 10
        right = (color - expectedBlack) * powerMultiplier + 10
        left_motor.run(maxMotorPower * (left/100))
        right_motor.run(maxMotorPower * (right/100))
        currentTime = time.time()
        totalTime = currentTime - startTime
        print(totalTime)
    robot.stop(Stop.BRAKE)