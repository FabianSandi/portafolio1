#Entrada: un número 'n' y un número 'm'
#Salida: la múltiplicación entre el número "n" por el número "m"
#Restricciones: tanto 'n' como 'm' deben ser números entero mayores o iguales a cero

def multiplicaciónrecursivo(n,m):
    if isinstance(n, int) and isinstance(m,int) and m>=0 and n>=0:
        return MultiRecurAux(n,m)
    else:
        return ('Su número no cumple con las restriccioes, intente de nuevo con otro número')

def MultiRecurAux(n,m):
    if m==0:
        return 0
    elif m==1:
        return n
    elif n==1:
        return m
    elif n==1 and m==1:
        return 1
    else:
        return n + MultiRecurAux(n,m-1)
