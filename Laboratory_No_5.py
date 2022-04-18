from tkinter import *
window = Tk()

#Number 1. Label
window.geometry("400x230+10+20")
window.title("Label")

label = Label(window, text="Laboratory Activity 5")
label.place(x=303, y=30)
label = Label(window, text="Submitted to: Mam Sayo")
label.place(x=293, y=50)

#Number 2. Text Label
window.geometry("400x150+10+20")
window.title("Text Field")

txtfld = Entry(window,text = "This is where i type my text", bd = 5)
txtfld.place(x=293, y=90)

#Number 3. Father of Computer
window.geometry("400x130+10+20")
window.title("Father of Computer")

label = Label(window, text = "Charles Babbage", font = ("Verdana", 20), fg = "black", bg = "cyan")
label.place(x=240, y=135)

#Number 4. Major Subjects
window.geometry("400x150+10+20")
window.title("Major Subjects")

data = "reading", "writing", "arithmetic", "coding"
lb = Listbox(window, height=5, selectmode="single")
for num in data:
    lb.insert(END, num)
lb.place(x=290, y=190)

#Number 5. Color Changing Button
def change():
    label['bg']='yellow'

button = Button(text='<--- Click to change the color of the button', command=change)
button.place(x=413, y=287)

label=Label(text='First number', fg='red', bg='blue')
label.place(x=313, y=290)

window.title('Hello Python')
window.geometry("800x400+10+20")

window.mainloop()