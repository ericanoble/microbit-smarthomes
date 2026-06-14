from microbit import *
import music
while True:
    if button_a.is_pressed():
        set_volume(75)
        music.play(['e:3', 'c:6'])
        music.stop()