#===========================
# Recursividad y memoización 
#===========================

#==============================
# Herramientas para memoización
#==============================
from functools import lru_cache

def feibonacci_lento(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n>2:
        return fibonacci_lento(n-1)+fibonaccio_lento(n-2)

for i in range(1,36):
    print(str(i)+":",fibonacci_lento(i))

#======================================
# Optimización 2: uso de conjuntos para 
#                 guardar valores
#======================================

#=======================
# Conjunto de fibonaccis
#=======================
fibonaccis = {}
def fibonacci(n)

    #=======================================
    # Revisa si ya existe y regresa el valor
    #=======================================
    if n in fibonnaccis:
        return fibonnaccis[n]

    if n==1:
        valor = 1
    elif n==2:
        valor = 1
    elif n>2:
        valor = fibonacci(n-1)+fibonacci(n-2)

    #=========
    # Guárdalo
    #=========
    fibonaccis[n] = valor
    return valor

for i in range(1,10001):
    print(str(i)+":",fibonacci(i))

#======================================
# Uso de decoradores para memoización
# maxsize: es cuantos anteriores guarde
#======================================

