diccionario = {
    "nombre" : "Mateo",
    "esta_feliz" : True,
    "altura" : 1.73,
    "dato_duplicado" : "Mateo"
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get (si no encuentra nada el programa continua)
claves = diccionario.get("nombre")

#eliminando todo del diccionario - clear
#diccionario.clear()

#eliminando un elemento del diccionario - pop

diccionario.pop("nombre")

print(diccionario)

#iterar es recorrer el elemento, para poder acceder a cada uno de los elementos
#obteniendo un elemento dict_items iterable

diccionario_iterable= diccionario.items()
print(diccionario_iterable)