from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser

def choosecolor():
	new_bg_color = ColorChooser.askcolor(title="Elige un color")
	return new_bg_color


def create_user(ven):

	def saveuser():
		ans = showdict.set([{'Nombre(s)':name.get()}, {'Apellido(s)':lastname.get()}, {'User':user_email.get()}])	
		MessageBox.showinfo("Guardado con éxito!", "Usuario creado")
		return ans
		

	def cancel_user():
		root.destroy()
		
	def clear_data():
		name.set(" ")
		lastname.set(" ")
		user_email.set(" ")

	root = ven
	

	label = Label(root, text="Ingresa tu(s) nombre(s)").pack()
	entry = Entry(root, justify="center", textvariable=name).pack()		#first number
	label2 = Label(root, text="Ingresa tu(s) apellido(s)").pack()
	entry2 = Entry(root, justify="center", textvariable=lastname).pack()		#second number

	label3 = Label(root, text="Nombre de usuario o email").pack()
	entry3 = Entry(root, justify="center", textvariable=user_email).pack()		#third number
	labe3 = Label(root, text=" ").pack()

	entry3 = Entry(root, justify="center", textvariable=showdict).pack()		#third number

	save_user = Button(root,text="Crear Usuario"
		, command=saveuser).pack(side= "top")				#command >>agrega un comportamiento al botton.

	cancel= Button(root,text="Cancelar"
		, command=cancel_user).pack(side= "top")




def calculadora(ven):

	def hello_world():
		print("Hello World ...")

	def crear_label():
		label = Label(root, text="label creada").pack()

	def sumar():
		ans = res.set(n1.get() + n2.get())				#El metodo SET ES PARA DAR VALOR AL ENTRY para el stringvar
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

	root = ven
	root.config(bd=20)

	n1 = DoubleVar()
	n2 = DoubleVar()
	res = DoubleVar()

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