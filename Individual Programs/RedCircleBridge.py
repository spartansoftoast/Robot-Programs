#!/usr/bin/env pybricks-micropython
import functions as toast

# This tells the robot to display the GyroSensor so that we can see if the Gyro is drifting.
# If the Gyro is not drifting, we push a button on the robot and it starts the program.

while not any(toast.brick.buttons()):
    toast.gyroDrift()
    pass
toast.brick.sound.beep()
toast.wait(750)

# This moves the robot foward to prepare it to get the red block into the red circle.
toast.moveInches(10, 200, 0)
toast.robot.stop(toast.Stop.BRAKE)
toast.wait(500)

# This turns the robot to the left to face the red circle.

toast.moveAngle(-17, 75, 0)
toast.robot.stop(toast.Stop.BRAKE)

# This pushes the blocks into the red circle.

toast.moveInches(19, 200, 0)

# This moves the robot backward to prepare the robot for the bridge.

toast.moveInches(-9, 350, 0)
toast.robot.stop(toast.Stop.BRAKE)
toast.wait(500)

# This moves the robot forward so that the robot can face the bridge.

toast.followLeft(7)
toast.wait(500)

# This turns the robot to face the bridge.

toast.moveAngle(-101, 125, 1)

# This moves the robot forward torward the bridge using line following.

toast.followLeft(4)

# This moves the robot partly up the bridge.

toast.moveInches(13, 250, 0)

# This moves the robot the rest of the way up the bridge.

toast.moveInches(19, 250, 0)
toast.robot.stop(toast.Stop.BRAKE)
