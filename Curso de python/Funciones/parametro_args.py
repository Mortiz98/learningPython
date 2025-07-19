#utilizando parametro args, sirve para poder meter en una lista lo que queramos de forma infinita
def suma(nombre,*numeros):
    return f'Tu nombre es {nombre}, y tu suma es {sum(numeros)}'
resultaod = suma( "Mateo",3,5,3,6,8,55)
print(resultaod)

#De esta forma podemos seguir agregando parametros
def suma_total(numeros):
    return sum([*numeros])
resultaod = suma_total([3,5,3,6,8,55])
print(resultaod)