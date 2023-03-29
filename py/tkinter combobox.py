import tkinter as tk
from tkinter.ttk import Combobox

form = tk.Tk()
form.title('ComboBox')
form.geometry("300x500")

def generate_values():
    values = []
    for i in range(100):
        values.append(str(i))
    return values

text_var = tk.StringVar()

combobox = Combobox(form, height=3, textvariable=text_var, values=generate_values())
combobox.pack()

def yazdır():
    print(text_var.get())

button = tk.Button(form, text='Yazdır', command=yazdır)
button.pack()

form.mainloop()