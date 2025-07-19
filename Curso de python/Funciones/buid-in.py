#Encontrando el numero mayor de una lista

numeros = [2,43,5,23,45,76]
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrando el numero menor en una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#retorna false --> 0, vacio , false, none /  retrona True--> distinto a 0, True, datos no vacio
Resultado_bool= bool(0)
print(Resultado_bool)

#retorna true si toso los valores son verdaderos, todos

Resultado_all = all((13,46,0))
print(Resultado_all)

#Suma todo lo que esta adentro de una lista o iterable, si o si deben ser numeros.
suma_total = sum(numeros)
print(suma_total)
#Si fueran numeros en una cadena = '1223765432'
suma = sum(int(i) for i in numeros) 
print(suma)