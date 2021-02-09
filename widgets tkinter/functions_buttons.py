from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

#diferentes popups(ventanas emergentes) para interactuar con el usuario

def showinfo():

	MessageBox.showinfo("Usuario creado con éxito!", "Nuevo usuario creado")

def showwarning():

	MessageBox.showwarning("Alerta", "Necesita permisos del administrador")

def showerror():
	MessageBox.showerror("Error", "An error has ocurred!")

def askquestion(root):			#Devuelve una cadena de caracteres
	answer = MessageBox.askquestion("Salir","¿Está seguro que quiere sair sin guardar?")
	#Se necesita guardar en una variable ya que regresa una cadena de texto yes/no
	if answer=='yes':
		root.destroy()

def askokcancel(root):
	answer = MessageBox.askokcancel("Salir","¿Sobreescribir el fichero actual?")	
	#Se necesita guardar en una variable ya que regresa TRUE/FALSE
	if answer:
		root.destroy()

def askquestionyesno(root):		#igual que askquestion pero devuelve un boleano
	answer = MessageBox.askyesno ("Salir","¿Está seguro que quiere sair sin guardar?")
	#Se necesita guardar en una variable ya que regresa una cadena de texto yes/no
	if answer:
		root.destroy()

def askretrycancel():		#Devuelve un boleano
	answer = MessageBox.askretrycancel("Reintentar", "No se puede conectar")
	if answer:
		root.destroy()


def colorchooser():		#devuelve una tupla con dos valores (colorRGB, colorHEXADECIMAL)
	color_saved = ColorChooser.askcolor(title="Elige un color")
	print(color_saved)		

def openfile():	#devuelve el path hacia el fichero
	path_file = FileDialog.askopenfilename(title="Abrir un fichero", initialdir=r"C:", 
		filetypes=(("Fichero de texto","*.txt"), 
			("Fichero de texto avanzado","*.txt2"), 
			("Todos los ficheros", "*.*")))

def savefile():		#Equivale a open(ruta, 'w')
	path_file = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
	if path_file is not None:
		path_file.write("Hola!")
		path_file.close()