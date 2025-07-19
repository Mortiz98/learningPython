#Falto el profe y los pibes van a comenzar la clase

#Pedir el nombre de los compañeros que vinieron a clase
def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input('Escribe tu nombre: ')
        edad = input('Escribe tu edad: ')
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key= lambda x: x[1])
    asistente = compañeros[0][0]
    profesor = compañeros [-1][0]
    return f'El asistente es {asistente} y el profesor es {profesor}'

print(obtener_compañeros(3))

