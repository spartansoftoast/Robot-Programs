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
    toast.moveAngle(77, 120, 0)

    # This lowers the leverator so it can slide under the left blue lever on the crane.
    toast.med_attachment_parallel(-90)

    # This makes the robot move toward the crane.
    toast.moveInches(10 , 300, 0)

    # This turns the robot torward the crane.

    toast.moveAngle(-43, 120, 0)

    # This reliably gets to the position needed to lift the crane lever.

    toast.moveInches(1.5, 255, 0)

    # This lifts the crane lever.
    toast.med_attachment(50)

    # This moves the robot back.
    toast.moveInches(-2, 300, 0)

    # This turns the robot to face near the base.

    toast.moveAngle(-150, 240, 0)

    # This resets the medium motor for the next mission.

    toast.med_attachment_parallel(-45)

    # This moves the robot in position to make it into the base.

    toast.moveInches(7, 800, 0)

    # This turns the robot to face the base.

    toast.moveAngle(-90, 300, 0)

    # This moves the robot into the base.

    toast.moveInches(18.5, 800, 0) 

   # This gets the medium motor ready for the next mission: Elevator.

    toast.med_attachment(-8)

def Innovative_A():
    toast.gyro.reset_angle(0)
    toast.brick.sound.beep()
    toast.wait(750)

    # This turns the robot to face the black circle near the tree.

    toast.moveAngle(-40, 200, 0)

    # This pushes the Innovative Architecture into the circle.

    toast.moveInches(16, 350, 0)

    # This moves the robot backward away from the Innovative Architecture.

    toast.moveInches(-8, 350, 0)

    # This turns the robot to the right, so that it is facing into base.

    toast.moveAngle(10, 500, 0)

    # This moves the robot into base.

    toast.moveInches(-27, 1100, 0)

def Tan_Elevator():
    toast.gyro.reset_angle(0)
    toast.brick.sound.beep()
    toast.wait(750)

    # This turns the robot toward the circle next to the Elevator.

    toast.moveAngle(-20, 60, 0)

    toast.wait(250)

    # This moves the robot forward to the circle next to the Elevator.

    toast.moveInches(40, 400, 0)

    # This checks for the white line to check the position of the robot.

    toast.moveWhite()

    # This turns the robot to face the tan circle.

    toast.moveAngle(-35, 80)

    # This pushes the tan block into the circle.

    toast.moveInches(6, 300, 0)

    # This moves the robot back to the white line.

    toast.moveWhiteB()

    # This moves the robot to face the Elevator.

    toast.moveAngle(20, 200)

    # This moves the robot to the white line.

    toast.moveWhite()

    # This moves the robot farther so that it can catch the line for line following.

    toast.moveInches(2, 300)

    # This turns the robot onto the line.

    toast.moveAngle(-5, 100)

    # This line follows toward the elevator.

    toast.followLeft(2.65)

    # This lifts the medium motor so that it does not hit the white block.

    toast.med_attachment(25)

    # This knocks over the elevator.

    toast.moveInches(4, 200, 0)

    # This moves the medium motor down for catching the white line.

    toast.med_attachment_parallel(-25)

    # This moves the robot backward towards the white line.

    toast.moveWhiteB()

    # This lifts the medium motor so that it does not hit the safety factor.

    toast.med_attachment_parallel(90)

    # This moves the motor back to align it to hit the safety factor.

    toast.moveInches(-2, 300)

    # This turns the robot ot hit the safety factor.

    toast.moveAngle(85, 200)

    # This moves forward to hit the safety factor.

    toast.moveInches(3, 100)

    # This moves backward in preparation to hit two more pegs.

    toast.moveInches(-2, 200)

    # This moves the left motor backward so that we can hit the two pegs.

    toast.left_motor.reset_angle(0)

    toast.left_motor.run_target(200, -390, toast.Stop.BRAKE, True)

    # This lowers the medium motor for hitting the pegs.

    toast.med_attachment(-80)

    # This moves the robot so that it can hit the pegs.

    toast.moveInches(3, 200)

    # This turns the robot to hit the pegs.

    toast.left_motor.reset_angle(0)

    toast.left_motor.run_target(200, -90, toast.Stop.BRAKE, True)

    # This makes sure the medium motor hits the pegs.

    toast.med_attachment(-8)

    # This moves the robot out of the safety factor.

    toast.moveInches(-4, 400)

    # This turns the robot so that we can go back to base.

    toast.moveAngle(-20, 200)

    # This moves the robot back into base.

    toast.moveInches(-73.5, 700)

    # This resets the medium motor for the next mission.

    toast.med_attachment(-2)

def Traffic_Red_Circle_Bridge():
    toast.gyro.reset_angle(0)
    toast.brick.sound.beep()
    toast.wait(750)

    # This moves the robot forward to lift the traffic jam.

    toast.moveInches(23, 400, 0)

    # This lifts the traffic jam.

    toast.med_attachment(40, 1)

    # This makes sure the traffic jam is lifted.

    toast.moveAngle(20, 200)

    # This send the medium motor down to catch the red block.

    toast.med_attachment_parallel(-30)

    # This turns the robot to face the red circle.

    toast.moveAngle(-55, 200)

    # This lifts the medium motor so that it does not drag the block out of the circle.

    toast.med_attachment_parallel(20)

    # This pushes the red block into the red circle.

    toast.moveInches(6.5, 400)

    # This brings the medium motor down to catch the white line.

    toast.med_attachment_parallel(-30)

    # This moves the robot backward toward the white line.

    toast.moveWhiteB()

    # This lines the robot up with the line for line following.

    toast.moveAngle(0, 200)

    # This line follows toward the swing.

    toast.followLeft(3.4)

    # This lifts the medium motor so that it can hit the swing.

    toast.med_attachment(25)

    # This moves the robot forward toward the swing.

    toast.moveInches(6, 400)

    # This turns the robot to hit the post holding the swing.

    toast.moveAngle(-8, 200)

    # This hits the post holding the swing.

    toast.moveInches(2, 400)

    # This moves the robot out of the swing.

    toast.moveInches(-6, 400)

    # This moves the medium motor down for line following.

    toast.med_attachment_parallel(-25)

    # This turns the robot to face the line going toward the bridge.

    toast.moveAngle(-97.5, 150)

    # This line follows toward the bridge.

    toast.followLeft(3.2)

    # This lifts the medium motor so that it does not catch on the bridge.

    toast.med_attachment(50)

    # This moves the robot forward toward the bridge because the line ends.

    toast.moveInches(3.5, 300)

    # This turns the robot so that it makes it onto the bridge.

    toast.moveAngle(-165, 200)

    # This turns the robot again to make sure it is on the bridge.

    toast.moveAngle(-130, 200)

    # This calles a function that moves the robot up the bridge until it reaches the top.

    toast.Bridge()
