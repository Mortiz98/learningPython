import pandas as pd
#Leer un csv de forma optima
df = pd.read_csv("archivo_problemas_resueltos\\datos.csv")

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

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





