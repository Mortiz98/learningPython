animales = ["gato","perro","loro","cocodrilo"]
numeros = [23,34,65,78]
familia = ["karen","jairo","mateo","diva"]

for i in familia:
    print(i)

#recorriendo listas animalesn
for i in animales:
    print(f'Ahora la variable animal es igual a:{i}')
#recorriendo la lista numeros y multiplicandolos por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
    #iterar dos listas al mismo tiempo
    #tener los mismos elementos ambas listas
for numero, animal in zip(numeros,animales):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
  #recorrer una lista obteniendo su indice  
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es {indice} y el valor es {valor}  ")
    
    for numero in numeros:
        print(f"ejecutando el ultimo bucle, valor actual {numero}")
    else:
        print(f"el blucle termino")
    #Funciona exactamente igual para tuplas, y conjuntos
    
    