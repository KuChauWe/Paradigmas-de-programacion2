#=================================
# Programación orientada a objetos
#=================================

#===============================
# Una clase para un objeto vacío
# No está tan vacío, necesita
# la palabra pass = pasar
#===============================
class ObjetoVacio:
    pass

#=======================
# Nada es un ObjetoVacio
#=======================
nada = ObjetoVacio()
print(type(nada))

#================
# La clase llanta
#================
    #====================================
    # Variable cuenta es de toda la clase
    #====================================
    cuenta = 0
    #==================================
    # Funcionconstuctora de identidad
    # __init__ es una función reservada
    # comienza con uno mismo: self
    # pero puede ser otro nombre (mi)
    # parámetros de entrada = default
    #==================================
    def __init__(mi,radio=50,ancho=30,presión=1.5):
        #Variablede la estructura completa Llanta
        Llata.cuenta += 1
        # Variables de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presión = presión # Por cierto, sí admite acentos:)

#=======================
# Objetos (instanciados)
#=======================
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presión=1.2)
llanta3 = Llanta()
llanta4 = Llanta(40,30,1.6)


#=================================
# Objeto qu contiene otros objetos
#=================================
class Coche :
    def __init__(mi,ll1,ll2,ll3,ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4

micoche = Coche(llanta1,llanta2,llanta3,llanta4)

print("Total de llantas: "Llanta.cuenta) #variable global de la clase
