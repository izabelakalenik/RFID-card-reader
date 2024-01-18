# client

import paho.mqtt.client as mqtt
from screen import Screen
from led import Led


class Connection:
    def __init__(self):
        self.broker = "10.108.33.127"
        self.client = mqtt.Client()
        self.client.connect('10.108.33.127')
        self.client.on_message = self.process_message
        self.client.loop_start()
        self.client.subscribe("server/authorization")
        self.device_id = "1"
        self.screen = Screen()
        self.led = Led()
        
    
    def process_message(self, client, userdata, message):
        message_decoded = (str(message.payload.decode("utf-8"))).split(".")
        
        device_id = message_decoded[0]
        message = message_decoded[1]
        
        if device_id == self.device_id and message == "true":
            self.entrance(True)
        elif(device_id == self.device_id):
            self.entrance(False)
        
    def send_authorization_request(self, card_number: str):
        self.client.publish("client/authorization", self.device_id + "." + card_number)


    def entrance(self, enabled):
            if enabled == True:
                self.led.blink(0, 255, 0)
                self.screen.show_message(True)
                print(str(enabled))
            else:
                self.led.blink(255, 0, 0)
                self.screen.show_message(False)
                print(str(enabled))
