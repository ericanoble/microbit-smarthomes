from microbit import *
import music
while True:
    if button_a.was_pressed():
        set_volume(75)
        music.play(music.ODE, wait=False)
    if button_b.was_pressed():
        music.stop()