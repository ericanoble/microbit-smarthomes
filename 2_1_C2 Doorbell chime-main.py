from microbit import *
import music
while True:
    if button_a.is_pressed():
        set_volume(75)
        music.set_tempo(bpm=125)
        music.play(['b','g','a','d','d','a','b','g'])
        music.stop()