def saludar(nombre,sexo):
    nombre = nombre.lower()
    sexo = sexo.lower()
    if (sexo == "hombre"):
        adjetivo = "rey"
    elif (sexo == "mujer"):
        adjetivo = "reina"
    else: adjetivo = "amor"
    print(f'hola {nombre}, que bueno que estes aqui {adjetivo}')    
saludar("mateo", "hOMBRE")
saludar("kEYTH", "MUJEr")

#crear una funcion que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "asdfghjklqwerty"
    num_entero = str(num);
    num = int(num_entero[0]);
    c1 = num - 3
    c2 = num - 8
    c3 = num 
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}'
    return contraseña,num

password, primer_numero = crear_contraseña_random(34)
print(password, primer_numero)