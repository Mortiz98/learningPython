#Cuando tenemos que dar mas de una instruccion no es apta
#Nos sirve para acortar el codigo
#No tenemos que retornar
numeros = [1,2,3,4,5,6,7,8,9,10]
#creando una funcion lamda para multiplicar por dos
multiplicar_por_dos = lambda x: x*2
print(multiplicar_por_dos(6))
#creando una funcion comun que diga si es par o no
def num_par(numeros):
    if  (numeros%2==0):
        return True
    
#usando filter para la funcion comun  
numeros_pares = filter(num_par,numeros)
print(list(numeros_pares))    

#creando lo mismo con lamda
numeros_pares = filter(lambda numero:numero%2==0,numeros)
print(list(numeros_pares))    

