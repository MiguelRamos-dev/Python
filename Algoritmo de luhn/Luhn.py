"""El algoritmo de lum es una suma de
verificacionn simple utilizada para validar numeros de tarjetas de 
credito, numeros IMEI entre otros"""

# Tarjetas de credito:
tarjetas = [1234567890123456, 2020202067678902, 5556661122334487,4517660095838932, 2920287677378900, 2987654321109923]

#funcion validar
def algoritmo(numero_tarjeta):
    digits = [int(caracter) for caracter in str(numero_tarjeta)]
    
    for i in range(len(digits)-2, -1, -2):
        digits[i]*=2
        if digits[i] > 9:
            digits[i] -=9
        
    suma_total = suma_total = sum(digits)
    
    return suma_total % 10 == 0

# validar cada numero de tarjeta de la lista

for tarjeta in tarjetas:
    if algoritmo(tarjeta):
        print(f"la tarjeta {tarjeta} es valida.")
    else:
        print(f"la tarjeta {tarjeta} es invalida.")