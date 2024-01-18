import neopixel
import board
import time
from config import *

class Led:
    def __init__(self):
        self.pixels = neopixel.NeoPixel(board.D18, 8, brightness=1.0/32, auto_write=False)

    def blink(self, R, G, B):
        self.pixels.fill((R, G, B))
        self.pixels.show()
        time.sleep(1)
        self.pixels.fill((0,0,0))
        self.pixels.show()    

    def card_blink():
        GPIO.output(led1, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led1, GPIO.LOW)       
