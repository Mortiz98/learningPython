#creando una funcion que suma numeros
def sumar():
    #iniciando un bucle
    while True:
        #convirtiendo a enteros numeros y sumarlos
        try: 
            numero_1 = int(input("Escribe un numero: "))
            numero_2 = int(input("Escribe un numero: "))
        
            resultado = numero_1 + numero_2
            #si lanzo una excepcion pedirle que reingrese los datos
        except:
            print("Es necesario ingresar un numero, intenta nuevamente")
            #si todo salio bien terminamos el bucle
        else:
            break
    return resultado
#mostrando el resultado
print(sumar())
    