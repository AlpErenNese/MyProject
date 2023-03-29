import tkinter as tk


form = tk.Tk()

form.title('SpinBox')
form.geometry('500x500')
form.config(background= 'pink')


x2 = tk.Variable()
spin2 = tk.Spinbox(form, from_= 10, to= 20, textvariable=x2).pack()

def veriAl():
    print(x2.get())

button = tk.Button(form, text= "Veri Al", command=veriAl).pack()




form.mainloop()