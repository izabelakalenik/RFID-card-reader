import paho.mqtt.client as mqtt
from database import Database
from datetime import datetime


class Connection:
    def __init__(self, database):
        self.database: Database = database
        self.broker = "10.108.33.123"  # ip address of a server
        self.client = mqtt.Client()
        self.client.connect(self.broker)
        self.client.on_message = self.process_message
        self.client.loop_start()
        self.client.subscribe("client/authorization")

    def process_message(self, client, userdata, message):
        message_decoded = (str(message.payload.decode("utf-8"))).split(".")

        device_id = message_decoded[0]
        card_id = message_decoded[1]

        if self.database.checkIfExists(card_id):
            self.database.addLog(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), card_id, device_id)
            self.send_authorization_response(device_id, True)
        else:
            self.send_authorization_response(device_id, False)

    def send_authorization_response(self, receiver_id, authorized: bool):
        if authorized:
            message = "true"
        else:
            message = "false"
        self.client.publish("server/authorization", receiver_id + "." + message)
