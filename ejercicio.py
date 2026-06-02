nombres=[]

for i in range(3):
    
    while True:
        nombre=input(f"ingrese un nombre {i+1}: ")
        if len(nombre) >= 3:
            nombres.append(nombre)
            break         
        else:
            print("El nombre tiene que tener mas de 3 letras")
            
longitud_maxima = max(len(nombre) for nombre in nombres)

ganadores = [nombre for nombre in nombres if len(nombre) == longitud_maxima]

for nombre in ganadores:
    print(f"Ganador: {nombre}")


    

#print(f"longotud_max {longitud_maxima}")
#nombre_mayor= max(nombres, key=len)
#print(f"el nombre mayor es :{nombre_mayor} y tiene {len(nombre_mayor)} caracteres")

