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


# This creates a Drivebase so that if we call "robot" it will move both motors.
robot=DriveBase(left_motor, right_motor, 53, 104)

def moveInches(myInches, mySpeedPercent, mySteering = 0):
    wheel_circ = 53
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    speed = 10.5 * mySpeedPercent
    if myInches > 0:
        robot.drive(speed, mySteering)
        while left_motor.angle() < wheel_circ*myInches: # and not left_motor.stalled():
            pass
        robot.stop(Stop.BRAKE)

    elif myInches < 0:
        robot.drive(-1 * speed, mySteering)
        while left_motor.angle() > wheel_circ*myInches: # and not left_motor.stalled():
            pass
        robot.stop(Stop.BRAKE)

    else:
        robot.stop(Stop.BRAKE)


def stopDriveMotors():
    print("Brake")
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
    left_motor.dc(0)
    right_motor.dc(0)

moveInches(12, 20)