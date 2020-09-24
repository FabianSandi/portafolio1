#Entrada: un número entero mayor o igual a cero
#Salida: la multiplicación de los dígitos pares incluidos en un número
#Restricciones: el número ingresado debe ser un número entero y este debe ser mayor o igual a cero
def multiplicatoriapares(num):
    if isinstance(num, int) and num>=0:
        if num==0:
            return 0
        else:
            return multiaux(num)
    else:
        return('Su número no cumple con las restriccioes, intente de nuevo con otro número')
def multiaux(num):
    if num==0:
        return 1
    if (num%10)%2==0:
        return (num%10)*multiaux(num//10)
    else:
        return multiaux(num//10)
