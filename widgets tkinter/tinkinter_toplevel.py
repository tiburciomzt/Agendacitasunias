from tkinter import *
import buttons_functions as bf


def test():
    ven = Toplevel(root)
    ven.geometry("200x200")
    ven.title("Configuracion")
    bf.create_user(ven)


root = Tk()
root.title('Login ')
root.geometry('400x300')
root.resizable(0,0)
root.config(bg='pink', cursor='pirate')
name = StringVar(root)
lastname = StringVar(root)
user_email = StringVar(root)

label = Label(root, text='Welcome', bg='pink', font=('Cambria',16), fg='red')
label.place(x=160, y=10)


user = Label(root, text='Usuario', bg='pink', font=('Cambria',14), fg='black')
user.place(x=170, y=50)
texto_user = Entry(root, bg='lightblue')
texto_user.place(x=140,y=83,width=125,height=20)
texto_user.config(justify='center')

password = Label(root, text='Password', bg='pink', font=('Cambria',14), fg='black')
password.place(x=165, y=110)
texto_password = Entry(root, bg='lightblue')
texto_password.place(x=140,y=143,width=125,height=20)
texto_password.config(show='*', justify='center')


login = Button(root, text='Login', font=('Cambria',9), fg='navy', state="disabled")
login.place(x=140, y=175)

create_new_user = Button(root, text='Create user', font=('Cambria',9), fg='navy', command=test)
create_new_user.place(x=195, y=175)
root.mainloop()