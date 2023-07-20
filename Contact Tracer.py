#Import all necessary tools
from GUI import *
import csv
from tkinter import messagebox, simpledialog

#Create a class that inherits the previous class
class ContactFunctions(ContactTracingApp):
#Add button function
    def __init__(self):
        super().__init__()
        tk.Button(self.app, text='Add Entry', command=self.add_entry, bg='green', fg='white', font=('Arial', 20)).place(relx=0.4, y=720, anchor='center')
        tk.Button(self.app, text='Search Entry', command=self.search_entry, bg='blue', fg='white', font=('Arial', 20)).place(relx=0.6, y=720, anchor='center')
#Create an object for adding entries       
#Create an object for searching entries (ADMIN PASSWORD REQUIRED)
#Run the app
