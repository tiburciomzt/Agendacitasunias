from tkinter import *
import functions_buttons as fb
import json
class NickGui(Frame):

    def __init__(self, root, *args, **kwargs):
        super().__init__(root, args, **kwargs)
        self.root = root
        self.root.title("Guardar Usuario")

        self.name = StringVar()
        self.lastname = StringVar()
        self.user = StringVar()
        self.password = StringVar()
        frame = Frame(root)
        frame.grid(row=0, column=0, padx=5, pady=5)

        label_name = Label(frame, text="Ingresa tu nombre(s)")
        label_name.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="n")

        insert_name = Entry(frame, width=30, textvariable=self.name)
        insert_name.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        label_name = Label(frame, text="Ingresa tu apellido(s)")
        label_name.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="n")

        insert_name = Entry(frame, width=30, textvariable=self.lastname)
        insert_name.grid(row=4, column=0, sticky="w", padx=5, pady=5)

        label_name = Label(frame, text="Crea tu user")
        label_name.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="n")

        insert_name = Entry(frame, width=30, textvariable=self.user)
        insert_name.grid(row=6, column=0, sticky="w", padx=5, pady=5)

        label_name = Label(frame, text="Crea tu contraseña")
        label_name.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="n")

        insert_name = Entry(frame, width=30, textvariable=self.password)
        insert_name.grid(row=8, column=0, sticky="w", padx=5, pady=5)

        boton_nick = Button(frame, text="Guardar usuario", command=self.guardar_usuario)
        boton_nick.grid(row=9, column=0, sticky="e", padx=5, pady=5)

        boton_nick = Button(frame, text="Cancelar", command=self.cancelar)
        boton_nick.grid(row=9, column=1, sticky="e", padx=5, pady=5)


    def guardar_usuario(self):
        user = {'Name':'', 'Last Name':'', 'User':'', 'Password':''}
        user['Name']=self.name.get()
        user['Last Name']=self.lastname.get()
        user['User']=self.user.get()
        user['Password']=self.password.get()
        file_name = "{}{}.json".format(user['Name'],user['Last Name'])
        with open(file_name, 'w') as f:
            json.dump(user, f)
        fb.showinfo()
        self.root.destroy()

    def cancelar(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    c = NickGui(root).place(relwidth=2, relheight=1)
    root.mainloop()