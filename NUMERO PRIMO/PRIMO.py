""" Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 """

"""from sympy import isprime  # resolucion usando la libreria de Sympy 
def primo(num):    # funcion para saber si es primo
     if isprime(num):
         return True
     else:
         return False


def primos(rango): # funcion para determinar cuales son primos de un rango dado
    for i in range(rango):
        if primo(i):
            print(f"El numero: {i} es primo")
        else:
            print(f"El numero: {i} no es primo")
            
primos(20)
"""
from sympy import isprime 

def num_primos(numeros):      # funcion mas reducida usando isprime dentro del for
    for i in range(numeros):
        if isprime(i):
            print(f"El numero {i} es primo")
        else:
            print(f"El numero {i} no es primo")
            
num_primos(20)