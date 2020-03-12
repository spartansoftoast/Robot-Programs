#!/usr/bin/env pybricks-micropython
import functions as toast


def Big_Boy_Drone_Bat():
    toast.gyro.reset_angle(0)
    toast.brick.sound.beep()
    toast.wait(750)

    # This turns the robot toward the circle next to the Elevator.

    toast.moveAngle(-20, 60, 0)

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

    toast.moveInches(2.5, 100)

    # This moves backward in preparation to hit two more pegs.

    toast.moveInches(-1.5, 200)

    # This moves the left motor backward so that we can hit the two pegs.

    toast.left_motor.reset_angle(0)

    toast.left_motor.run_target(200, -390, toast.Stop.BRAKE, True)

    # This lowers the medium motor for hitting the pegs.

    toast.med_attachment(-70)

    # This moves the robot so that it can hit the pegs.

    toast.moveInches(3, 200)

    # This turns the robot to hit the pegs.

    toast.left_motor.reset_angle(0)

    toast.left_motor.run_target(200, -90, toast.Stop.BRAKE, True)

    # This makes sure the medium motor hits the pegs.

    toast.med_attachment(-18)

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

    toast.med_attachment(0)
    toast.moveAngle(-20, 20, 2)

    # This moves the robot forward to lift the traffic jam.

    toast.moveInches(25, 50)

    toast.moveInches(-10, 50)

    toast.moveAngle(-90, 40, 1)

    toast.moveInches(-5)

    toast.moveAngle(-5, 40, 1)

    toast.moveInches(6)
    toast.med_attachment(30)
    toast.pivotTurn(5, 20, 1)
    toast.pivotTurn(-10, 20, 1)
    toast.moveWhite()
    toast.followLeft(4)
    toast.moveInches(6)
    toast.med_attachment(40)
    toast.moveInches(3)
    toast.moveWhiteB()
    toast.moveAngle(-25, 40, 2)
    toast.moveInches(12)
    toast.moveAngle(-90, 20, 2)
    toast.moveInches(2)
    toast.moveInches(-4)
    toast.moveAngle(-90, 40, 2)
    toast.moveInches(8)
    # This turns the robot to face the red circle.
    toast.wait(1000000)


    toast.moveInches(5, 80)

    # This moves the robot backward toward the white line.

    toast.moveWhiteB()

    # This lines the robot up with the line for line following.

    toast.moveAngle(0, 20, 1)

    # This line follows toward the swing.

    toast.followLeft(3.4)

    # This lifts the medium motor so that it can hit the swing.

    toast.med_attachment(25)

    # This moves the robot forward toward the swing.

    toast.moveInches(6, 400)

    # This turns the robot to hit the post holding the swing.

    toast.moveAngle(-8, 20, 2)

    # This hits the post holding the swing.

    toast.moveInches(2, 40)

    # This moves the robot out of the swing.

    toast.moveInches(-6, 40)

    # This moves the medium motor down for line following.

    toast.med_attachment(0)

    # This turns the robot to face the line going toward the bridge.

    toast.moveAngle(-95, 15, 2)

    # This line follows toward the bridge.

    toast.followLeft(3.2)

    # This lifts the medium motor so that it does not catch on the bridge.

    toast.med_attachment(50)

    # This moves the robot forward toward the bridge because the line ends.

    toast.moveInches(3.5, 30)

    # This turns the robot so that it makes it onto the bridge.

    toast.moveAngle(-165, 20, 2)

    # This turns the robot again to make sure it is on the bridge.

    toast.moveAngle(-130, 20, 1)

    # This calles a function that moves the robot up the bridge until it reaches the top.

    toast.Bridge()

def Crane():
  toast.medium_motor_down(-130, 0)
  toast.moveInches(24, 40)
  toast.moveInches(-10)
  toast.spinTurn(50, 30)
  toast.moveInches(5)
  toast.spinTurn(-50, 30)

