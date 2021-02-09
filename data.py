import json

filename = 'user.json'

datos = []

try:

	with open(filename) as file:
		user = json.load(file)

except FileNotFoundError:
		 name = datos.append(input('What is your name?'))
		 with open(filename, 'w') as file:
		 	json.dump(name, file)
else:
		 	print('name = '+name)



class User():
	

	def __init__(self, datos):
		self.datos = datos

	def get_datos(self):
		return self.datos


datos = [{'name':''}, 
{'last name':''}
, {'email':''}
, {'password':''}]

c = User(datos)
print(c.get_datos())