#!/usr/bin/env pybricks-micropython
import functions as toast # import the functions we created to help mission programmers
import Missions as missions # import the mission functions each team member programmed

# This tells the robot to display the GyroSensor so that we can see if the Gyro is drifting.
# If the Gyro is not drifting, we push a button on the robot and it starts the program.
while True:
    while not any(toast.brick.buttons()) and not toast.touch.pressed():
        toast.gyroDrift()
        pass

    # Third mission Traffic Jam and Swing.
    if toast.Button.RIGHT in toast.brick.buttons():
        missions.TJ_Swing()
        pass

    # First mission Design and Build and Crane.
    elif toast.Button.LEFT in toast.brick.buttons():
        missions.DB_Crane()
        pass

    # Fourth mission Innovative Architecture.
    elif toast.Button.DOWN in toast.brick.buttons():
        missions.Innovative_A()
        pass

    # Second mission Tan Circle and Elevator.
    elif toast.Button.UP in toast.brick.buttons():
        missions.Tan_Elevator()
        pass

    # Fifth mission Red Circle and Bridge.
    elif toast.Button.CENTER in toast.brick.buttons():
        missions.Red_Circle_Bridge()
        pass

    elif toast.touch.pressed() == True:
        toast.SEQ_Touch()

    else:
        toast.robot.stop(toast.Stop.BRAKE)
