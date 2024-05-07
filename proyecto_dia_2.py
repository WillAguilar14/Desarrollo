
print('cual es tu nombre?')
Nombre=input()
print('cual es tu apellido?')
Apellido=input()
print('cuanto vendiste este mes?')
ganancias=input()
comisiones = round((int(ganancias)*0.13),2)
print(f'Hola {Nombre} {Apellido}, tu comisiones fueron de {comisiones}')