from config import *

class Button:
    def __init__(self, buttonPin: int):
        self.pin = buttonPin
        
    def is_pressed(self):
        return GPIO.input(self.pin) == 0