from tkinter import *
from tkinter import messagebox


def click():
    answer = messagebox.askquestion(title="Clicked!", message="Do you want to download a Virus?")
    if answer == "yes":print("You are downloading a Virus :O")
    else:print("You escaped the Virus :)")

    #messagebox.askyesno("Clicked!", "Do you want to Download a Virus?")

    #if messagebox.askokcancel("Click", "You will download a Virus!"):
        #print("He clicked")
        #button.config(state=DISABLED, text="Downloading VIRUS...")
    #else:
        #print("He canceled")
        #button.config(state=DISABLED, text="Canceled")
#while True:
    #messagebox.showwarning("Ahhhhhh", "YOU GOT A VIRUS!!!")


window = Tk()

button = Button(window, command=click, text="free ROBUX!!!", font=("Impact", 20))
button.pack()

window.mainloop()
