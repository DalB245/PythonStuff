from tkinter import *

click_count = 0


def click():
    global click_count
    click_count += 1
    if click_count >= 10:
        print("Clicked " + str(click_count) + " times! :)")
    else:
        print("Clicked " + str(click_count) + " times")


window = Tk()
window.config(background="#855cd6")

follow_photo = PhotoImage(file="Follow.png")

button = Button(window,
                text="Click me!",
                font=("Arial", 20, "bold"),
                command=click,  # Executes a function, in this case the "click" function
                bg="#855cd6",
                fg="white",
                activebackground="#855cd6",
                activeforeground="white",
                state=ACTIVE,
                image=follow_photo,
                compound="top")
button.pack()

window.mainloop()
