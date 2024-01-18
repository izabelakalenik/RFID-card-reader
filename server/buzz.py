from config import *
from datetime import datetime, timedelta


class Buzzer:
    def __init__(self, buzzer_pin):
        self.buzzer_pin = buzzer_pin
        self.buzz_until = datetime.now() - timedelta(milliseconds=1000)

    def buzz_for(self, miliseconds: int):
        self.buzz_until = datetime.now() + timedelta(milliseconds=miliseconds)

    def buzz(self):
        GPIO.output(buzzerPin, datetime.now() > self.buzz_until)
