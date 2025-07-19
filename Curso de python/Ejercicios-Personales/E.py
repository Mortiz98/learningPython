#ordenar lista sin usar sorted

#def orden(lista):
#    change = True
#    while change:
#        change = False
#        for i in range(len(lista)-1):
#            
#            if lista[i] > lista[i+1]:
#                
#                temp = lista[i]
#                lista[i] = lista[i+1]
#                lista[i+1] = temp
#                change = True
#    return lista
            
            
#orden = orden([9,8,7,6,5,4,3,2,1])
#print(orden)
#-------------------------------------------------------------------------------------------------
#def multiplicacion(a,b):
#    resultado = 0
#    for i in range(a):
#         resultado += b
#    return resultado
#print(multiplicacion(5,8))
#-------------------------------------------------------------------------------------------------
#texto = 'sd4s56d6fgfd67df7gf6d7fg6f7d7fgf5d6ssdf655dfdf6d5fgfd56g7fd4g4fd33dx5'
#def extraer_numeros(texto):
#    numeros = ''
#    for i in texto:
#        if i.isdigit():
#            numeros += i
#    return numeros

#def orden(numeros):
#    orden = sorted(numeros)
#    numeros_ordenados = ''.join(orden)
#    return numeros_ordenados


#def suma(numeros):
#   resultado = sum(int(i)for i in numeros)
#   return resultado

#numeros= extraer_numeros(texto)
#orden = orden(numeros)
#suma = suma(numeros)
#print(suma)
#print(numeros)
#-------------------------------------------------------------------------------------------------
#texto = "Bienvenidos a SyS cursos"
#def desordenar(texto):
#    texto = texto [::-1]
#    return texto
#desordenar = desordenar(texto)
#print(desordenar)
#-------------------------------------------------------------------------------------------------
#def maximo(lista):
#    Mayor = 0
#    for i in lista:
#        if i > Mayor:
#            Mayor = i
#    return Mayor
#        
#print(maximo([1,2,3,43,2,45,4]))
#-------------------------------------------------------------------------------------------------
#diccionario = {}
#for i in range(3):
#    nombre = input("Ingrese su nombre: ")
#    nacimiento = int(input("Ingrese su año de nacimiento "))        
#    diccionario[nombre] = nacimiento
#print (diccionario)
#-------------------------------------------------------------------------------------------------
#lista = ["mateo","karen","keyth","cloe","dala","falckor"]
#def mas_larga(lista):
#    mas_larga = ""
#    for i in lista:
#        if len(i)  >  len(mas_larga):
#            mas_larga = i
#    return mas_larga
#print(mas_larga(lista))
#-------------------------------------------------------------------------------------------------
#numeros = [1,2,3,4,6,4,644,676,32,645,677]
#def mayor(numeros):
#    mayor = 0
#    for i in numeros:
#        if i > mayor:
#            mayor = i
#    return mayor

#print(mayor(numeros))        
#-------------------------------------------------------------------------------------------------
#def filtrar_palabras(lista,num):
#    palabras = []
#    for i in lista:
#        if len(i) > num:
#            palabras.append(i)
#    return palabras
#lista = ["mateo","cocodrilo","avestruz","perro"]
#print(filtrar_palabras(lista,8))
#-------------------------------------------------------------------------------------------------
#def n_mayusculas(palabra):
#    cont = 0
#    for i in palabra:
#        if i ==  i.upper() :
#            cont += 1
#    return cont        
#print(n_mayusculas("MatEoAwSdfsAeERAasdA"))
            
#Otra opcion

#def n_mayusculas(palabra):
#    mayusculas = palabra.upper()
#    mayus = []
 #   for i in palabra:
 #       if i in mayusculas:
  #          mayus.append(i)
  #  numero = len(mayus)
 #   return numero

#print(n_mayusculas("MatEoAwSdfsAeERAasdA"))
#-------------------------------------------------------------------------------------------------            

def binario(decimal):
    numero_binario = []
    while decimal > 0:
      resultado = decimal % 2
      decimal = decimal // 2
      numero_binario.insert(0,str(resultado))
      binario_str = ''.join(numero_binario)
    return binario_str

print(binario(110))
#------------------------------------------------------------------------------------------------         
#format nos permite sacar el numero binario de una, me devuelve un string

#------------------------------------------------------------------------------------------------      
def decimales(binario):
    bin = str(binario)
    elev = len(bin)-1
    numeros = []
    for i in bin:
        resultado = int(i) * 2 ** elev
        numeros.append(resultado)
        elev -= 1
        suma = int(sum(numeros))
    return suma
    
print(decimales(1101110))

def decimal(numero_decimal):
    digitos = 10
    resultado = '0,'
    while numero_decimal > 0 and digitos > 0:
        numero_decimal = numero_decimal * 2
        entero = int(numero_decimal)
        decimal = numero_decimal % 1
        resultado += str(entero)
        numero_decimal = decimal
        digitos -= 1
    return resultado

print(decimal(0.23))


        
        









#-------------------------------------------------------------------------------------------------
#edades = (20,23,16,31,26,19)
#def edad(edades):
#    cont = 0
#    for i in edades:
#        if i >= 20:
#         cont += 1
#         
#    return cont

#print(edad(edades))
#-------------------------------------------------------------------------------------------------
#def mcd(m,n):
 #   while n:
  #      m,n = n, m%n
   # return m


    
        
    
        
   
    
   












