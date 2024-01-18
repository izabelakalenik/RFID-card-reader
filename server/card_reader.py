#!/usr/bin/env python3

from mfrc522 import MFRC522
from config import *

# gdy nie przylozona to 2
# gdy przylozony to na zmiane 2, 0, 2, 0
class RFIDReader:
    def __init__(self):
        self.MIFAREReader = MFRC522()

        self.read1 = False
        self.read2 = False

    def read(self):
        to_return = None
        cur = False

        (status, _) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)
        # print(status)
        if status == self.MIFAREReader.MI_OK:
            (status, uid) = self.MIFAREReader.MFRC522_Anticoll()
            if status == self.MIFAREReader.MI_OK:
                cur = True
                # gdy oba poprzedni odczyty byly False -> nowy odczyt
                if (not self.read1 and not self.read2):
                    num = 0
                    for i in range(0, len(uid)):
                        num += uid[i] << (i*8)
                    to_return = num
                    # self.buzzer()

        self.read1 = self.read2
        self.read2 = cur
        
        return to_return
