import re

texto = '''Hola maestro como estas? Mi capitan
Esta es la 2 linea mi capitan
Y esta es la 3 definitiva mi capitan'''

resultado = re.search #--> Busca
resultado = re.findall("Hola",texto)#--> Me devuelve las veces que esta esa palabra
resultado = re.findall("Hola",texto,flags=re.IGNORECASE)#--> Ignora las mayusculas y me pasa todo lo que encuentra

#\d -> Busca digitos numericos del 0-9
resultado = re.findall(r'\d',texto)

#\D -> Busca TODO menos digitos numericos del 0-9
resultado = re.findall(r'\D',texto)

#\w -> Busca caracteres alfanumericos [a-z,A-Z,0-9,_]
resultado = re.findall(r'\w',texto)

#\W-> Busca TODO menos alfanumericos
resultado = re.findall(r'\W',texto)


#\s -> Busca espacios en blanco, espacios,tabs,saltos en linea
resultado = re.findall(r'\s',texto)

#\S -> Busca TODO menos espacios en blanco, espacios,tabs,saltos en linea
resultado = re.findall(r'\S',texto)

#. -> Busca TODO menos saltos en linea
resultado = re.findall(r'\.',texto)

#\n -> Busca saltos en linea
resultado = re.findall(r'\n',texto)

#\ -> Cancelan caracteres especiales, cancelando la funcion del punto y buscando puntos

resultado = re.findall(r'\.',texto)

#armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(r'\d\.\s',texto)

#^--> Busca el comienzo de una linea
#flags=re.M activa la multilinea
resultado = re.findall(r'^Hola',texto)

#$--> Busca el final de una linea
#flags=re.M activa la multilinea
resultado = re.findall(r'capitan$',texto)

#n --> Busca n cantodad de veces el valor de la izquierda
resultado = re.findall(r'\d{3}',texto)

#{n,m} --> Al menos n, como maximo m
resultado = re.findall(r'\d{2,4}',texto)

# | -> Busca una cosa o la otra
resultado = re.findall(r'\d{3}|Hola',texto)












print(resultado)