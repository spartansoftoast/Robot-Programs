#!/usr/bin/env pybricks-micropython
import functions as toast

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
    toast.moveInches(10 , 300, 0)

    toast.moveAngle(-43, 120, 0)


    # This reliably gets to the position needed to lift the crane lever.
    toast.moveInches(3.67, 255, 0)


    # This lifts the crane lever.
    toast.med_attachment(50)
    toast.moveInches(-2, 300, 0)

    # This moves the robot into the base.
    toast.moveAngle(-150, 120, 0)


    # This gets the leverator ready for the next mission: Elevator.
    toast.med_attachment_parallel(-45)  
    toast.moveInches(17, 800, 0)
    toast.moveAngle(-90, 120, 0)
    toast.moveInches(13.5, 800, 0)
    toast.med_attachment(-8)

def Innovative_A():
    toast.gyro.reset_angle(0)
    toast.brick.sound.beep()
    toast.wait(750)

    # This turns the robot to face the black circle near the tree.

    toast.moveAngle(-40, 200, 0)

    toast.wait(250)

    # This pushes the Innovative Architecture into the circle.

    toast.moveInches(16, 350, 0)

    toast.wait(250)

    # This moves the robot backward away from the Innovative Architecture.

    toast.moveInches(-8, 350, 0)

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

    toast.moveWhite()

    toast.moveAngle(-35, 80)

    toast.moveInches(6, 300, 0)

    toast.moveWhiteB()

    # This moves the robot to face the Elevator.

    toast.moveAngle(20, 200)

    # This moves the robot to the Elevator.

    toast.moveWhite()

    toast.moveInches(2, 300)

    toast.moveAngle(-5, 100)

    toast.followLeft(2.65)

    #toast.moveAngle(-30, 80)

    #toast.moveInches(2, 400)

    #toast.med_attachment_parallel(45, 1)

    toast.moveInches(4, 200, 0)

    toast.moveWhiteB()

    toast.med_attachment_parallel(90)

    toast.moveInches(-1, 300)

    toast.moveAngle(85, 200)

    toast.moveInches(3, 100)

    toast.moveInches(-2, 200)

    toast.left_motor.reset_angle(0)

    toast.left_motor.run_target(200, -390, toast.Stop.BRAKE, True)

    toast.med_attachment(-80)

    toast.moveInches(2, 200)

    toast.left_motor.reset_angle(0)

    toast.left_motor.run_target(200, -90, toast.Stop.BRAKE, True)

    toast.med_attachment(-8)

    toast.moveInches(-4, 400)

    toast.moveAngle(-20, 400)

    toast.moveInches(-73.5, 700)

    toast.med_attachment(-2)

    #toast.moveInches(-10, 200, 0)

def Traffic_Red_Circle_Bridge():
    toast.gyro.reset_angle(0)
    toast.brick.sound.beep()
    toast.wait(750)

    toast.moveInches(23, 400, 0)

    toast.med_attachment(40, 1)

    toast.moveAngle(20, 200)

    toast.med_attachment_parallel(-30)

    toast.moveAngle(-55, 200)

    toast.med_attachment_parallel(20)

    toast.moveInches(6.5, 400)

    toast.med_attachment_parallel(-30)

    toast.moveWhiteB()

    toast.moveAngle(0, 200)

    toast.followLeft(3.4)

    toast.med_attachment(25)

    toast.moveInches(6, 400)

    toast.moveAngle(-8, 200)

    toast.moveInches(2, 400)

    toast.moveInches(-6, 400)

    toast.med_attachment_parallel(-25)

    toast.moveAngle(-92.5, 150)

    toast.followLeft(3.2)

    toast.med_attachment(50)

    toast.moveInches(3.5, 300)

    toast.moveAngle(-165, 200)

    toast.moveAngle(-130, 200)

    toast.Bridge()
