#Duracion de cursos
#este curso: 1.5
#minimo: 2.5
#promedio: 4
#maximo: 7
#Crudo este curso: 3.5
#crudo promedio: 5

#a)diferencia en porcentaje entre el curso actual y
#-el mas rapido, el maslento, el promedio

#b)porcentaje de crudo que se reduce en: el promedio, este curso

#c)ver 10 horas de este curso a cuantas horas equivale?


#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5
crudo_dalto = 3.5
crudo_promedio = 5


#diferencia de duracion
diferencia_con_min = int(100 - dalto_curso / otros_cursos_min * 100)
diferencia_con_max = int(100 - dalto_curso / otros_cursos_max *100) 
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

print(f'el curso de dalto dura un {diferencia_con_min}% menos que el mas rapido')
print(f'el curso de dalto dura un {diferencia_con_max}% menos que el mas lento')
print(f'el curso de dalto dura un {diferencia_con_promedio}% menos que el promedio')

print("-----------------------")

#diferencia de crudo
crudo_reduccion_dalto = round(100 - dalto_curso/ crudo_dalto * 100,1)
crudo_reduccion_promedio = 100 -otros_cursos_promedio/crudo_promedio * 100
print(f'El tiempo de reduccion de video en un curso de dalto es de {crudo_reduccion_dalto}%')
print(f'El tiempo de reduccion de video en un curso promedio es de {crudo_reduccion_promedio}%')
print("-----------------------")

print(f'ver 10 horas de este curso equivale a ver {round(otros_cursos_promedio / dalto_curso *100 / 10,2) } horas de otros curos')

print(f'ver 10 horas de este curso equivale a ver {dalto_curso *100 / otros_cursos_promedio / 10 } horas de otros curos')

