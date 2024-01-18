import time
from PIL import Image, ImageDraw, ImageFont
import lib.oled.SSD1331 as SSD1331
import os


class Screen:
    def __init__(self):
        os.system('sudo systemctl stop ip-oled.service')
        self.screen = SSD1331.SSD1331()
        self.screen.Init()
        self.screen.clear()
        self.image = Image.new("RGB", (self.screen.width, self.screen.height), "WHITE")
        self.draw = ImageDraw.Draw(self.image)
        self.font_small = ImageFont.truetype('./lib/oled/Font.ttf', 10)

    def show_message(self, message):

        if message == True:
            self.image = Image.open('./lib/oled/welcome.jpg')
        else:
            self.image = Image.open('./lib/oled/not_welcome.jpeg')

        self.screen.ShowImage(self.image, 0, 0)
        time.sleep(1)
        self.screen.clear()
