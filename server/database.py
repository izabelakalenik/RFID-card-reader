#!/usr/bin/env python3

import sqlite3
import os

class Database:
    
    def __init__(self, db_name="workers.db"):
        self.db_name = db_name # name of database

    # create database
    def create_database(self):
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
            print("An old database removed.")
        connection = sqlite3.connect(self.db_name)
        
        cursor = connection.cursor()
        cursor.execute(""" CREATE TABLE workers (
            card_id text PRIMARY KEY,
            first_name text,
            last_name text,
            registration_date text
        )""")

        cursor.execute(""" CREATE TABLE workers_log (
            log_time text,
            worker text,
            terminal_id text
        )""")
        connection.commit()
        connection.close()
        print("The new database created.")

    # add a worker with all data
    # addWorker("420", "Mikolaj", "Jastrzembski", "2024-01-10")
    def addWorker(self, card_id, first_name, last_name, registration_date):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        
        if not self.checkIfExists(card_id):
            cursor.execute("INSERT INTO workers VALUES (?, ?, ?, ?)", (card_id, first_name, last_name, registration_date))
            print(f"Worker {first_name} {last_name} added.")
        else:
            print("Worker already exists.")
        
        connection.commit()
        connection.close()
        
    # add a worker only with card ID
    # addWorker("420", "2024-01-10")
    def addWorker(self, card_id, registration_date):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        
        if not self.checkIfExists(card_id):
            cursor.execute("INSERT INTO workers VALUES (?, ?, ?, ?)", (card_id, "", "", registration_date))
            print(f"Worker added using quick registration.")
        else:
            print("Worker already exists.")
        
        connection.commit()
        connection.close()

    # remove a worker
    def removeWorker(self, card_id):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        
        if self.checkIfExists(card_id):
            cursor.execute("DELETE FROM workers WHERE card_id = ?", (card_id,))
            print(f"Worker with card ID {card_id} removed.")
        else:
            print("Worker does not exist.")
        
        connection.commit()
        connection.close()

    # add a log entry
    # addLog("2024-01-11 10:00", "420", "terminalX")
    def addLog(self, log_time, worker_card_id, terminal_id):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        
        cursor.execute("INSERT INTO workers_log VALUES (?, ?, ?)", (log_time, worker_card_id, terminal_id))
        print("Log entry added.")
        
        connection.commit()
        connection.close()

    # check if a worker exists
    # removeWorker("420")
    def checkIfExists(self, card_id):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM workers WHERE card_id = ?", (card_id,))
        result = cursor.fetchone()
        
        connection.close()
        return result is not None
    
    def listWorkers(self):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM workers")
        workers = cursor.fetchall()
        
        print("\nListing workers:")
        if(len(workers) == 0):
            print("No workers in database")
        for worker in workers:
            print(worker)
        
        connection.close()