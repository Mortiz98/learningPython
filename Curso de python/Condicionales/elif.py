ingreso_mensual = 81000
gasto_mensual = 77000

#if anidados y else if (elif)
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estas bien")
    else:
        print("no te alcanza")          
 
 #elif se usa para dar mas opciones, si la primera no se cumple sigue con la otra
 #podemos usarlo las veces que queramos
  
if ingreso_mensual > 90000:
    print("estas bien economicamente en cualquier parte de tu pais")
if ingreso_mensual > 85000:
    print("estas bien economicamente en cualquier parte de departamento")
else: print("No tienes suficiente para tu departamento")
if ingreso_mensual > 500:
    print("estas bien economicamente en cualquier parte de marinilla")    
    
else:
    print("eres pobre")
    print("hola")   
    
    
            
    