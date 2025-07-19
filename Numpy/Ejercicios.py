import numpy as np

#Todo lo que puedo hacer con una lista que tambien se hace con numpy
#¿Que operaciones podemos hacer en una lista que tambien se puede hacer en un array?
np_lista = np.array([1,2,3,4,5,6])
np_suma = np.sum(np_lista)
append = np.append(np_lista,8)
insert = np.insert(np_lista,0,0)
min = np.min(np_lista)

#print(min)

#¿Que cosas no podemos hacer en una lista que si se puede hacer con numpy?

suma = np_lista + 1         #------> Le agrega 1 a cada uno de los elementos de la lista
#print(suma)
cuadrado = np_lista **2         #-----> Eleva al cuadrado cada uno de los elementos de la lista
#print(cuadrado)



#¿Cuál es la diferencia entre un arreglo de forma -shape- (n,), (n,1) y (1,n)?
#Arreglo (n,)
array = np.array([1,2,3,4,5,6])
#print(np.shape(array))  #--> (6,)

#Arreglo (n,1)
array = np.array([[1,2,3,4,5],[6,5,4,3,2]])
#print(np.shape(array)) #--> (2, 5)

#Arreglo (1,n)
array = np.array([[1,2,3,4,64,2]])
#print(np.shape(array)) #--> (1, 6)

#Con el .T podemos ver la matriz en 6 filas y 1 columna
#print(array.T)
#Otra manera de hacerlo --->                  [[1]
#                                              [2]
#      ------>                                 [3]
#                                              [4]]
array = np.array([[1],[2],[3],[4]])
#print(np.shape(array)) #--> (4,1)


mat = np.arange(10,50,10).reshape(4,1)
#print(mat)
                                     #-----> Algunos ejemplos
nrt = np.arange(2,10).reshape(2,4)
#print(nrt)



#Escribir un arreglo con numeros del 0-9
numeros = np.arange(9)
#print(numeros)

#Escribir un arreglo de numeros equiespaciados del 0-9
numeros_2 = np.linspace(0,9,100)
#print(numeros_2)



#Escribir un arreglo con numeros del 10 al 100 y seleccionar aquellos que son divisibles por 3
arreglo = np.arange(0,101)
#print(arreglo)

mascara = arreglo%3 == 0
#print(mascara) #        -------->>>>>> Me pasa puros True o False(booleano)

divisible = arreglo[mascara]#    ----------->>>>  Es la forma de usar mascara, toma una condicion, y si se cumple me pasa todos los true
#print(divisible)





#Crear un arreglo de ceros de shape (5,10)

ceros = np.zeros((5,10),dtype=int)#---> Solo numero entero
#print(ceros,'shape:' ,np.shape(ceros))




#Reemplazar la segunda y la cuarta fila con unos
Rempl = ceros[[2,4]] = 1                              
print(ceros)#------> Se reemplazan por unos



#Reemplazando las columnas 2 y 4 por el 2
rempls = ceros[:,[2,4]] = 2                     #----------->>>>>>>>Primero filas, luego columnas al hacer slicing<<<<<<<<<<------------
print(ceros)

rempls = ceros[2:]= 2#---> Reemplaza desde la fila 2 hasta el final
print(ceros)