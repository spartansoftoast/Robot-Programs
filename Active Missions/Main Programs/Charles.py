#!/usr/bin/env pybricks-micropython

import RobotFunctions as robot
import time


# Clear the display
robot.brick.display.clear()
# Print ``Hello`` near the middle of the screen
robot.brick.display.text("Hello", (60, 50))
# Print ``World`` directly underneath it
robot.brick.display.text("World")

# Wait until any of the buttons are pressed
while not any(robot.brick.buttons()):
    # Clear the display
    robot.brick.display.clear()

    # Print ``Gyro: `` near the middle of the screen
    robot.brick.display.text("Gyro: ", (60, 50))

    # Print Gyro value directly underneath it
    robot.brick.display.text(str(robot.gyro.angle()))

    time.sleep(.100)


# Make sure the scoop is above the ground
# This moves the robot to the swing
robot.med_motor.run_time(1500, 1000)
robot.med_motor.stop()
time.sleep(1)
robot.moveInches(90)
time.sleep(.250)
robot.moveAngle(40)
time.sleep(.250)
robot.moveInches(5)
time.sleep(.250)
robot.moveAngle(-15)
time.sleep(.250)
robot.moveInches(-120)
time.sleep(.250)
robot.moveAngle(-120)