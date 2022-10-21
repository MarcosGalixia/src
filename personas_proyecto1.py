import csv
from collections import namedtuple
'''creamos la funcion que nos permite leer el fichero entero,saltandose la cabecera separando cada una de las columnas por el punto y coma'''
Registros=namedtuple('Registros','numero nombre apellidos gender pais fecha_nacimiento altura peso hobbies')
def leer_fichero_entero(fichero):
    '''
    Devuelve una lista de tuplas de tipo Registro a partir de los datos incluidos en el fichero
    csv dado como parámetro. El fichero debe estar codificado en formato utf-8.
     
    @param fichero: Nombre y ruta del fichero csv a leer. 
    @type fichero:srt
    @return: Una lista de tuplas de tipo Registros con todos los datos del csv
     @rtype: [ Registros(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]  
     a
    '''
    with open(fichero,encoding='utf-8') as f:
        lector=csv.reader(f, delimiter=';')
        next(lector)
        datos_personas=[]
        for numero,nombre,apellidos,gender,pais,fecha_nacimiento,altura,peso,hobbies in lector:
            tupla_datos=Registros(int(numero),nombre,apellidos,gender,pais,fecha_nacimiento,float(altura.replace(',','.')),int(peso),tuple(hobbies.split(',')))
            datos_personas.append(tupla_datos)
    return datos_personas
 
def calcular_numero_registros(datos_personas):
    numero_de_personas={numero for numero,nombre,apellidos,gender,pais,fecha_nacimiento,altura,peso,hobbies in datos_personas}
    return len(numero_de_personas)
