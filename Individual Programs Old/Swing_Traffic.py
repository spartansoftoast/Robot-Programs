#!/usr/bin/env pybricks-micropython
import functions as toast

# This tells the robot to display the GyroSensor so that we can see if the Gyro is drifting.
# If the Gyro is not drifting, we push a button on the robot and it starts the program.

while not any(toast.brick.buttons()):
    toast.gyroDrift()
    pass
toast.brick.sound.beep()
toast.wait(750)

# This moves the robot to the Traffic Jam, so that the attachment is under the Traffic Jam.

toast.moveInches(23.6, 250, 0)
toast.robot.stop(toast.Stop.BRAKE)
toast.wait(250)

# This lifts the Traffic Jam.

toast.med_attachment(40, 1)

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