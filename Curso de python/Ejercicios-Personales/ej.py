#palabras = ["mateo","keyth","karen","andres"]
#def letra(palabras):
#    count = 0
#    letra_a_buscar = input("Que letra deseas buscar? ")
#    for i in palabras:
#        if i.startswith(letra_a_buscar):
#            count += 1
#    return count
#print(letra(palabras))
#----------------------------------------------------------------------------------------------
a = "cancion"
b = "oracion"
def rima(a,b):
    if a.endswith(b[-3:]):
       return "Estas palabras riman"
    else:
        return "No riman"
print(rima(a,b))




    

    