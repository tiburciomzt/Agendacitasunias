import threading

def myfunc():
	print("Probando hilos")

task1 = threading.Thread(target=myfunc)
task1.start()