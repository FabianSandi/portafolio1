#Entrada: ini, que será por donde iniciará la sumatoria, fin que será el número máximo de la sumatoriá y ran, que será el intervalo que se irá sumando a ini hasta acercarse pero no pasarse
#Salida: la sumatoria dadas las variables ingresada ini, fin y ran
#Restricciones: tanto ini como fin y ran deben ser números enteros, de otro modo recibirá un mensaje de error
def sumatoriarango(ini,fin,ran):
    if isinstance(ini, int) and isinstance(fin, int) and isinstance(ran, int):
        if ini>fin:
            return 0
        elif ran>fin:
            return ini
        else:
            return ini+sumatoriarango(ini+ran,fin,ran)
    else:
        return ('Su número no cumple con las restriccioes, intente de nuevo con otro número')
