from tkinter import *
window = Tk()

window.geometry("400x150+10+20")
window.title("Text Field")

txtfld = Entry(window,text = "This is where i type my text", bd = 5)
txtfld.place(x=100,y=100)
window.mainloop()


