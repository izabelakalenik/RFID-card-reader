from config import *
from button import Button
from connect_to_client import Connection
from card_reader import RFIDReader
from buzzer import Buzzer
from database import Database
from datetime import datetime

def main():
    red_button = Button(buttonRed)
    green_button = Button(buttonGreen)
    database = Database("workers.db")
    connection = Connection(database)
    card_reader = RFIDReader()
    buzzer = Buzzer(buzzerPin)
    database.create_database()
    
    
    while True:
        # gui
        read = card_reader.read()
        
        if(green_button.is_pressed() and not red_button.is_pressed() and read != None):
            print("adding")
            database.addWorker(read, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            buzzer.buzz_for(200)
            database.listWorkers()
        
        if(red_button.is_pressed() and not green_button.is_pressed() and read != None):
            #action to remove user from database (TODO: check if user exists in database class)
            print("removing")
            database.removeWorker(read)
            buzzer.buzz_for(200)
            database.listWorkers()
    
        buzzer.buzz()
        
    

if __name__== '__main__':
    main()
    