frutas = ["banana","manzana","ciruela","pera","naranja","granadilla","durazno"]
cadena = "Hola mateo"
numeros = [2,4,3,6]
#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta =="granadilla":
        continue
    print(f"me voy a comer una {fruta}")
    
    #evitar que el buble siga ejecutandose
    
for fruta in frutas:
    if fruta =="granadilla":
        break
    print(f"me voy a comer una {fruta}")    
    
#recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo
numeros_duplicados = [i *2 for i in numeros]
print(numeros_duplicados)

        