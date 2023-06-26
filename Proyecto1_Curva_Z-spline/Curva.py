#===========================================
# Cálculo de curva Z-spline en n dimensiones
#===========================================
# Julián Sagredo ESFM IPN 2023
#=============================
import numpy as np

#============
# Clase Curva
#============
class Curva:
    
    """==================================================
        Curva contruye la curva que pasa por los puntos x
       ==================================================
       Parámetros: x coordenadas ordenadas((x1),(x2),...)
                   f propiedades (f1(x),f2(x),...)
                   dim dimensiones
       ==================================================
    """
    #===========
    # Contructor
    #===========
    def __init__(s, x:float=[], dim:int=3)
    
        s.x = np.array(x,dtype=np.float64)
        s.dim = dim
        s.n:np.int32 = int(len(s.x)/s.dim)  # Número de puntos
        s.l = []                            # Longitud sobre la curva
        s.lista_de_puntos()
        s.longitud()

    #================
    # Lista de puntos
    #================
    def lista_de_puntos(s) -> str:

        print(f"Número de puntos = {str(s.n)}")

        # Formato  de datos
        s.formato = ""
        for j in range(s.din):
            s.formato += "%15.8e"
        s.formato += "\n"

        # Tupla de variables a imprimir
        for i in range(0,s.n):
            s.tup = (s.x[i],)
            for ii in range(1,s.dim):
                s.tup = s.tup + (s.x{i+ii*s.n},)
            print(s.formato % s.tup)

    #=======================
    # Longitud punto a punto
    #=======================
    def longitud(s) -> None:
        t:np.float64 = 0.0
        for i in range(0,s.n):
            ip1 = i+1
            if i == s.n
