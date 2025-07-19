#numeros_ganadores =[]
#for i in range(5): 
 #   n_ganador = int(input("Cuales son los numeros ganadores? "))
  #  numeros_ganadores.append(n_ganador)


#numeros_ganadores.sort()

#print(f'los numeros ganadores fueron{numeros_ganadores}')
#------------------------------------------------------------------------------------------- 
#numeros = [1,2,3,4,5,6,7,8,9,10]
#numeros.reverse()

#print(numeros)
#------------------------------------------------------------------------------------------- 
#asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
#pendientes = []
#for i in asignaturas:
 #   nota = int(input(f"Que nota has sacado en {i}? "))
  #  if nota < 3: pendientes.append(i)
#for i in asignaturas:
 #   asignaturas.remove(i)  
        
#print(f'tienes que repetir {pendientes}')
#------------------------------------------------------------------------------------------- 

#def fibonacci(num):
 #   a,b = 0,1
    #fibonacci_lista = [0]
    #for i in range(num):
   #     if b > num: return fibonacci_lista
  #      else:
 #           a,b = b,a+b
#            fibonacci_lista.append(b)
#fibonacci_lista = fibonacci(50)
#print(fibonacci_lista)
#------------------------------------------------------------------------------------------- 
#def num_primo(num):
    #for i in range(2, num-1):
     #   if num%i==0: return False
    #return True
#print(num_primo(6))

#numeros_primos = []   
#def primos_hasta(num):
   # for i in range(3,num+1):
    #   resultado = num_primo(i)
     #  if resultado==True: numeros_primos.append(i)
    #return numeros_primos
    
#print(primos_hasta(50))
#------------------------------------------------------------------------------------------- 
#palabra = input(f'Escriba una palabra ')
#palindromo = palabra
#palabra = list(palabra)
#palindromo = list(palindromo)
#palabra.reverse()
#if palabra == palindromo:
 #   print(True)
#else:
 #   print(False)       
 #------------------------------------------------------------------------------------------- 
#palabra = input("ingrese una palabra ")
#palabra_list = palabra
#palabra_list = list(palabra) 
#vocales = ["a","e","i","o","u"]
#num_de_vocales = []
#for i in palabra:
 #   if i in vocales:
  #      num_de_vocales.append(i)
#numero = len(num_de_vocales)

#print(f'el numero de vocales que hay en la palabra es {numero}')

#for vocal in vocales:
 #   veces = 0
  #  for i in palabra:
   #     if i==vocal:
    #       veces +=1 
    #print(f'la vocal {vocal} aparece {veces} veces')
    
 #------------------------------------------------------------------------------------------- 
#precios = [50, 75, 46, 22, 80, 65, 8]
#precio_mas_alto = max(precios)
#precios_mas_bajo = min(precios) 

#print(f'El precio mas alto es {precio_mas_alto}$, y el precio mas bajo es {precios_mas_bajo}$')
#------------------------------------------------------------------------------------------- 
#def factorial(num):
 #   n = 1
   # for i in range(num):
  #     n *= i+1
 #   return n
#factorial = factorial(4)
#print(factorial)

#------------------------------------------------------------------------------------------- 
#def total_factura(sin_iva, iva):
  #  total = float(round(sin_iva + sin_iva / 100 * iva ,1))
 #   return total
#print(total_factura(40043,19))
#------------------------------------------------------------------------------------------- 
#def media(lista):
 #   return sum(lista) / len(lista)
#
#print(media([1,2,3,4,5,6,7,8,9]))
#------------------------------------------------------------------------------------------- 
def cuadrados(lista):
    lista_1 = []
    for i in lista:
        cuadr = i **2 
        lista_1.append(cuadr)
    return lista_1
    


def elimina(lista):
  lista_nueva = []
  lista.pop(0)
  lista.pop(-1)
  lista_nueva.append(lista)
  return lista_nueva

