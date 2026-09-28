"""
    Las listas nos permiten almacenar información en un lugar,
     la cantidad que se desee: ya sean pocos elementos o millones de elementos
     Una lista es una colección de items (elementos) que tiene un orden 
     particular. Se pueden crear listas que incluyan strings, enteros, floats,
     los nombres de las personas de tu familia. etcétera, podemos almacenar ( los tipos de datos
     permitidos en Python) lo que queramos en una lista.

     Son elementos Mutables: puede modificarse el tamaño de la lista.
     Se recomiendan nombrar una variable del tipo lista en plural.
    En Python, los corchetes indican una lista, sus elementos se separan por
    comas.
    Ejemplo: 
"""
bicycles = ['trek',"cannondale", 'redline', 'specialized', ]
print(bicycles)

# ¿Cómo podemos acceder a los elementos de una lista?

"""
    Las listas son colecciones ordenadas. Se pueden acceder a un elemento
    de una lista diciéndole a Python la posición o índice del elemento
    deseado

    Para obtener el valor deseado, se debe escribir el nombre de la lista, seguido del índice 
    del elementos entre corchetes.
    """

print(bicycles[2])
print(bicycles[0], bicycles[1], bicycles[2])
print(bicycles[0].upper())

# Los índices comienzan en 0, no en 1
# Ejemplo:
print(bicycles[1]) #cannondale
print(bicycles[3]) #specialized

# Accediendo al último y penúltimo elemento de una lista 

print(bicycles[-1])
print(bicycles[-2])

message = f"My first bicycle was a {bicycles[-1].upper()}"
print(message)