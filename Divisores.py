#Entrada: un número entero mayor o igual a cero
#Salida: los divisores del número agregado o un mensaje de error
#Restricciones: el número debe ser entero y al mismo tiempo debe ser mayor o igual a cero

def divisores(num):
    if isinstance(num, int) and num>=0:
        if num==0:
            return ('El cero no se puede dividir')
        else:
            return divaux(num, num)
    else:
        return ('Su número no cumple con las restriccioes, intente de nuevo con otro número')
        
def divaux(num, divisor):
    if divisor==0:
        return 0
    else:
        if num%divisor==0:
            print(divisor)
            return divaux(num, divisor-1)
        else:
            return divaux(num, divisor-1)
