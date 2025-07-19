with open('archivos\\texto_de_dalto.txt','w') as archivo:
    #Sobreescrimos el archivo
    #archivo.write("jajaj te la recontajugue")
    
    #Afregando dos lineas con writelines
    archivo.writelines(["-Hola maestro como andas \n","-bien y tu? \n"])
    
    #Agregando otras dos lineas
    archivo.writelines(["-Me alegra mucho \n","-gracias"])