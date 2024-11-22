import datetime
import time
import os


def limpiarPantalla():
	os.system("cls")


while(True):
	limpiarPantalla()
	dt=datetime.datetime.now()
	
	print("{}:{}:{}".format(dt.hour,dt.minute,dt.second))
	sl=time.sleep(1)
	
