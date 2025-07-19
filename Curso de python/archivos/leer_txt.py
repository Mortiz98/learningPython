archivo = open("archivos\\texto_de_dalto.txt")

#Leer archivo completo ---> Si se lee una vez no se vuelve a leer, debemos cerrar el archivo
#archivo = archivo.read()
#print(archivo)

#Leer linea por linea
lineas = archivo.readlines()
#print(lineas) #Me sale el \n es la forma en que me interpreta un espacio en linea

#Leer una sola linea

linea = archivo.readline()#--> Lee una linea completa --> readline(3)--> Me lee solo 3 letras
#print(linea) 

#Cerrar el archivo
archivo.close()
