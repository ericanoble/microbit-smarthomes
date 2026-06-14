# Instead of button input use input from the touch logo, accelerometer, microphone, compass, light sensor or temperature sensor
from microbit import *
while True:
    if pin_logo.is_touched():
        display.scroll(display.read_light_level())