#list - crea una lista

lista = list(["hola", "mateo" , 23,45,32])

#len - devuelve cantidad de elementos de la lista
cantidad_de_elem = len(lista)

#agregando un elemnto a la lista - append
lista.append("keyth")


##agregando un elemnto a la lista en un orden especifico - insert
lista.insert(2, "cloe")

#agregando varios elemoentos a la lista - extend, debe ser dentro de corchetes
lista.extend([False, True])

#elimianr un elemebto de la lista - pop
lista.pop(0)

#eliminando un elemento de la lista por su valor
lista.remove("mateo")

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista (si usamos el parametro reverse=true lo ordena en reversa) Sin textos
#lista.sort()

#invirtiendo los elementos de la lista
#lista.reverse()

#verificando si un elemento se encuentra e la lista
buscando_eleme = lista.index(45)
print(buscando_eleme)






print(lista)



