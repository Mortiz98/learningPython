import pandas as pd
#usando la funcion read_csv para leer el archivo CSV

#dataframe--> df--> estructuras de datos similares a una hoja de calculo
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv") #-->  (,names=["name","lastname","age"])->Darle otro nombre
#print(df)

#obteniendo los dato de la columna nombre
nombres = df["nombre"]
#print(nombres)

#ordenando el dataframe por la edad
df_ordenado = df.sort_values("edad")
#print(df_ordenado)

#ordenandolo de forma descendente
df_orden_descendente = df.sort_values("edad",ascending=False)
#print(df_orden_descendente)

#concatenando dos dataframe
df_concatenado = pd.concat([df,df2])
#print(df_concatenado)

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
elemento_especifico_loc = df.loc[1,"edad"]
#print(elemento_especifico_loc)

#accediendo a la edad con iloc
elemento_especifico_iloc = df.iloc[2,2]
#print(elemento_especifico_iloc)

#accediendo a todas las filas de una columna

fila_2= df.iloc[2,:]
print(fila_2)

#accediendo a toda una columna

columna = df.iloc[:,0]
#print(columna)

#accediendo a filas > a 30
mayor_que_30 = df.loc[df["edad"]>30,:]
#print(mayor_que_30)









   












