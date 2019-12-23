#!/usr/bin/env pybricks-micropython
import functions as toast

while not any(toast.brick.buttons()):
    toast.gyroDrift()
    pass
toast.brick.sound.beep()
toast.wait(750)

toast.moveInches(-16.5, 200, 0)
toast.wait(250)
toast.moveInches(15, 200, 0)
toast.wait(250)
toast.moveAngle(60, 50)
toast.wait(250)
toast.moveInches(16, 200, 0)
toast.wait(250)
toast.moveAngle(-200, 50)