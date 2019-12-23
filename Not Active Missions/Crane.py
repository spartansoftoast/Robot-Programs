#!/usr/bin/env pybricks-micropython
import functions as toast

while not any(toast.brick.buttons()):
    toast.gyroDrift()
    pass
toast.brick.sound.beep()
toast.wait(500)
