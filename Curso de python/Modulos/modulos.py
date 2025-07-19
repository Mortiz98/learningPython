import modulo_saludar

saludar = modulo_saludar.saludar("mateo")


#variable = asdfghjk
#asdfghjk as variable                            Esto es casi lo mismo pero al reves
#Nos ayuda para cambiar el nombre del modulo
#Ejemplo:
import modulo_saludar as m_saludar

saludar = m_saludar.saludar("mateo")
print(saludar)

#Si queremos importar solo una funcion del modulo hacemos lo siguiente:
from modulo_saludar import saludar # Aqui tambien podemos utilizar el as
saludar = saludar("keyth")
print(saludar)
#para ver las propiedades y metodos del namespace
print(dir(m_saludar))
#Accedemos al nombre de este modulo
print(__name__)
#Accedemos al nombre del modulo llamado
#print(m_saludar,__name__)

#Acceder a un modulo dentro de una carpeta
#from modulos.modulo_saludar import saludar
