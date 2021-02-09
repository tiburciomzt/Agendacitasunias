import time


class Fecha():

	def __init__(self):
		self.time24 = time.strftime("%H:%M:%S")		#Formato 24 hrs.
		self.time12 = time.strftime("%I:%M:%S")		#Formato 12 hrs.


date = Fecha()
print(date.time12)