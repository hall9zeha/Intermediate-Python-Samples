 
#import saludos #importando todos los métodos o funciones del módulo

#from saludos import saludar #solo importamos un método en específico
import sys 

sys.path.insert(1,"..")#agregamos la dirección actual que es un directoria aparte a la lista de busquedas de python para
#que ejecute nuetro módulo, un puto para nuestra ubicación actual y otro punto para la ubicación anterior
from saludos import * #importará todas las funciones del módulo para usarlas como si fueran estáticas

#saludos.saludar()

saludar()

saludos()