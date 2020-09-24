#Entrada: un número entero mayor a -1
#Salida: respuesta booleana; 'true' si el número es par, y 'false' si el número es impar
#Restricciones: debe ser un número entero y este debe ser mayor a -1

def par(num):
    if isinstance (num, int) and num>-1:
        if num%2==0:
            return True
        else:
            return False
    else:
        return ('Su número no cumple con las restriccioes, intente de nuevo con otro número')
