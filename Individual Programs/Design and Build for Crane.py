#!/usr/bin/env pybricks-micropython
import functions as toast

# This tells the robot to display the GyroSensor so that we can see if the Gyro is drifting.
# If the Gyro is not drifting, we push a button on the robot and it starts the program.

while not any(toast.brick.buttons()):
    toast.gyroDrift()
    pass
toast.brick.sound.beep()
toast.wait(750)

# This makes the robot deliver the units to the black circle near the crane.
toast.moveInches(17, 75, 0)
toast.wait(500)

# This makes the robot back away from black circle mentioned above.
toast.moveInches(-5, 300, 0)
toast.wait(505)

# Turn robot to the right.
toast.moveAngle(75, 175, 1)
toast.wait(250)

# This lowers the leverator so it can slide under the left blue lever on the crane.
toast.med_attachment_parallel(-110, 1)
toast.wait(100)

# This makes the robot move toward the crane.
toast.moveInches(15 , 300, 0)
toast.wait(250)
toast.moveAngle(-115, 125, 1)
toast.wait(250)

# This reliably gets to the position needed to lift the crane lever.
toast.moveWhite()
toast.wait(250)
toast.moveBlack()
toast.wait(250)

# This lifts the crane lever.
toast.med_attachment(50,1)
toast.wait(250)

# This moves the robot into the base.
toast.moveAngle(-90, 125, 1)
toast.wait(250)

# This gets the leverator ready for the next mission: Elevator.
toast.med_attachment_parallel(-50,1)  
toast.moveInches(30, 300, 0)