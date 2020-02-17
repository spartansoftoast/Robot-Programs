#!/usr/bin/env pybricks-micropython
import functions as toast

# This tells the robot to display the GyroSensor so that we can see if the Gyro is drifting.
# If the Gyro is not drifting, we push a button on the robot and it starts the program.

while not any(toast.brick.buttons()):
    toast.gyroDrift()
    pass
toast.brick.sound.beep()
toast.wait(750)


toast.moveAngle(-80, 75, 1)
toast.wait(750)
toast.moveInches(26, 300, 0)
toast.wait(750)
toast.moveInches(-7, 300, 0)
toast.wait(750)
toast.moveAngle(80, 75, 1)
toast.wait(750)
toast.moveInches(6, 300, 0)
toast.wait(750)
toast.moveAngle(-80, 75, 1)
toast.wait(750)
toast.moveInches(6, 50, 0)
