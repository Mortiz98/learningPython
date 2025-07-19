#Escribe un programa que reciba una nota entre 0 y 100.
#Si la nota es mayor o igual a 60, imprime "Aprobado", de lo contrario, imprime "Reprobado".

nota= int(input("Digita la nota de tu curso: "))

if  0 <= nota <= 100:
    if nota >= 60:
        print("Aprobaste la materia")
    else:
         print("Reprobaste")
else:
    print("opcion invalida")