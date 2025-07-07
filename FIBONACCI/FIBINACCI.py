"""/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */"""
 
 
"""fibonacci = [0,1]    # iniciamos la lista con los dos numeros iniciales

while len(fibonacci)< 50:    # mientras la longitud de la lista no supere los 50 siguee
    siguiente = fibonacci[-1] + fibonacci[-2]  # para crear el siguiente hacemos la suma de los dos anteriores, por eso creamos los dos primeros numeros de la lista. 
    fibonacci.append(siguiente) # vamos agregando los numeros generados a la lista

print(fibonacci) 
"""

#otra forma de hacerlo

def fibo(valor):
    val1=0
    val2=1
    
    for i in range(val1, valor):
        print(val1)
        valor_fibo = val1 + val2
        val1 =  val2
        val2 = valor_fibo
        

fibo(50)