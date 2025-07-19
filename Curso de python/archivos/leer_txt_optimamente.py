#Abriendo el archivo con with open
with open("archivos\\texto_de_dalto.txt") as archivo:
    
    #leemos el archivo
    contenido = (archivo.read())
    
    #mostramos el archivo
    print(contenido)
    
#No es necesario cerrarlo al usar with open
    
    