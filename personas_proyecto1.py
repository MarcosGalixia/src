import csv

#creamos la funcion que nos permite leer el fichero entero,saltandose la cabecera separando cada una de las columnas por el punto y coma


def leer_fichero_entero(fichero):
    with open(fichero,encoding='utf-8') as f:
        lector=csv.reader(f, delimiter=';')
        next(lector)
        datos_personas=[]
        for datos in lector:
            numero=int(datos[0])
            nombre=datos[1]
            apellidos=datos[2]
            gender=datos[3]
            pais=datos[4]
            fecha_nacimiento=datos[5]
            altura=float(datos[6].replace(',','.'))
            peso=int(datos[7])
            hobbies=(tuple(datos[8].split(',')))
            tupla_datos=(numero,nombre,apellidos,gender,pais,fecha_nacimiento,altura,peso,hobbies)
            datos_personas.append(tupla_datos)
    return datos_personas
 
def calcular_numero_registros(datos_personas):
    numero_de_personas={numero for numero,nombre,apellidos,gender,pais,fecha_nacimiento,altura,peso,hobbies in datos_personas}
    return len(numero_de_personas)
