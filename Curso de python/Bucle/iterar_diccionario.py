diccionario = {
    "nombre": "mateo",
    "apellido": "ortiz",
    "edad": 25,
    "nombre" : "keyth",
    "apellido" : "vergara",
    "edad": 19
    
}
#obteniendo la clave
for key in diccionario:
    print(key)
    
  #recorriendo diccionario para obtener clave y valor  
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es {key} y el valor es {value}")
    