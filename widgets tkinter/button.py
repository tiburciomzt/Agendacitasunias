from tkinter import *

def hello_world():
	print("Hello World ...")

def crear_label():
	label = Label(root, text="label creada").pack()

def sumar():
	ans = res.set(float(n1.get()) + float(n2.get()))				#El metodo SET ES PARA DAR VALOR AL ENTRY para el stringvar
	borrar_numbers()
	return ans										#El metodo GET obtiene el valor dado enel entry

def restar():
	ans = res.set(float(n1.get()) - float(n2.get()))				#El metodo SET ES PARA DAR VALOR AL ENTRY para el stringvar
	borrar_numbers()
	return ans

def multiplicar():
	ans = res.set(float(n1.get()) * float(n2.get()))				#El metodo SET ES PARA DAR VALOR AL ENTRY para el stringvar
	borrar_numbers()
	return ans

def dividir():
	ans = res.set(float(n1.get()) / float(n2.get()))				#El metodo SET ES PARA DAR VALOR AL ENTRY para el stringvar
	borrar_numbers()
	return ans


def borrar_numbers():
	n1.set(" ")
	n2.set(" ")

root = Tk()
root.config(bd=20)

n1 = StringVar()
n2 = StringVar()
res = StringVar()

label = Label(root, text="First number").pack()
entry = Entry(root, justify="center", textvariable=n1).pack()		#first number
label2 = Label(root, text="Second number").pack()
entry2 = Entry(root, justify="center", textvariable=n2).pack()		#second number

label3 = Label(root, text="Answer").pack()
entry3 = Entry(root, justify="center", textvariable=res, state="disabled").pack()		#third number
labe3 = Label(root, text=" ").pack()

button = Button(root,text="Sumar"
	, command=sumar).pack(side= "left")				#command >>agrega un comportamiento al botton.

button_restar = Button(root,text="Restar"
	, command=restar).pack(side= "left")
button_multiplicar = Button(root,text="Multiplicar"
	, command=multiplicar).pack(side= "left")
button_dividir = Button(root,text="Dividir"
	, command=dividir).pack(side= "left")




root.mainloop()