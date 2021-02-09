from tkinter import *
import json
from tkinter.filedialog import asksaveasfile

test = 1
def writeToJSONFile(path, fileName, data):
        json.dump(data, path)
 
path = './'
 
 
def check():
    a = Name.get()
    b = test * int(Age.get())
    c = Role.get()
    data = {}
    data['Name'] = a
    data['Age'] = b
    data['Role'] = c
    files = [('JSON File', '*.json'),]
    fileName='{}{}'.format(a,b)
    filepos = asksaveasfile(filetypes = files,defaultextension = json,initialfile='IOTEDU')
    writeToJSONFile(filepos, fileName, data)
 
window = Tk()
window.geometry('640x300')
window.title('IoT4Begineers')
 
name = Label(window, text="Name:")
Name = Entry(window)
age = Label(window, text="Age:")
Age = Entry(window)
role = Label(window, text="Role:")
Role = Entry(window)
submit = Button(window,text='Submit',command = check).grid(row=3, column=1)
 
 
name.grid(row=0, column=0)
age.grid(row=1,column=0)
role.grid(row=2,column=0)
Name.grid(row=0, column=1)
Age.grid(row=1, column=1)
Role.grid(row=2, column=1)
 
 
mainloop()