from microbit import *
while True:
    if button_a.is_pressed():
        display.show(Image.SILLY)
    if button_b.is_pressed():
        display.show(Image.DUCK)
