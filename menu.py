from tkinter import *
from tkinter import messagebox as MessageBox
import json
from settings import *


class Menu():

	def __init__(self):
		self.root = Tk()
		self.root.title('Login ')
		self.root.geometry('400x300')
		self.root.resizable(0,0)
		self.root.config(bg='pink', cursor='pirate')

		self.name = StringVar(self.root)
		self.lastname = StringVar(self.root)
		self.user_email = StringVar(self.root)
		self.password = StringVar(self.root)
		self.usuario = StringVar(self.root)
		self.contra = StringVar(self.root)

		label = Label(self.root, text='Welcome', bg='pink', font=('Cambria',16), fg='red')
		label.place(x=160, y=10)


		user = Label(self.root, text='Usuario', bg='pink', font=('Cambria',14), fg='black')
		user.place(x=170, y=50)
		texto_user = Entry(self.root, bg='lightblue', textvariable=self.usuario)
		texto_user.place(x=140,y=83,width=125,height=20)
		texto_user.config(justify='center')

		password = Label(self.root, text='Password', bg='pink', font=('Cambria',14), fg='black')
		password.place(x=165, y=110)
		texto_password = Entry(self.root, bg='lightblue', textvariable=self.contra)
		texto_password.place(x=140,y=143,width=125,height=20)
		texto_password.config(show='*', justify='center')


		login = Button(self.root, text='Login', font=('Cambria',9), fg='navy', command=self.login)
		login.place(x=140, y=175)

		create_new_user = Button(self.root, text='Create user', font=('Cambria',9), fg='navy',command=self.create_user)
		create_new_user.place(x=195, y=175)

		quit= Button(self.root,text="QUIT", command=self.quit)
		quit.place(x=165, y=230)
		
		self.root.mainloop()

	def create_user(self):

		def cancel():
			create_user.destroy()

		def saveuser():
			ans = {'Nombre':self.name.get(), 'Apellidos':self.lastname.get(), 'user/email':self.user_email.get(), 'password':self.password.get()}
			file_name = "{}.json".format(ans['user/email'])
			with open(file_name, 'w') as f:
				json.dump(ans, f)
			clear_data()
			MessageBox.showinfo("Guardado con éxito!", "Nuevo Usuario Creado")
			create_user.destroy()
		
		def clear_data():
			self.name.set(" ")
			self.lastname.set(" ")
			self.user_email.set(" ")
			self.password.set(" ")


		create_user = Toplevel(master=self.root)
		create_user.geometry("400x400")
		create_user.title("Creando usuario")
		label = Label(create_user, text="Ingresa tu(s) nombre(s)").pack()
		entry = Entry(create_user, justify="center", textvariable=self.name).pack()		#first number
		label2 = Label(create_user, text="Ingresa tu(s) apellido(s)").pack()
		entry2 = Entry(create_user, justify="center", textvariable=self.lastname).pack()		#second number

		label3 = Label(create_user, text="Nombre de usuario o email").pack()
		entry3 = Entry(create_user, justify="center", textvariable=self.user_email).pack()		#third number
		labe3 = Label(create_user, text=" ").pack()

		password_label= Label(create_user, text="Contraseña").pack()
		entry4 = Entry(create_user, justify="center", textvariable=self.password).pack()		#third number

		save_user = Button(create_user,text="Crear Usuario", command=saveuser).pack(side= "top")				#command >>agrega un comportamiento al botton.

		cancel= Button(create_user,text="Cancelar", command=cancel).pack(side= "top")


	def login(self):

		def quit():
			create_user.destroy()

		def clear_datos():
			self.usuario.set(" ")
			self.contra.set(" ")

		obtener_usuario = self.usuario.get()
		obtener_contra = self.contra.get()
		
		filename = '{}.json'.format(obtener_usuario)

		with open(filename) as f:
				data = json.load(f)
		
		if obtener_usuario == data['user/email'] and obtener_contra ==data['password']:
			clear_datos()
			create_user = Toplevel(master=self.root)
			create_user.geometry("720x600")
			create_user.title("Bienvenido {}".format(data['Nombre']))
			create_user.resizable(0,0)
			create_user.config(bg="#53CDB8", cursor='pirate')

			inbox_frame = Frame(create_user, bg= "#53CDB8")
			inbox_frame.pack()

			button_frame = Frame(create_user, bg="#F26262")
			button_frame.pack()
			
			name_label = Label(inbox_frame, text='Name', bg="#FFBB20", font=("Comic Sans MS", "11", "normal")).pack()
			name_entry = Entry(inbox_frame, font=("Comic Sans MS", "11", "normal"), width=28).pack()

			phone_label = Label(inbox_frame, text='Phone', bg="#FFBB20", font=("Comic Sans MS", "11", "normal")).pack()
			phone_entry = Entry(inbox_frame, font=("Comic Sans MS", "11", "normal"), width=28).pack()

			email_label = Label(inbox_frame, text='Email', bg="#FFBB20", font=("Comic Sans MS", "11", "normal")).pack()
			email_entry = Entry(inbox_frame, font=("Comic Sans MS", "11", "normal"), width=28).pack()

			fecha_label = Label(inbox_frame, text='Fecha (DD/MM/YY)))', bg="#FFBB20", font=("Comic Sans MS", "11", "normal")).pack()
			fecha_entry = Entry(inbox_frame, font=("Comic Sans MS", "11", "normal"), width=28).pack()

			quit= Button(button_frame,text="Quit", command=quit).pack(side= "bottom")

		elif obtener_usuario == data['user/email'] and obtener_contra !=data['password']:
			MessageBox.showerror("Contraseña incorrecta", "Su contraseña es incorrecta")
		elif obtener_usuario == ' ' and obtener_contra == " ":
			MessageBox.showwarning("Campos vacios", "Favor de ingresar datos")


	def quit(self):
		self.root.destroy()