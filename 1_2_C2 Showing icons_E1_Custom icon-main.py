# MicroPython DIY Images
# https://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html#diy-images
# When run, the micro:bit should display an old-fashioned “Blue Peter” sailing ship with the masts dimmer than the boat’s hull.
from microbit import *
while True:
    if button_a.is_pressed():
        display.show(Image('05050:'
                           '05050:'
                           '05050:'
                           '99999:'
                           '09990'))