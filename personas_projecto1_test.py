import csv
from personas_proyecto1 import *

def test_leer_fichero(fichero):
    print("Leemos los tres primeros registros:")
    print(leer_fichero_entero(fichero)[:3])
    print("Leemos los tres ultimos registros:")
    print(leer_fichero_entero(fichero)[-3:])

def test_calcular_numero_registros(fichero):
    numero_registros=calcular_numero_registros(leer_fichero_entero(fichero))
    print("Calculamos el numero total de registros: "+str(numero_registros))
    
test_leer_fichero('data\personas.csv')
test_calcular_numero_registros('data\personas.csv')

