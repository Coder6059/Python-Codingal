from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("After School Routine Checker")
root.geometry("400x400")

heading = Label(root,text = "My After School Routine", font=("Arial", 15 , "bold" ))
heading.pack(pady=10)
instruction = Label(root, text = "Enter ur next after school activity:- ")
instruction.pack()

task_entry = Entry(root, width = 35)
task_entry.pack(pady = 8)

key_label = Label(root, text = "Last key pressed- None")
key_label.pack(pady = 5)

def handle_keypress(event):
    key_label.config(text = "Last key pressed- " + event.char)


task_entry.bind("<Key>", handle_keypress)

def handle_click(event):
    routine_message.config(text = "Routine Area Selected")

routine_message = Label(root, text= "Click here to check your routine", bg = "#d0efff", width = 32, height = 3)
routine_message.pack(pady = 10)

routine_message.bind("<Button-1>", handle_click)

def check_routine():
    task = task_entry.get()

    if task == "":
        messagebox.showwarning("Missing Task!", "Please enter an after school activity!")
    else:
        routine_message.config(text = "Next activity is: " + task)

check_button = Button(root, text = "Check Routine", command = check_routine)
check_button.pack(pady = 10)

root.mainloop()
