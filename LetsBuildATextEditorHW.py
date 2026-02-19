from tkinter import *
def calculate():
    p = float(e1.get())
    r = float(e2.get())
    t = float(e3.get())
    si = (p * r * t) / 100
    amount = p * ((1 + r / 100) ** t)
    ci = amount - p
    res_si.config(text="SI: " + str(round(si, 2)))
    res_ci.config(text="CI: " + str(round(ci, 2)))
root = Tk()
root.title("Interest App")
root.geometry(('400x400'))
Label(root, text="Principal:").grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)
Label(root, text="Rate (%):").grid(row=1, column=0)
e2 = Entry(root)
e2.grid(row=1, column=1)

Label(root, text="Time (years):").grid(row=2, column=0)
e3 = Entry(root)
e3.grid(row=2, column=1)
btn = Button(root, text="Calculate", command=calculate)
btn.grid(row=3, column=0, columnspan=2)
res_si = Label(root, text="")
res_si.grid(row=4, column=0, columnspan=2)

res_ci = Label(root, text="")
res_ci.grid(row=5, column=0, columnspan=2)

root.mainloop()