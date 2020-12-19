from tkinter import *

window = Tk()
window.title("Tasks")
window.config(padx=25, pady=25)

project_label = Label(text="Project:")
project_entry = Entry(width=30)

project_label.grid(column=0, row=0)
project_entry.grid(column=1, row=0)

window.mainloop()
