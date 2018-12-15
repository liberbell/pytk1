import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python GUI')
# win.resizable(0,0)
# ttk.Label(win, text='A label').grid(column=0, row=0)

alabel = ttk.Label(win, text='A label')
alabel.grid(column=0, row=0)

def clickMe():
    action.configure(text='** I have been clicked! **')
    alabel.configure(foreground='red')
    alabel.configure(text='A Red Label')

action = ttk.Button(win, text='Click Me!', command=clickMe)
action.grid(column=1, row=0)

win.mainloop()
