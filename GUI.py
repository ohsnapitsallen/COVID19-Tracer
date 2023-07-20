#Import all necessary tools for the GUI
import tkinter as tk
import csv
from tkinter import ttk

#Create a class for the GUI
class ContactTracingApp:
#Set the design for the app
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("COVID-19 Tracer by OhSnapItsAllen")
        self.app.geometry("1280x720")
        self.app.config(bg='light blue')

#Add user inputs, gender will be a drop down menu
        self.name = tk.StringVar()
        self.email = tk.StringVar()
        self.phone = tk.StringVar()
        self.gender = tk.StringVar()
        self.date = tk.StringVar()
        self.recentcontacts = tk.StringVar()
#Design the inputs and text display
        tk.Label(self.app, text="Name", bg='light blue', font=('Arial', 20)).place(relx=0.5, y=120, anchor='center')
        tk.Entry(self.app, textvar=self.name, font=('Arial', 20)).place(relx=0.5, y=160, anchor='center')

        tk.Label(self.app, text="Email", bg='light blue', font=('Arial', 20)).place(relx=0.5, y=220, anchor='center')
        tk.Entry(self.app, textvar=self.email, font=('Arial', 20)).place(relx=0.5, y=260, anchor='center')

        tk.Label(self.app, text="Phone Number", bg='light blue', font=('Arial', 20)).place(relx=0.5, y=320, anchor='center')
        tk.Entry(self.app, textvar=self.phone, font=('Arial', 20)).place(relx=0.5, y=360, anchor='center')

        tk.Label(self.app, text="Date (YYYY-MM-DD)", bg='light blue', font=('Arial', 20)).place(relx=0.5, y=420, anchor='center')
        tk.Entry(self.app, textvar=self.date, font=('Arial', 20)).place(relx=0.5, y=460, anchor='center')

        tk.Label(self.app, text="Gender", bg='light blue', font=('Arial', 20)).place(relx=0.5, y=520, anchor='center')
        gender_dropdown = ttk.Combobox(self.app, textvariable=self.gender, values=["Male", "Female", "Other"], font=('Arial', 20))
        gender_dropdown.place(relx=0.5, y=560, anchor='center')

        tk.Label(self.app, text="Recent Contacts (comma separated)", bg='light blue', font=('Arial', 20)).place(relx=0.5, y=620, anchor='center')
        tk.Entry(self.app, textvar=self.recentcontacts, font=('Arial', 20)).place(relx=0.5, y=660, anchor='center')
#Create a function to run the program
