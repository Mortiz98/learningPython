import re
#le pedimos al usuario que nos diga una frase, o varias
frase = input ("decime una frase y te calculo cuanto tardarias en decirla:  ")
frase_limpia = re.sub(r'[^\w\s]', '', frase)

#creamos una lista con todas las palabras de la frase (se separan cada vez que hay un espacio en blanco)
palabras_separadas = frase_limpia.split( )

#Usamos len()para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)

#Calculamos cuanto tardaria en decir las palabras y se lo decimos
print(f'dijiste {cantidad_de_palabras} palabras, tardarias {cantidad_de_palabras / 2} segundos en decirlo')
print(f'Dalto lo diria en {cantidad_de_palabras /  1.3} segundos')

#En caso de que tarde mas de un minuto en decirlas le decimos que pare un poco
if cantidad_de_palabras > 100:
 print("para, tampoco te pedi un testamento")
 
 