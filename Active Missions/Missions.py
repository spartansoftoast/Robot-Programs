#!/usr/bin/env pybricks-micropython
import functions as toast

def TJ_Swing():
    toast.gyro.reset_angle(0)
    toast.brick.sound.beep()
    toast.wait(750)

    # This moves the robot to the Traffic Jam, so that the attachment is under the Traffic Jam.

    toast.moveInches(23.6, 250, 0)

    toast.wait(250)

    # This lifts the Traffic Jam.

    toast.med_attachment(70, 1)

    # This bumps the Traffic Jam to make it stay up.

    toast.moveAngle(36, 40, 1)
    toast.wait(250)

    # This turns the robot to face the line for line following.
    toast.moveAngle(-65, 40, 1)
    toast.wait(250)

    # This moves the robot to the line for line following.

    toast.moveWhite()
    toast.wait(250)
    toast.moveBlack()
    toast.wait(250)

    # This turns the robot toward the line for more accurate line following.

    toast.moveAngle(6, 40, 1)

    # This makes the medium motor move down in preperation for the Swing mission.

    toast.med_attachment_parallel(-10, 1)
    toast.wait(250)

    # This follows the line using the right color sensor.

    toast.followRight(5.3)

    # This turns the robot to make sure it can hit the Swing.

    toast.moveAngle(16, 40, 1)
    toast.wait(250)

    # This tells the robot to move forward so that it stays on the line.

    toast.moveInches(.5, 100, 0)
    toast.wait(250)

    # This moves the medium motor down to hit the Swing.

    toast.med_attachment(-35, 1)
    toast.wait(250)

    # This turns the robot to go back into base.

    toast.moveAngle(-5, 40, 1)
    toast.wait(250)

    # This resets the medium motor for the next mission.

    toast.med_attachment_parallel(80, 1)

    # This moves the robot back into base.

    toast.moveInches(-72, 400, 0)

def DB_Crane():
    toast.gyro.reset_angle(0)
    toast.brick.sound.beep()
    toast.wait(500)

    # This makes the robot deliver the units to the black circle near the crane.
    toast.moveInches(17, 125, 0)

    # This makes the robot back away from black circle mentioned above.
    toast.moveInches(-5, 300, 0)

    # Turn robot to the right.
    toast.moveAngle(75, 120, 0)

    # This lowers the leverator so it can slide under the left blue lever on the crane.
    toast.med_attachment_parallel(-90, 1)

    # This makes the robot move toward the crane.
    toast.moveInches(15 , 300, 0)

    toast.moveAngle(-43, 120, 0)


    # This reliably gets to the position needed to lift the crane lever.
    toast.moveWhite()


    # This lifts the crane lever.
    toast.med_attachment(50,1)


    # This moves the robot into the base.
    toast.moveAngle(-93, 120, 0)


    # This gets the leverator ready for the next mission: Elevator.
    toast.med_attachment_parallel(-50,1)  
    toast.moveInches(30, 300, 0)

def Innovative_A():
    toast.gyro.reset_angle(0)
    toast.brick.sound.beep()
    toast.wait(750)

    # This turns the robot to face the black circle near the tree.

    toast.moveAngle(-34, 200, 0)

    toast.wait(250)

    # This pushes the Innovative Architecture into the circle.

    toast.moveInches(16, 200, 0)

    toast.wait(250)

    # This moves the robot backward away from the Innovative Architecture.

    toast.moveInches(-8, 200, 0)

    toast.wait(250)

    # This turns the robot to the right, so that it is facing into base.

    toast.moveAngle(10, 500, 0)

    toast.wait(250)

    # This moves the robot into base.

    toast.moveInches(-27, 1100, 0)

def Tan_Elevator():
    toast.gyro.reset_angle(0)
    toast.brick.sound.beep()
    toast.wait(750)

    # This turns the robot toward the circle next to the Elevator.

    toast.motorReset()

    toast.moveAngle(-20, 60, 0)

    toast.wait(250)

    # This moves the robot forward to the circle next to the Elevator.

    toast.moveInches(40, 400, 0)

    toast.wait(250)

    toast.moveWhite()

    toast.wait(250)

    toast.moveAngle(-5, 40, 1)

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

    toast.moveAngle(-10, 40, 1)

    toast.wait(250)

    toast.followLeft(2.65)

    toast.wait(250)

    toast.med_attachment_parallel(45, 1)

    toast.moveInches(5, 200, 0)

    toast.wait(250)

    toast.moveInches(-10, 200, 0)

    toast.wait(250)

def Red_Circle_Bridge():
    toast.gyro.reset_angle(0)
    toast.brick.sound.beep()
    toast.wait(750)

    # This moves the robot foward to prepare it to get the red block into the red circle.
    toast.moveInches(10, 200, 0)

    toast.wait(500)

    # This turns the robot to the left to face the red circle.

    toast.moveAngle(-17, 75, 0)


    # This pushes the blocks into the red circle.

    toast.moveInches(19, 200, 0)

    # This moves the robot backward to prepare the robot for the bridge.

    toast.moveInches(-9, 350, 0)

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
