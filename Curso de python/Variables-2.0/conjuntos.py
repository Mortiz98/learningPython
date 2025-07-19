#creando un conjuntos con set

conjunto = set(["dato1","dato2",])
print(conjunto)

#metiendo un conunto en otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 ={conjunto1,"dato3"}

#teoria de conjuntos
#me devuelve true o false
conjunto1 = {1,3,5,7}
conjunto2 ={1,3,7}
#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
#otra forma, funcionan igual
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto1.issuperset(conjunto2)
#otra forma, funcionan igual
resultado = conjunto1 > conjunto2

#verificar si hay akgun numero en comun
#cuando un elemento coincide es false
resultado =conjunto2.isdisjoint(conjunto1)

print(resultado)


