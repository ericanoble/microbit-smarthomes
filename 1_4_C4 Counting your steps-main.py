from microbit import *
steps = 0
while True:
    if accelerometer.was_gesture('shake'):
        steps+=1
    if button_a.was_pressed(): 
        display.show(steps)
        sleep(1000)
        display.clear()
    if button_b.was_pressed():
        steps = 0