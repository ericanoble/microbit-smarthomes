from microbit import *
counter = 0
while True:    
    display.show(counter)
    if button_a.was_pressed():
        counter+=1
    if button_b.was_pressed():
        counter-=1 