#Tkinter module
from tkinter import *

window = Tk()

window.title("Calculator")
window.geometry("340x230")

#Function written for the click of button
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

#Function for the Operators
def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0, END)

def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0, END)

def mul():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, END)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0, END)

#the equal operation
def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, i + int(n2))
    elif math == "subtraction":
        e.insert(0, i - int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))
    elif math == "division":
        e.insert(0, i / int(n2))

#clear function
def clear():
    e.delete(0, END)

e = Entry(window, width=52, borderwidth=5)
e.place(x = 10, y= 0)

b = Button(window, text="Esc", width = 10, activeforeground = "red", activebackground = "grey")
b.place(x = 10, y = 60)
b = Button(window, text="Clear", width = 10, activeforeground = "red", activebackground = "grey", command = clear)
b.place(x = 90, y = 60)
b = Button(window, text="+", width = 10, activeforeground = "black", activebackground = "yellow", command = add)
b.place(x = 170, y = 60)
b = Button(window, text="-", width = 10, activeforeground = "black", activebackground = "yellow", command = sub)
b.place(x = 250, y = 60)

b = Button(window, text="1", width = 10, activeforeground = "black", activebackground = "lightblue", command = lambda:click(1))
b.place(x = 10, y = 90)
b = Button(window, text="2", width = 10,activeforeground = "black", activebackground = "lightblue", command = lambda:click(2))
b.place(x = 90, y = 90)
b = Button(window, text="3", width = 10, activeforeground = "black", activebackground = "lightblue", command = lambda:click(3))
b.place(x = 170, y = 90)
b = Button(window, text="*", width = 10, activeforeground = "black", activebackground = "yellow", command = mul)
b.place(x = 250, y = 90)

b = Button(window, text="4", width = 10, activeforeground = "black", activebackground = "lightblue", command = lambda:click(4))
b.place(x = 10, y = 120)
b = Button(window, text="5", width = 10, activeforeground = "black", activebackground = "lightblue", command = lambda:click(5))
b.place(x = 90, y = 120)
b = Button(window, text="6", width = 10, activeforeground = "black", activebackground = "lightblue", command = lambda:click(6))
b.place(x = 170, y = 120)
b = Button(window, text="/", width = 10, activeforeground = "black", activebackground = "yellow", command = div)
b.place(x = 250, y = 120)

b = Button(window, text="7", width = 10, activeforeground = "black", activebackground = "lightblue", command = lambda:click(7))
b.place(x = 10, y = 150)
b = Button(window, text="8", width = 10, activeforeground = "black", activebackground = "lightblue", command = lambda:click(8))
b.place(x = 90, y = 150)
b = Button(window, text="9", width = 10, activeforeground = "black", activebackground = "lightblue", command = lambda:click(9))
b.place(x = 170, y = 150)
b = Button(window, text="=", width = 10, height = 3, activeforeground = "black", activebackground = "lightgreen", command = equal)
b.place(x = 250, y = 150)
b = Button(window, text="0", width = 33, activeforeground = "black", activebackground = "lightblue", command = lambda:click(0))
b.place(x = 10, y = 180)

mainloop()