# All objects have a state and a behavior.

# The state of the object "cat" can be defined by the following
# characteristics: name, breed, age, happiness level etc.

# The behaviour of the object "cat" can be definied by
# the following actions or behaviours: e.g. meow, purr etc.

# A class is a definition of objects of the same kind
# A class is like a template or blueprint that defines and describes the
# characteristics (data) and behaviours (methods) of all objects of the same kind

# Let's use the micro:bit to simulate the behaviour of a cat.

from microbit import *

# Step 1
# Create a Cat class where the cat will react to various actions.

    # The __init__ method is a special method in Python called a constructor.
    # It is used to initialise the attributes of an object when it is created.
    # The __init__ method is automatically called when a new object
    # is created from a class.
    # The __init__ method (like all methods) always takes the parameter self
    # as its first argument.
    # The parameter self refers to the object itself,
    # allowing the method to access and modify its attributes.

class Cat:
# Step 2
# Define the Cat class as follows:
    def __init__ (self, name, breed, age, color, healthStatus, hungerlevel, happinesslevel):
        # characteristics (data)
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.healthStatus = healthStatus
        self.hungerLevel = hungerlevel
        self.happinessLevel = happinesslevel

# behaviours (methods)
    def meow(self):
        display.scroll('Meow!')

    def purr(self):
        display.scroll('Purrr ...')

    def eat(self):
        display.scroll('Eating!')
        self.hungerLevel = self.hungerLevel - 20
        self.happinessLevel = self.happinessLevel + 1
    
    def play(self):
        display.scroll('Playing! ')
        self.hungerLevel =self.hungerLevel+ 10
        self.happinessLevel = self.happinessLevel + 1

    def pain(self):
        display.scroll('Pain!')
        self.happinessLevel = self.happinessLevel - 2

# Step 3
# Create an object of the Cat class we defined above
my_cat = Cat("Whiskers", "Persian", 3, "Gray", "Healthy", 50, 6)

#Step 4
# use micro:bit to simulate the behaviour of the my_cat object we created above
while True:
    # Checks button input - both first, then each on its own
    if button_a.is_pressed() and button_b.is_pressed():           # pressing button a and button b the cat hurts
        my_cat.pain()
    elif button_a.is_pressed():                                   # by pressing button a the cat meows
        my_cat.meow()
    elif button_b.is_pressed():                                   # by pressing button b the cat purrs
        my_cat.purr()

    # Checks shake input - did this input happen since the last check?
    if accelerometer.was_gesture('shake'):                        # shake the microbit and the cat will eat
        my_cat.eat()

    # Checks sound input - did this input happen since the last check?
    if microphone.was_event(SoundEvent.LOUD):                     # speaking loudly on the microbit the cat was playing
        my_cat.play()

    # A short pause (0.1 seconds) gives time to press the second button before the next check
    sleep(100)
                   
