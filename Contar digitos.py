#Entrada: un número entero mayor que -1
#Salida: la cantidad de digitos del número ingresado
#Restricciones: debe ser un número entero y este debe ser mayor que -1

def contar_digitos(num):
    if isinstance(num, int) and num>-1:
        if num==0:
            return 1
        else:
            return contar_digitosaux(num)
            
    else:
        return ('Su número no cumple con las restriccioes, intente de nuevo con otro número')
        
def contar_digitosaux(num):
    if num==0:
        return 0
    else:
        return 1 + contar_digitosaux(num//10)
    
