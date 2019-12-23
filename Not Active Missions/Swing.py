#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
# 1+1=2
# Write your program here
left_motor = Motor(Port.C, Direction.CLOCKWISE)
right_motor = Motor(Port.D, Direction.CLOCKWISE)
med_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
gyro = GyroSensor(Port.S4)
robot=DriveBase(left_motor, right_motor, 56, 104)
med_motor.reset_angle(0)

def moveInches(myInches):
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    if myInches > 0:
        robot.drive(200, 0)
        while left_motor.angle() < 29.75*myInches and not left_motor.stalled():
            pass
        robot.stop(Stop.BRAKE)

    elif myInches < 0:
        robot.drive(-200, 0)
        while left_motor.angle() > 29.75*myInches and not left_motor.stalled():
            pass
        robot.stop(Stop.BRAKE)
        
    else:
        robot.stop(Stop.BRAKE)

def moveAngle(myAngle):
    gyro.reset_angle(0)
    if myAngle > 0:
        left_motor.dc(30)
        right_motor.dc(-30)
        wait(100)
        while gyro.angle() < myAngle and gyro.speed() > 5:
            pass
        robot.stop(Stop.BRAKE)

    elif myAngle < 0:
        left_motor.dc(-30)
        right_motor.dc(30)
        wait(100)
        while gyro.angle() > myAngle and gyro.speed() < -5:
            pass
        robot.stop(Stop.BRAKE)

    else:
        robot.stop(Stop.BRAKE)
        pass

while not any(toast.brick.buttons()):
    toast.gyroDrift()
    pass
toast.brick.sound.beep()
toast.wait(750)

# Make sure the scoop is above the ground
# This moves the robot to the swing
med_motor.run_time(1500, 1000)
med_motor.stop(Stop.BRAKE)
wait(1000)
moveInches(90)
wait(250)
moveAngle(40)
wait(250)
moveInches(5)
wait(250)
moveAngle(-15)
wait(250)
moveInches(-120)
wait(250)
moveAngle(-120)
