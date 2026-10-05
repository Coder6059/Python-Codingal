from tkinter import *
from datetime import date
window = Tk()
window.title("Demo Window")
window.geometry("400x300")

lbl = Label(text = "Hey there!", fg = "white", bg = "blue", height = 1, width = 300)
name_label = Label(text = "Enter your full name: ", bg = "yellow", fg="black")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = "Welcome to the application! Today's date is: "
    greet = "Hello " + name + "\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height = 3)
btn = Button(text = "Click Me!", command = display, height = 1, bg = "purple", fg= "white")

lbl.pack()
name_label.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()