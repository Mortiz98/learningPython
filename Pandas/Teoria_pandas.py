import pandas as pd
import numpy as np

asignaturas = ['matematicas','historia','economia','progrmacion','ingles']

#Creamos una serie, es una tabla de una sola dimension, un solo tipo de dato.
serie_1 = pd.Series(asignaturas)
#print(serie_1)

#Creamos una serie apartir de una lista creada con arange
numeros = np.arange(10,100,10)
serie = pd.Series(numeros)
#print(serie)

#Lo mismo con un diccionario, las materia funcionan como indices.
diccionario = {'matematica': 6.0, 'economia': 4.5, 'programacion': 8.5}
serie_2 = pd.Series(diccionario)
#print(serie_2)

#Atributos
serie_3 = pd.Series([1,2,3,4,4,5,5,5,6,6,6])
#print(serie_3.size)#Me da el tamaño de la serie, parecido a len
(serie_3.index)#Me da el (start=0, stop=9, step=1)
(serie_3.count())#Me cuenta los elementos que tiene
(serie_3.sum())#Me suma los elementos
(serie_3.cumsum())#Me hace la suma acumulativa
(serie_3.describe())#Me hace una descripcion estadistica y de ahi puedo ver cada uno.
(serie_3.value_counts())#Me dice cuantos de cada uno hay
(serie_3.index)
(serie_3.sort_values())#Me ordena los valores solamente.(ascending=false)de mayor a menor
#(serie_3.apply())#Dentro puedo aplicarle una funcion que haga lo que yo quiera.
#Acceder a cada elemento
#serie[3:]


#Juntando np y pandas
numeros_1 = pd.Series(np.arange(1,10,2))
#print(numeros_1)

#-------------------------------------------------------------------------------------------------------------


#---------------------------------DataFrames-------------------------------------------

datos = {
    'nombre':['maria','luis','carmen','antonio'],
    'edad':[18,22,20,21],
    'grado':['economia','medicina','arquitectura','economia'],
    'correo':['maria@gmail.com','luis@yahoo.com','carmen@gmail.com','antonio@hotmail.com']
}


df = pd.DataFrame(datos,index=[1,2,3,4])
print(df)

print(df['nombre'])


#Otra forma de crear un dataframe

lista = [['mateo',25],['keyth',18]]
df = pd.DataFrame(lista, columns=['nombre','edad'], index=['fila1','fila2'])#---> Con columns y index asigno el valor de las columnas y el indice
print(df)

#Para leer un archivo que esta en otra carpeta de la pc
df = pd.read_csv("C:\\Users\\morti\\OneDrive\\Escritorio\\Ingenieria de datos\\Curso de python\\archivos\\datos.csv")
print(df)

#accediendo a las primeras 3 filas, de arriba a abajo
primeras_filas = df.head(2)
#print(primeras_filas)

#accediendo a las ultimas filas, de abajo a arriba
ultimas_filas = df.tail(2)
#print(ultimas_filas)

#accediendo a la cantidad de filas y columnas con shape, lo primero es filas y lo segundo columnas
filas_y_columnas_totales = df.shape

filas,columnas = df.shape
#print(columnas)
#print(filas)

#obteniendo data estadistica del dataframe:
db_info = df.describe()

#accediendo a un elemento especifico del df con el loc, edad de la fila 2
#loc se utiliza para seleccionar filas y columnas por sus etiquetas o nombres en el DataFrame.
elemento_especifico_loc = df.loc[1,"edad"]
#print(elemento_especifico_loc)

#accediendo a la edad con iloc
#iloc se utiliza para seleccionar filas y columnas por su posición numérica en el DataFrame.
elemento_especifico_iloc = df.iloc[2,2]
#print(elemento_especifico_iloc)

#accediendo a todas las filas de una columna

fila_2= df.iloc[2,:]
print(fila_2)

#accediendo a toda una columna               La sintaxis general es: df.iloc[filas, columnas].

columna = df.iloc[:,0]
#print(columna)

#accediendo a filas > a 30
mayor_que_30 = df.loc[df["edad"]>30,:]
#print(mayor_que_30)

#ordenando el dataframe por la edad
df_ordenado = df.sort_values("edad")
#print(df_ordenado)

#ordenandolo de forma descendente
df_orden_descendente = df.sort_values("edad",ascending=False)
#print(df_orden_descendente)

#mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df['edad'][0]))

#reemplazando los datos de dalto por "maestro"
df["apellido"].replace("dalto","maestro",inplace=True)
#print(df["apellido"])    

#eliminando las filas con datos vacios
df = df.dropna() #si queremos eliminar columnas(axis:1)

#eliminando las filas repetidas
df = df.drop_duplicates()

#creando un df con el df limpio
df.to_csv("archivo_problemas_resueltos\\datos_limpios.csv")


