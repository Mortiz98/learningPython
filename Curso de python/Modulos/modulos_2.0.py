#Importar modulos que no estan en la mksma ruta
#Usamos en sys: es un modulo de python

import sys
#print(sys.builtin_module_names) ---> Muestra los nombres de todos los modulos integrados de python
#print(sys.path) ----> Nos da la ruta de los modulos

sys.path.append('c:\\Users\\morti\\OneDrive\\Escritorio\\Curso de python\\Ejercicios-Personales')



import E as Ejercicios

print(Ejercicios.mcd(3,6))
