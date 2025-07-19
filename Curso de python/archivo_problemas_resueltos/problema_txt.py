# 2 listas, una con nombres otra con apellidos
nombres = ["lucas","Matias","Camila","pedro","roberto"]
apellidos = ["dalto","zing","dalto","robetix","tarado"]

with open("archivo_problemas_resueltos\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f'Nombre: {n}\nApellido: {a}\n-------------\n') for n,a in zip(nombres,apellidos)]
    
    
    
import pandas as pd
df = pd.read_csv("archivo_problemas_resueltos\\datos.csv")
print(df[nombres]) 