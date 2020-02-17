#!/usr/bin/env pybricks-micropython
import functions as toast

toast.moveInches(12, 800)

toast.left_motor.run_target(400,470)

toast.brick.display.text("Hello! My name is Joel", (0,45))

toast.wait(10000)