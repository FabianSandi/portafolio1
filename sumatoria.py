#Entrada: un número entero mayor o igual a cero
#Salida: el factorial calculado del número ingresado por el usuario 
#Restricciones: debe ser un número entero y este debe ser mayor o igual a cero

def sumatoria(num):
    if isinstance(num, int) and num>=0:
        if num==0:
            return 0
        else:
            return num + sumatoria(num-1)
    else:
        return ('Su número no cumple con las restriccioes, intente de nuevo con otro número')
