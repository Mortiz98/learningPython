with open('archivos\\texto_de_dalto.txt','a') as archivo:
    #agregando el archivo
    archivo.write('\n')
    for i in range(5):
        archivo.write(f'linea {i+1} agregada \n')
        