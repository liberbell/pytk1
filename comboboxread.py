import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python GUI')
# win.resizable(0,0)
# ttk.Label(win, text='A label').grid(column=0, row=0)

alabel = ttk.Label(win, text='A label')
alabel.grid(column=0, row=0)

def clickMe():
    action.configure(text='Hello ' + name.get())

ttk.Label(win, text='Enter a name:').grid(column=0, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
nameEntered.focus()

action = ttk.Button(win, text='Click Me!', command=clickMe)
action.grid(column=2, row=1)
# action.configure(state='disabled')
# nameEntered.focus()

ttk.Label(win, text='choose a number:').grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

win.mainloop()
