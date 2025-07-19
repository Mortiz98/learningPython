#Nos sirve para agrupar datos, tenemos listas, tuplas,conjunto, diccionario
#Las listas las podemos modificar cuando queramos
lista = ["mateo","ortiz",True, 1.73]
lista[3] = "Keyth"
print(lista[3])
print(lista[0])
print(lista)

#En tupla usamos parentesis
#Tupla no la podemos modificar nunca
tupla = ("mateo","ortiz",True, 1.73)
print(tupla[2])

#creando un conjunto (set)
#no tienen un orden fijo, pueden intercambiar de lugar
#Puedo modificar el conjunto entero pero no un elemento como en las listas
#No puedo repetir valores
#No podemos acceder a cada uno de los elemento
# ej: print(conjunto[2]), no funciona
#El conjunto nos sirve para eliminar datos duplicados, no almacena datos duplicados
conjunto = {"mateo","ortiz",True, 1.73}


#creando un diccionario (dict)
#Se separa hacia abajo, es con llaves
#Se separan con coma siempre
#Cuando le pedimos que nos de la funcion print no le damos un numero sino el nombre de los que queremos

diccionario = {
    "nombre" : "Mateo",
    "esta_feliz" : True,
    "altura" : 1.73,
    "dato_duplicado" : "Mateo"
}
print(diccionario["nombre"])
