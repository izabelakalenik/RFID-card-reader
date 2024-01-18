import tkinter as tk
from tkinter import ttk
import sqlite3

def load_workers_data():
    for row in tree_workers_data.get_children():
        tree_workers_data.delete(row)
    conn = sqlite3.connect('workers.db')
    cursor = conn.cursor()


    query = "SELECT card_id, first_name, last_name, registration_date FROM workers"
   
    cursor.execute(query)
    records = cursor.fetchall()
    for row in records:
        tree_workers_data.insert('', tk.END, values=row)
    conn.close()

def load_workers_logs_data():
    for row in tree_logs.get_children():
        tree_logs.delete(row)
    conn = sqlite3.connect('workers.db')
    cursor = conn.cursor()

    query = """
        SELECT w.card_id, w.first_name, w.last_name, wl.log_time, wl.terminal_id
        FROM workers_log wl
        JOIN workers w ON wl.worker = w.card_id
        """
    
    cursor.execute(query)
    records = cursor.fetchall()
    for row in records:
        tree_logs.insert('', tk.END, values=row)
    conn.close()

def update_data():
    conn = sqlite3.connect('workers.db')
    cursor = conn.cursor()
    selected_item = tree_workers_data.focus()
    if selected_item:
        worker_id = tree_workers_data.item(selected_item)['values'][0]
        new_first = first_name_entry.get()
        new_last = last_name_entry.get()
        query = "UPDATE workers SET first_name = ?, last_name = ? WHERE card_id = ?"
        cursor.execute(query, (new_first, new_last, worker_id))
        conn.commit()
        load_workers_data()
    conn.close()

app = tk.Tk()
app.title("Worker Data Viewer")
app.geometry("800x500")

# Notebook for tabbed interface
notebook = ttk.Notebook(app)
notebook.pack(expand=True, fill='both')

# Tab for Workers Data
workers_frame = tk.Frame(notebook)
notebook.add(workers_frame, text='Workers Data')

# Treeview widget for the table
tree_workers_data = ttk.Treeview(workers_frame, columns=('Card ID', 'First Name', 'Last Name', 'Registration Date'), show='headings')
tree_workers_data.heading('Card ID', text='Card ID')
tree_workers_data.heading('First Name', text='First Name')
tree_workers_data.heading('Last Name', text='Last Name')
tree_workers_data.heading('Registration Date', text='Registration Date')
tree_workers_data.column('Card ID', width=100)
tree_workers_data.column('First Name', width=150)
tree_workers_data.column('Last Name', width=150)
tree_workers_data.column('Registration Date', width=150)
tree_workers_data.pack(expand=True, fill='both')

# Input fields and update button for workers data
workers_input_frame = tk.Frame(workers_frame)
workers_input_frame.pack(pady=10)

first_name_label = tk.Label(workers_input_frame, text="First Name")
first_name_label.grid(row=0, column=0, padx=5, pady=5)
first_name_entry = tk.Entry(workers_input_frame)
first_name_entry.grid(row=0, column=1, padx=5, pady=5)

last_name_label = tk.Label(workers_input_frame, text="Last Name")
last_name_label.grid(row=0, column=2, padx=5, pady=5)
last_name_entry = tk.Entry(workers_input_frame)
last_name_entry.grid(row=0, column=3, padx=5, pady=5)

load_button = tk.Button(workers_input_frame, text="Refresh Data", command=load_workers_data)
load_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
update_button = tk.Button(workers_input_frame, text="Update Data", command=update_data)
update_button.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky="ew")



# Tab for Workers Logs
workers_logs_frame = tk.Frame(notebook)
notebook.add(workers_logs_frame, text='Workers Logs')

# Treeview widget for the table
tree_logs = ttk.Treeview(workers_logs_frame, columns=('Card ID', 'First Name', 'Last Name', 'Log time', 'Terminal id'), show='headings')
tree_logs.heading('Card ID', text='Card ID')
tree_logs.heading('First Name', text='First Name')
tree_logs.heading('Last Name', text='Last Name')
tree_logs.heading('Log time', text='Log time')
tree_logs.heading('Terminal id', text='Terminal id')
tree_logs.column('Card ID', width=100)
tree_logs.column('First Name', width=150)
tree_logs.column('Last Name', width=150)
tree_logs.column('Log time', width=150)
tree_logs.column('Terminal id', width=150)
tree_logs.pack(expand=True, fill='both')

# Input fields and update button for workers data
input_frame = tk.Frame(workers_logs_frame)
input_frame.pack(pady=10)

# Button to load workers logs data
load_logs_button = tk.Button(input_frame, text="Refresh Workers Logs", command=load_workers_logs_data)
load_logs_button.pack(pady=10)

# Initialize with workers data
load_workers_data()
load_workers_logs_data()

app.mainloop()
