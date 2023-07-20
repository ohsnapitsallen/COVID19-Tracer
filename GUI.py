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
#Design the inputs and text display
#Create a function to run the program
