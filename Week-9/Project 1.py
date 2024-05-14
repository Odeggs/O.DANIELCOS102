import tkinter as tk
from tkinter import messagebox
import random

class Employee:
    def __init__(self, name):
        self.name = name
        self.tasks = ["Loading", "Transporting", "Reviewing Orders", "Customer Service", "Delivering Items"]

    def check_name(self, employees):
        return self.name in employees

    def take_attendance(self):
       
        pass

    def assign_task(self):
        return random.choice(self.tasks)

def submit_action():
    employee_name = name_entry.get()
    employee = Employee(employee_name)
    if employee.check_name(employees):
        employee.take_attendance()
        task = employee.assign_task()
        messagebox.showinfo("Task Assignment", f"Task for {employee_name}: {task}")
    else:
        messagebox.showinfo("Access Denied", "You are not on the list of employees.")

employees = ["Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu", "Stella Mankinde", "Jane Akibo", "Ago James", "Michell Taiwo", "Abraham Jones", "Nicole Anide", "Kosi Korso", "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima"]

root = tk.Tk()
root.title("Employee Attendance and Task Assignment")
root.geometry("400x600")
tk.Label(root, text="Enter your name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_action)
submit_button.pack()

root.mainloop()
