#!/usr/bin/env pybricks-micropython
import functions as toast

while not any(toast.brick.buttons()):
    toast.gyroDrift()
    pass
toast.brick.sound.beep()
toast.wait(750)


# This moves the robot to the Traffic Jam
toast.med_motor.run_time(-1500, 1000)
toast.moveInches(23, 200, 0)
# This lifts the Traffic Jam
toast.med_motor.run_time(1500, 2000)
toast.moveAngle(20, 20, 1)
toast.wait(500)
toast.moveAngle(-20, 20, 1)
toast.moveInches(-35, 200, 0)
toast.moveAngle(-120, 20, 1)