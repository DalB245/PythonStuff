from tkinter import *

window = Tk()  # initiate window
window.geometry("900x500")
window.title("Test GUI")

icon = PhotoImage(file="Thumb.png")
window.iconphoto(True, icon)
window.config(background="#92887c")
photo_mountain = PhotoImage(file="mountain_low-res.png")

label = Label(window, text="Hello, i like Pizza",
              font=("arial", 40, "bold"),
              fg="white",
              bg="#92887c",
              relief=SUNKEN,
              bd=10,
              padx=20,
              pady=10,
              image=photo_mountain,
              compound="bottom")

label.pack()
# label.place(x=0, y=0)

window.mainloop()  # Display Window
