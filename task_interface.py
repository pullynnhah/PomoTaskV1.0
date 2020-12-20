from tkinter import *
import json


# I left notes on the README.md
class TaskInterface:
    FONT = ("Comic Sans", 12)

    def __init__(self, projects):
        self.window = Tk()
        self.window.title("Tasks")
        self.window.config(padx=25, pady=25)

        self.project_label = Label(text="Project:", font=self.FONT)
        self.project_spinbox = Spinbox(width=30,
                                       values=self.get_projects(projects),
                                       font=self.FONT)

        self.new_project_label = Label(text="New Project:", font=self.FONT)
        self.new_project_entry = Entry(width=30, font=self.FONT)

        self.new_task_label = Label(text="New Task:", font=self.FONT)
        self.new_task_Spinbox = Entry(width=30,
                                      values=self.get_tasks(projects),
                                      font=self.FONT)
        self.task_label = Label(text="Task:", font=self.FONT)
        self.task_entry = Entry(width=30, font=self.FONT)
        self.subtask_label = Label(text="Subtask:", font=self.FONT)
        self.subtask_entry = Entry(width=30, font=self.FONT)


        self.search_button = Button(text="Search", font=self.FONT)
        self.save_button = Button(width=20, text="Save", font=self.FONT)

        self.project_label.grid(column=0, row=0)
        self.project_spinbox.grid(column=1, row=0)
        self.new_project_label.grid(column=0, row=1)
        self.new_project_entry.grid(column=1, row=1)
        self.new_task_label.grid(column=0, row=2)
        self.new_task_entry.grid(column=1, row=2)
        self.subtask_label.grid(column=0, row=3)
        self.subtask_entry.grid(column=1, row=3)
        self.search_button.grid(column=2, row=0)

        self.save_button.grid(column=0, row=4, columnspan=3)
        self.window.mainloop()

    def create_project(self):
        pass

    def get_projects(self):
        pass


task = TaskInterface()
