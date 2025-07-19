 #dir nos permite ver todos los atributos que podemos ejecutar
 #es una funcion
 
 
cadena1 = "Hola soy mateo"
cadena2 = "Bienvenido"
 
resultado = dir(cadena1)
#print(resultado)

#los metodos se ejecutan, cadena1.djsjks

#upper - Covierte Todo en mayusculas
mayusc = cadena1.upper()

#lower - Convierte a minusculas
minusc = cadena1.lower()

#capitalize - Covierte la primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#find - Buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("o")

#index - Buscamos una cadena en otra cadena
busqueda_index = cadena1.index("a")

#isnumeric - Si es numerico devuelve true, sino devuelve false
es_numerico = cadena1.isnumeric()

#isalpha - Si es alfanumerico nso devuelve true, sino false
es_alfanumerico = cadena1.isalpha()

#contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("m")

#len - contamos cuantos caracteres tiene una cadena
#es una funcion

contar_caracteres = len(cadena1)

#starwith - verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empiez_con = cadena1.startswith("h")

#endwith - verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termin_con = cadena1.endswith("h")

#replace - reemplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace("la" , "lu")
 
#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")



print(cadena1[:cadena1.find(' ')] +" soy keyth")








