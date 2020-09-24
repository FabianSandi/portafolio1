#Entrada: un número entero mayor a -1
#Salida: respuesta booleana; 'true' si el número es impar, y 'false' si el número es par
#Restricciones: debe ser un número entero y este debe ser mayor a -1

def impar(num):
    if isinstance (num, int) and num>-1:
        if num%2==1:
            return True
        else:
            return False
    else:
        return ('Su número no cumple con las restriccioes, intente de nuevo con otro número')
