#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

med_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)

# This makes the medium motor attachment move up when the up button is pushed
# and move down when the down button is pushed.

while True:
    if Button.DOWN in brick.buttons():
        med_motor.dc(-75)
    elif Button.UP in brick.buttons():
        med_motor.dc(75)
    elif Button.RIGHT in brick.buttons():
        med_motorB.dc(75)
    elif Button.LEFT in brick.buttons():
        med_motorB.dc(-75)
    else:
        med_motor.stop(Stop.BRAKE)
