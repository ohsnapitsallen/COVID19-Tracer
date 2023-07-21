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
    def add_entry(self):
        new_entry = [self.name.get(), self.email.get(), self.phone.get(), self.date.get(), self.gender.get(), self.recentcontacts.get()]
        with open("contact_tracing.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_entry)
        messagebox.showinfo("Success", "Entry has been added successfully")
        
#Create an object for searching entries (ADMIN PASSWORD REQUIRED)
    def search_entry(self):
        self.admin_password = "redvelvet"
        password = simpledialog.askstring("Admin Password", "Enter admin password:", show='*')
        if password != self.admin_password:
            messagebox.showerror("Error", "Invalid password")
            return
        
        name = self.name.get()
        date = self.date.get()
        with open("contact_tracing.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == name.lower() and row[3] == date:
                    messagebox.showinfo("Found", f"Entry found: {row}")
                    return
        messagebox.showinfo("Not Found", "No entry found")
        
#Run the app
