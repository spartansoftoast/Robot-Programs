#!/usr/bin/env pybricks-micropython
import functions as toast

# This tells the robot to display the GyroSensor so that we can see if the Gyro is drifting.
# If the Gyro is not drifting, we push a button on the robot and it starts the program.

while not any(toast.brick.buttons()):
    toast.gyroDrift()
    pass
toast.brick.sound.beep()
toast.wait(750)

# This moves the robot near to the Bridge.

toast.moveInches(32, 200)

# This moves the robot to the white line.

toast.moveWhite()
toast.wait(200)

# This moves the robot a little more forward.

toast.moveInches(3, 200)
toast.wait(200)

# This turns the robot torward the Bridge.

toast.moveAngle(-110, 20, 1)
toast.wait(200)

# This moves the robot up the Bridge.

toast.moveInches(75, 1000)
toast.robot.stop(Stop.BRAKE)