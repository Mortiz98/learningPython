#Calcular todos los numeros primos que hay hasta el numero que le pasemos
def es_primo(num):
    for i in range(2,num-1):
      if num%i == 0: return False
    return True
  
print(es_primo(10))  

def primos_hasta(num):
    primos = []
    for i in range (3, num+1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos

print(primos_hasta(200))