#!/usr/bin/env pybricks-micropython
import functions as toast

# This tells the robot to display the GyroSensor so that we can see if the Gyro is drifting.
# If the Gyro is not drifting, we push a button on the robot and it starts the program.

while not any(toast.brick.buttons()):
    toast.gyroDrift()
    pass
toast.brick.sound.beep()
toast.wait(750)

# This turns the robot to face the black circle near the tree.

toast.moveAngle(-34, 200, 0)

toast.wait(250)

# This pushes the Innovative Architecture into the circle.

toast.moveInches(16, 200, 0)

toast.wait(250)

# This moves the robot forward away from the Innovative Architecture.

toast.moveInches(-8, 200, 0)

toast.wait(250)

# This turns the robot to the right, so that it is facing into base.

toast.moveAngle(10, 500, 0)

toast.wait(250)

# This moves the robot into base.

toast.moveInches(-27, 1100, 0)