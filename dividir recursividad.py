#Entrada: 'm' y 'n'n donde ambos son números enteros mayores o iguales a cero
#Salida: la división del número n(dividendo) entre el número m(divisor)
#Restricciones: m y n deben ser enteros y deben ser iguales o mayores a cero
def dividirRecur(m,n):
    if isinstance(m, int) and isinstance(n, int) and m>=0 and n>=0:
        if n==m:
            return 1
        elif m==0:
            return ('Ningún número puede ser dividido entre 0, intente con otro divisor')
        elif n==0:
            return ('Cero no puede ser dividido')
        elif n==0 and m==0:
            return ('Cero no puede ser dividido y ningún número puede ser dividido entre cero')
        else:
            return 1 + dividirRecur(m,n-m)
    else:
        return ('Su número no cumple con las restriccioes, intente de nuevo con otro número')
