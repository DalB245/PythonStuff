from tkinter import *


def submit():
    message = entry.get()
    print("Submitted: "+message)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

def toggle_password():
    entry.config(show="*e")
    pass_trigger_button.config(state=DISABLED)

window = Tk()  # create window
window.config(bg="#303030")

entry = Entry(window,
              font=("minecraft", 50),
              bg="#303030",
              fg="#ffffff",
              disabledbackground="#333333",
              disabledforeground="#a3a3a3")
entry.insert(0, "What's up?")

submit_button = Button(window, text="Submit", command=submit)
delete_button = Button(window, text="delete", command=delete)
backspace_button = Button(window, text="back", command=backspace)
pass_trigger_button = Button(window, text="Password mode", command=toggle_password)


# Pack all Objects to display
submit_button.pack(side=RIGHT)
delete_button.pack(side=RIGHT)
backspace_button.pack(side=RIGHT)
pass_trigger_button.pack(side=LEFT)
entry.pack(side=LEFT)


window.mainloop()  # Display the window
