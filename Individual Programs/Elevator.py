#!/usr/bin/env pybricks-micropython
import functions as toast

# This tells the robot to display the GyroSensor so that we can see if the Gyro is drifting.
# If the Gyro is not drifting, we push a button on the robot and it starts the program.

while not any(toast.brick.buttons()):
    toast.gyroDrift()
    pass
toast.brick.sound.beep()
toast.wait(750)

# This turns the robot toward the circle next to the Elevator.

toast.motorReset()

toast.moveAngle(-20, 60, 0)

toast.wait(250)

# This moves the robot forward to the circle next to the Elevator.

toast.moveInches(40, 200, 0)

toast.wait(250)

toast.moveWhite()

toast.wait(250)

toast.moveAngle(-15, 40, 1)

toast.wait(250)

toast.moveInches(6, 200, 0)

toast.wait(250)

toast.moveInches(-3, 200, 0)

toast.wait(250)

# This moves the robot to face the Elevator.

toast.moveAngle(45, 50, 1)

toast.wait(250)

# This moves the robot to the Elevator.

toast.moveWhite()

toast.wait(250)

toast.followLeft(2.65)

toast.wait(250)

toast.med_attachment_parallel(45, 1)

toast.moveInches(5, 200, 0)

toast.wait(250)

toast.moveInches(-10, 200, 0)

toast.wait(250)

