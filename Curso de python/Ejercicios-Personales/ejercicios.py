Saludo = "Hola Mundo"

print(Saludo)

#Nombre = input("cual es tu nombre? " )
#print(f"mi nombre es {Nombre} ")
#-------------------------------------------------------------------------------------------
#Operacion = ((3+2) / (2*5)) **2
#print(Operacion)
#-------------------------------------------------------------------------------------------
#num_horas_trabajadas= int(input ("cual es el numero de horas trabajadas? "))
#coste_hora = int (input ("que cuesta cada hora? "))
#pago = num_horas_trabajadas * coste_hora
#print(f'Tu pago es de {pago}')
#-------------------------------------------------------------------------------------------
#n= int(input("dame un numero entero al azar "))

#suma = int((n*(n+1)/2))
#print(f'la suma de los primeros numeros desde 1 hasta {n} es igual a {suma}')
#-------------------------------------------------------------------------------------------
#peso = float(input("cual es tu peso? "))
#estatura = float(input("cual es tu estatura?" ))
#imc = round(peso / estatura **2,2)
#print (f'tu indice de masa corporal es igual a {imc}')
#-------------------------------------------------------------------------------------------
#m = int(input("dame un numero al azar "))
#n = int(input("dame otro numero "))
#c =int(n / m)
#r = int(n % m)
#print(f'el cociente es {c} y el resto es {r}')
#-------------------------------------------------------------------------------------------
#cant_invertir = int(input("que cantidad desea invertir? "))
#interes_anual = float(0.60)
#num_años = int(input("introduzca el numero de años que desea invertir "))

#capital_obtenido = int(cant_invertir * interes_anual * num_años )

#print(f'el capital obtenido en {num_años} años es de {capital_obtenido}')
#-------------------------------------------------------------------------------------------
#peso_payaso = int(input("Peso del payaso: "))
#peso_muñeca = int(input("Peso de muñeca: "))
#payasos_vendidos = int(input("Cuantos payasos se vendieron?: "))
#muñecas_vendidos = int(input("Cuantas muñecas se vendieron?: "))
#peso_paquete =int((peso_payaso*payasos_vendidos)+(peso_muñeca*muñecas_vendidos))
#num_paquetes = int(peso_paquete / 50)
#if peso_paquete > 5000:
 #   print(f'Es demasiado pesado, conseguir dos camiones')
#else:
 #   print("Va bien, llevar en un camion")
#print(f'El peso total enviado fue de {peso_paquete}kg y {num_paquetes} paquetes')
#-------------------------------------------------------------------------------------------
#cant_ivertir = float(input("cantidad a invertir: "))
#int_anual = 0.04
#primer_año = float(cant_ivertir * int_anual)
#seg_año = float((primer_año + cant_ivertir)* int_anual)
#ter_año = float((seg_año + cant_ivertir) * int_anual)

#print(f'La cantidad de dinero obtenida en el primer año fue de {primer_año}, el segundo año de {seg_año}, y el tercer año de {ter_año}')
#-------------------------------------------------------------------------------------------
#barra_pan = 3.49
#descuento = 0.60
#vendidas = int(input("Numero de barras vendidas: "))

#print(f'el precios por una barra de pan fresca es {barra_pan}$')
#print(f'el descuento es de {descuento * 100}%')
#print(f'el coste normal seria de {round(vendidas * barra_pan,2)}')
#print(f'el coste total es de {vendidas * barra_pan * descuento}$')
#-------------------------------------------------------------------------------------------
#email = input("Introduce tu correo electrónico: ")
#print(email[:email.find('o')] + '@ceu.es')
#-------------------------------------------------------------------------------------------
#def mayor_de_edad(edad):
  #  if edad >= 18:
   #     return("Eres mayor de edad")
    #else:
     #   return("Eres menor de edad")
#print(mayor_de_edad(15))    
#-------------------------------------------------------------------------------------------
#def contraseña(contra):
 #   contraseña_almacenada = "mateoykeyth"
  #  if contra == contraseña_almacenada:
   #     print("Podes pasar")
    #else:
     #   print("contraseña incorrecta")
    #return

#contraseña("mateoykeyth")
#-------------------------------------------------------------------------------------------

#def num_par(lista):
 #   numeros_pares = []
  #  for i in lista:
   #    if  (i%2==0):
    #       numeros_pares.append(i)
    #return numeros_pares
       
#lista1 =[1,2,3,45,54,56,76,89,78,64]  
#print(num_par(lista1))

#print(max(num_par(lista1)))
#-------------------------------------------------------------------------------------------
#def suma(lista):
 #   result = 0
  #  for i in lista:
   #     result = result + i
    #return result
#print(suma([1,2,3,5,4,5,6,7,3,4,56,65,4,]))
#-------------------------------------------------------------------------------------------
#def multiplica(numeros):
 #   result = 1
  #  for i in numeros:
   #     result = i * result
    #return result

#print(multiplica([1,2,3,]))
#-------------------------------------------------------------------------------------------
#def max_de_dos(a,b):
 #   if a > b:
  #      return a
   # elif b > a:
    # return b
#    else:
 #       return "Son iguales"
#print(max_de_dos(55,58))
#-------------------------------------------------------------------------------------------
#def max_de_tres(a,b,c):
 #   d = max_de_dos(a,b)
  #  final = max_de_dos(c,d)
   # return final
#
#print(max_de_tres(8,2,5))
 #------------------------------------------------------------------------------------------- 
#def es_vocal(letra):
    #vocales = ("a","e","i","o","u") 
   # if letra in vocales:
  #      return "Es una vocal"
 #   else: return "No es una vocal"
#print(es_vocal("a"))
 #-------------------------------------------------------------------------------------------   
#def es_vocal(lista):
 #   vocales = ("a","e","i","o","u") 
  #  vocal = []
   # for i in lista:
    #    if i in vocales:
     #      vocal. append(i)
   #     else: None
    #return vocal
#lista1 = ("a","e","t","o","u","r","w","h") 
#print(es_vocal(lista1))
#------------------------------------------------------------------------------------------- 

#asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
#puntajes =[]
#for i in asignaturas:
 #   Puntaje =int(input(f'Que nota has sacado en {i}? '))
  #  puntajes.append(Puntaje)
#for i in range(len(asignaturas)):
 #   print(f'en {asignaturas[i]},he sacado {puntajes[i]}')
import numpy as np
import matplotlib.pyplot as plt

# Definir los vectores
u = np.array([3, -4])
v = np.array([6, -3])
w = np.array([-14, -3])

# Crear el gráfico
plt.figure()

# Graficar los vectores
plt.quiver(0, 0, u[0], u[1], angles='xy', scale_units='xy', scale=1, color='r', label='u')
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='g', label='v')
plt.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='b', label='w')

# Etiquetas de ejes
plt.xlabel('X')
plt.ylabel('Y')

# Límites de ejes
plt.xlim(-15, 15)
plt.ylim(-15, 15)

# Cuadrícula
plt.grid(True)

# Leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
