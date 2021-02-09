from tkinter import *


def createuser():
    createuser = Toplevel(master=root)
    createuser.geometry("200x200")
    Label(createuser, text="Ingrese un valor: ").pack()
    Entry(createuser, textvariable=name).pack()


root = Tk()
root.geometry("200x200")

name = StringVar(root)

Button(root,text='Abrir secundaria', command=createuser).pack()
ans = Label(root, textvariable=name)

print(ans)

root.mainloop()