from tkinter import *
import functions_buttons as fb

#Funciones para los comandos de buttons
def testing():
	fb.savefile()



#Inicializamos la ventana principal
root = Tk()


Button(root, text="Click me!", command=testing).pack()



root.mainloop()