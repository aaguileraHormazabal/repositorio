nombres=[]

for i in range(3):
    
    while True:
        nombre=input(f"ingrese un nombre {i+1}: ")
        if len(nombre) >= 3:
            nombres.append(nombre)
            break         
        else:
            print("El nombre tiene que tener mas de 3 letras")
            

nombre_mayor= max(nombres, key=len)

print(f"el nombre mayor es :{nombre_mayor} y tiene {len(nombre_mayor)} caracteres")

