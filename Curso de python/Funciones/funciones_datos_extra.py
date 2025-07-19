#Funcion de 3 parametros
def frase(nombre,apellido,adjetivo):
    return f'Hola {nombre}, {apellido}, sos un {adjetivo}'
#Parametros posicionales
frase_resultante = frase("Mateo","Ortiz","Capo")
print(frase_resultante)

#Puedo cambiar de orden los parametros de la siguiente manera, funiona igual
def frase(nombre,apellido,adjetivo):
    return f'Hola {nombre} {apellido}, sos un {adjetivo}'

frase_resultante = frase(adjetivo="Capo",apellido="Ortiz",nombre ="Mateo")
print(frase_resultante)