# MicroPython Animation
# https://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html#animation
# In this example as the boat sinks to the bottom of the display the animation speeds up
from microbit import *
while True:
    if button_a.is_pressed and button_b.is_pressed():
        display.show(Image("05050:"
                           "05050:"
                           "05050:"
                           "99999:"
                           "09990"))
        sleep(1000)
        display.show(Image("00000:"
                           "05050:"
                           "05050:"
                           "05050:"
                           "99999"))
        sleep(800)
        display.show(Image("00000:"
                           "00000:"
                           "05050:"
                           "05050:"
                           "05050"))
        sleep(600)
        display.show(Image("00000:"
                           "00000:"
                           "00000:"
                           "05050:"
                           "05050"))
        sleep(400)
        display.show(Image("00000:"
                           "00000:"
                           "00000:"
                           "00000:"
                           "05050"))
        sleep(200)
        display.show(Image("00000:"
                           "00000:"
                           "00000:"
                           "00000:"
                           "00000"))
        sleep(50)