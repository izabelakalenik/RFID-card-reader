from config import *
import time

class Buzzer:
    def __init__(self, buzzer_pin):
        self.buzzer_pin = buzzer_pin

    def card_buzzer(self):
        GPIO.output(buzzerPin, False)
        time.sleep(1.0)
        GPIO.output(buzzerPin, True)    