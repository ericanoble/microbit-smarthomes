from microbit import *
import music
set_volume(75)
current_song_number = 0
current_song = music.RINGTONE
while True:
    display.show(current_song_number)
    if button_a.was_pressed():
        music.play(current_song, wait=False)
    if button_b.was_pressed():
        music.stop()
        current_song_number += 1
        if current_song_number > 2:
            current_song_number = 0
        if current_song_number == 0:
            current_song = music.RINGTONE
        elif current_song_number == 1:
            current_song = music.ODE
        elif current_song_number == 2:
            current_song = music.BADDY