from tkinter import *
import json


# I left notes on the README.md
class TaskInterface:
    FONT = ("Comic Sans", 12)

    def __init__(self):
        self.window = Tk()
        self.window.title("Tasks")
        self.window.config(padx=25, pady=25)

        with open("./Data/test.json") as file:
            data = json.load(file)
        data = list(data.keys())
        data.insert(0, "No project selected")
        self.project_label = Label(text="Project:", font=self.FONT)
        self.project_spinbox = Spinbox(width=30, values=tuple(data), font=self.FONT)
        self.new_project_label = Label(text="New Project:", font=self.FONT)
        self.new_project_entry = Entry(width=30, font=self.FONT)
        self.task_label = Label(text="Task:", font=self.FONT)
        self.task_entry = Entry(width=30, font=self.FONT)

        self.search_button = Button(text="Search", font=self.FONT)
        self.save_button = Button(width=20, text="Save", font=self.FONT)

        self.project_label.grid(column=0, row=0)
        self.project_spinbox.grid(column=1, row=0)
        self.new_project_label.grid(column=0, row=1)
        self.new_project_entry.grid(column=1, row=1)
        self.task_label.grid(column=0, row=2)
        self.task_entry.grid(column=1, row=2)
        self.search_button.grid(column=2, row=0)
        self.save_button.grid(column=0, row=3, columnspan=3)
        self.window.mainloop()


task = TaskInterface()
