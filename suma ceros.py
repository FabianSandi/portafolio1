#Entrada: un número entero mayor o igual a cero
#Salida: la cantidad de ceros incluidos en el número ingresado 
#Restricciones: debe ser un número entero y este debe ser mayor o igual a cero
def sumaceros(num):
   if isinstance(num, int) and num>=0:
      if num==0:
         return 1
      elif num>0 and num<10:
         return 0
      else:
         if num%10==0:
            return 1+sumaceros(num//10)
         else:
            return sumaceros(num//10)
   else:
      return ('Su número no cumple con las restriccioes, intente de nuevo con otro número')
