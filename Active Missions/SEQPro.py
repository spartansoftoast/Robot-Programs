#!/usr/bin/env pybricks-micropython
import functions as toast # import the functions we created to help mission programmers
import Missions as missions # import the mission functions each team member programmed

# This tells the robot to display the GyroSensor so that we can see if the Gyro is drifting.
# If the Gyro is not drifting, we push a button on the robot and it starts the program.
while True:
    while not any(toast.brick.buttons()) and not toast.touch.pressed():
        toast.gyroDrift()
        pass

    # First mission Crane.
    if toast.Button.LEFT in toast.brick.buttons():
        missions.Crane()
        pass
    
    # Second mission Tan Circle and Elevator.
    elif toast.Button.CENTER in toast.brick.buttons():
        missions.Big_Boy_Drone_Bat()
        pass

    # Third mission Innovative Architecture.
    elif toast.Button.RIGHT in toast.brick.buttons():
        missions.Traffic_Red_Circle_Bridge()
        pass

    elif toast.touch.pressed() == True:
        toast.SEQ_Touch()

    else:
        toast.stopDriveMotors()
