import tkinter as tk

win = tk.Tk()

strData = tk.StringVar()

strData.set('Hello StringVar')

varData = strData.get()

intData = tk.IntVar()
# print(varData)
print(intData)

print(tk.IntVar())
print(tk.DoubleVar())
print(tk.BooleanVar())
