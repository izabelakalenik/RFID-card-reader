# RFID card reader

This project, developed as part of an Internet of Things (IoT) course - 5th semester, was done in a group of 4 people. 

The primary goal is to create a **RFID Card Reader Employee Registration System** using two Raspberry Pi devices. 
The first device functions as the server, responsible for employee card registration, 
while the second acts as the "entry door," equipped with a card scanning mechanism.

## Key Features
* **Server-Door Architecture:** The system consists of two Raspberry Pi devices, with one designated as the server and the other as the entry door for card scanning.
* **Card Registration:** The server is responsible for registering RFID cards, storing relevant information in a SQLite database. The graphical user interface (GUI) on the server allows users to input additional details such as the employee's first and last name, alongside the card ID and registration date.
* **Access Control:** Only registered cards within the database grant access through the entry door, enhancing security and access control measures.

## Technologies
* **RFID Card Reader Integration:** The project incorporates a proximity card reader (RFID) to facilitate seamless card scanning at the entry door.
* **MQTT Protocol:** The project utilizes the MQTT (Message Queuing Telemetry Transport) protocol for communication between the server and the entry door, ensuring efficient and reliable data exchange.
* **SQLite Database:** Information about registered cards, including employee details, is stored in an SQLite database, providing a structured and accessible data storage solution.
* **Tkinter Library:** The graphical user interface is implemented using the Tkinter library, allowing for a user-friendly interaction with the server.
