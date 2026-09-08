# MicroPython Animation
# https://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html#images
# This animation incorporates a built-in image of a heart and custom images
# with varying brightness so that when button a and b are pressed the heart fades
from microbit import *
while True:
    if button_a.is_pressed and button_b.is_pressed():
        display.show(Image.HEART)
        sleep(500)
        display.show(Image("07070:"
                           "77777:"
                           "77777:"
                           "07770:"
                           "00700"))
        sleep(500)
        display.show(Image("05050:"
                           "55555:"
                           "55555:"
                           "05550:"
                           "00500"))
        sleep(500)
        display.show(Image("03030:"
                           "33333:"
                           "33333:"
                           "03330:"
                           "00300"))
        sleep(500)
        display.show(Image("01010:"
                           "11111:"
                           "11111:"
                           "01110:"
                           "00100"))
        sleep(500)
