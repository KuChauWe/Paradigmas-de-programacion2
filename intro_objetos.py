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
class Llanta:
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
        Llanta.cuenta += 1
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

print("Total de llantas: ",Llanta.cuenta) #variable global de la clase
print("Presión de llanta 4 = ",llanta4.presión) #Presión de la llanta 4
print("Radio de la llanta 4 = ", llanta4.radio)
print("Radio de la llanta 3 = ", llanta3.radio)
print("Presión de la llanta 1 de mi coche = ",micoche.llanta1.presión)

#================
# Encapsulamiento
#================

#====================================================================
# Uso de la función de python property para poner y obtener atributos
#====================================================================
class Estudiante:
    def __init__(mi):
        mi.__nombre= ''
    def ponerme_nombre(mi,nombre):
        print("Se llamó a ponerme_nombre")
        mi.__nombre = nombre 
    def obtener_nombre(mi):
        print("Se llamó a obtener_nombre")
        return mi.__nombre
    nombre = property(obtener_nombre,ponerme_nombre)

#======================================
# Crear un objeto estudiante sin nombre
#======================================
estudiante = Estudiante()

#=====================================================================
# Ponerle nombre usando la propiedad nombre y el método ponerme_nombre
# (sin tener que llamar explicitamente a la función)
#=====================================================================

estudiante.nombre = "Diego"

#================================================================
# Obtener el nombre con el método obtener_nombre
# __nombre es una variable encapsulada (no visible desde fuera)
# (sin tener que llamar explítamente a la función obtener_nombre)
#================================================================
print(estudiante.nombre)

# ojo piojo
# print(estudiante.__nombre) NO FUNCIONA



