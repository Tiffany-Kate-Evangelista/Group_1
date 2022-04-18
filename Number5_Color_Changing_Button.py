from tkinter import *
window=Tk()
def change():
    label['bg']='yellow'

button = Button(text='<---Click to change the color of the button', command=change)
button.place(x=120, y=150)

label=Label(text='First number', fg='red', bg='blue')
label.place(x=22, y=153)

window.title('Hello Python')
window.geometry("400x200+10+10")
window.mainloop()