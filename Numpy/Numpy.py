import numpy as np
import matplotlib.pyplot as plt
lista_1 = [1,2,3,4]
#Se ve igual que una lista cuando lo imprimimos, pero sin comas
#Podemos agregar elementos con append, insert, sumar, min o max, muchas cosas
np_lista = np.array(lista_1)
np_suma = np.sum(np_lista)
append = np.append(np_lista,8)
insert = np.insert(np_lista,0,0)
min = np.min(np_lista)
print(min)
#Podemos ver el tipo de elemento
np_lista.dtype
#print(np_lista.dtype)

#Creamos una lista con los valores hasta el numero que le pasemos
lista_2 = np.arange(12)
#print(lista_2)

#Podemos dividirlo en filas y columnas que sean divisoras de ese numero, se llama matrix
lista_matrix = lista_2.reshape(4,3)
#print(lista_matrix)

#Podemos crear un tensor

lista_tensor = lista_2.reshape(3,2,2)
#print(lista_tensor)

#Podemos crear un vector

lista_vector = lista_2.reshape(12,1)
#print(lista_vector)

#NP ARANGE ---> Podemos crear listas con parametros que le pasemos

lista_3 = np.arange(start=2, stop=20, step=4) #Empieza en 2, termina en 20, y me los muestra de 4 en 4
#print(lista_3)


#Tambien puedo hacer de para atras
lista_4 = np.arange(start=20, stop=2, step=-4) 
#print(lista_4)


#LINSPACE --> Puedo darle dos parametros, inicio y final y me lo divide en las partes que yo le diga, asi sean flotantes

lista_5 = np.linspace(start=12, stop=13, num=10) #Empieza en 12, termina en 13, y me lo divide en 10 partes
#print(lista_5)


#ZEROS Y ONES --> Puedo crear una lista de solo ceros o solo unos

zeros = np.zeros(6)
#print(zeros)

unos = np.ones(7)
#print(unos)

#crear una matriz con zeros o unos
matrix = np.zeros((3,4))
#print(matrix)

#Calcular el numero de pi

pi = np.pi
#print(pi)


#Hacer arreglos aleatorios entre 0 y 1
random = np.random.rand(10)#----> Me tira 10 datos aleatorios
#print(random)

random_1 = np.random.uniform(low=15,high=10,size=10)#----> Random aleatorio desde el 15 hasta el 10 y en 10 partes
#print(random_1)

#Datos aleatorios en una distribucion normal, pueden estar entre - y + infinito
randn = np.random.randn(10)
#print(randn)

#Daros normales pero con parametros

normal = np.random.normal(loc=15,scale=2,size=12)#---> Media y desviacion estandar
#print(normal)

#RANDINT ---> Me imprime numeros enteros al azar desde 12 hasta 20, y 100 veces
otro_random = np.random.randint(low=12, high=20, size=100)
#print(otro_random)

otro_random = np.random.randint(low=10, high=20, size=(10,10))#---> Matrix random de 10 x 10 de numeros del 10 al 20
#print(otro_random)
entero = np.random.randint(low=0, high=100, size=(20,10))#---> Matrix random de 20 x 10 de numeros del 0 al 100
#print(entero)


#SHAPE, me devuelve el tamaño de mi array
shape = np.shape(entero)
#print(shape)

#Convertir una lista en un una matriz o un tensor
rango = np.arange(2,10)

hola = np.reshape(rango,[2,2,2])#---> Crear tensores a partir de una lista

#print(hola)

#Para volverla a convertir en vector utilizamos FLATTEN

hey = hola.flatten()#---> La volvio a convertir en vector
#print(hey)

#Multiplicaacion de matrices

primero = np.arange(0,10)
segundo = np.arange(10,20)

lista1 = np.reshape(primero, [5,2])
lista2 = np.reshape(segundo, [2,5])

#print(lista1)
#print(lista2)

multi = np.matmul(lista1,lista2)
#print(multi)