cars = [ 'kia', 'nissan','ford', ]
print(cars)
print(cars[0],cars[1], cars[2])
for cars in cars:
    print(cars)
    
# Identación

"""
    Python utiliza la identación para determinar
    cuando una línea de código está conectada a la línea 
    de código anterior.

    Basicamente, se utiliza 4 espacios en blano para obligarnos 
    a escribir código ordenado y estructurado.
"""

# Error de lógica - logig Error - IdentationError
cars = ['ford', 'nissan', 'MG']

for car in cars:
    print(cars)
    print(f"Marcas de autos, {car}")