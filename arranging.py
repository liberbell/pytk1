import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Create instance
win = tk.Tk()

# Add a title
win.title("Python GUI")

# Disable resizing the GUI
#win.resizable(0,0)

# Modify adding a Label
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

# Modified Button Click Function
def clickMe():
    action.configure(text='Hello ' + name.get() + ' '+ numberChosen.get())

# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)
#action.configure(state='disabled')    # Disable the Button Widget

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text='Disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text='Unchecked', variable=chVarUn)
check2.select()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text='Enabled', variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# COLOR1 = 'Blue'
# COLOR2 = 'Gold'
# COLOR3 = 'Red'
#
# def radCall():
#     radSel = radVar.get()
#     if radSel == 1:
#         win.configure(background=COLOR1)
#     elif radSel == 2:
#         win.configure(background=COLOR2)
#     elif radSel == 3:
#         win.configure(background=COLOR3)
colors = ['Blue', 'Gold', 'Red']

def radCall():
    radSel = radVar.get()
    if radSel == 0:
        win.configure(background=colors[0])
    elif radSel == 1:
        win.configure(background=colors[1])
    elif radSel == 2:
        win.configure(background=colors[2])

radVar = tk.IntVar()
radVar.set(99)

for col in range(3):
    curRed = 'rad' + str(col)
    curRed = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRed.grid(column=col, row=6, sticky=tk.W, columnspan=3)

# rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
# rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)
#
# rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
# rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)
#
# rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
# rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)
#
# scrolW = 30
# scrolH = 3
# scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
# scr.grid(column=0, columnspan=3)
labelIsFrame = ttk.LabelFrame(win, text=' Labels in a Flame ')
labelIsFrame.grid(column=0, row=7)

ttk.Label(labelIsFrame, text='Label1').grid(column=0, row=0, sticky=tk.W)
ttk.Label(labelIsFrame, text='Label2').grid(column=1, row=0, sticky=tk.W)
ttk.Label(labelIsFrame, text='Label3').grid(column=2, row=0, sticky=tk.W)

nameEntered.focus()      # Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()
