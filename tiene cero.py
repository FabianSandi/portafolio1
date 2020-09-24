#Entrada: un número entero mayor que -1
#Salida: respuesta booleana; 'true' si un dígito del número ingresado es un cero, y 'false' si ningún dígito del número es un cero
#Restricciones: debe ser un número entero y este debe ser mayor que -1

def tienecero(num):
    if isinstance(num, int) and num>-1:
        if num<10 and num>0:
            return False 
        elif num==0:
            return True
        elif num>9:
            return tieneceroaux(num)
    else:
        return ('Su número no cumple con las restriccioes, intente de nuevo con otro número')
def tieneceroaux(num):
    if num==0:
        return False
    else:
        if (num%10)==0:
            return True
        else:
            return tieneceroaux(num//10)
