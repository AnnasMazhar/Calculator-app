"""importing modules."""

from tkinter import *
import parser


root = Tk()

root.title("Calculator")

# get user input and place it in the field

i = 0
# creating a function for adding numbers to display

def get_variables(num):
    global i
    display.insert(i, num)
    i += 1

# clear all

def clearall():
    display.delete(0, END)

# get operator function.

def get_operation(operator):
    global i
    legnth = len(operator)
    display.insert(i, operator)
    i += legnth

# calculate

def calculate():
    strlegnth = display.get()
    try:
        a = parser.expr(strlegnth).compile()
        result = eval(a)
        clearall()
        display.insert(0, result)
    except Exception:
        clearall()
        display.insert(0, "Error")

# undo

def undo():
    strlegnth = display.get()
    if len(strlegnth):
        newstring = strlegnth[:-1]
        clearall()
        display.insert(0, newstring)
    else:
        clearall()
        display.insert(0, "error")

# adding input fields

display = Entry(root)
display.grid(row=1, columns=6, sticky=W + E)

# adding buttons

Button(root, text="1", command=lambda: get_variables(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda: get_variables(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda: get_variables(3)).grid(row=2, column=2)
Button(root, text="4", command=lambda: get_variables(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: get_variables(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: get_variables(6)).grid(row=3, column=2)
Button(root, text="7", command=lambda: get_variables(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: get_variables(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: get_variables(9)).grid(row=4, column=2)

# adding other operation buttons

Button(root, text="AC", command=lambda: clearall()).grid(row=5, column=0)
Button(root, text="0", command=lambda: get_variables(0)).grid(row=5, column=1)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=2)

Button(root, text="+", command=lambda: get_operation("+")).grid(row=2, column=3)
Button(root, text="-", command=lambda: get_operation("-")).grid(row=3, column=3)
Button(root, text="*", command=lambda: get_operation("*")).grid(row=4, column=3)
Button(root, text="/", command=lambda: get_operation("/")).grid(row=5, column=3)

# adding new operations
Button(root, text="pi", command=lambda: get_operation("*3.14")).grid(row=2, column=4)
Button(root, text="%", command=lambda: get_operation("%")).grid(row=3, column=4)
Button(root, text="(", command=lambda: get_operation("(")).grid(row=4, column=4)
Button(root, text="exp", command=lambda: get_operation("**")).grid(row=5, column=4)

Button(root, text="<-", command=lambda: undo()).grid(row=2, column=5)
Button(root, text="x!").grid(row=3, column=5)
Button(root, text=")", command=lambda: get_operation(")")).grid(row=4, column=5)
Button(root, text="^2", command=lambda: get_operation("**2")).grid(row=5, column=5)

root.mainloop()
