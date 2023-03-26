'''PRIMERA PRÁCTICA DE PYTHON O.o'''
#=============================
# Operaciones básicas juasjuas
#=============================
print (2+3)
print (2*3)
print (2/3)
print (2**10)
print (2**0.5) #raíz cuadrada
print (10%2) #residuo
print (10%0.1) #solo de python 

#============================================= 
# Para saber el tipo de objeto que se usa type 
#============================================= 
t=0
print(type(t)) #entero
t=3.6
print(type(t)) #real (flotante)
t=True
print(type(t)) #booleano (bool)

#=====================
# Mensajes en pantalla
#=====================
print ("Este es un comentario en python. ", "Este es otro enunciado". t)
print ('id: ',1)
print ('First Name: ', 'Doo') 
print ('Last Name: ', 'Mentio')
print ("Vamos a sumar esto" + " con esto otro")

#==============================================
# Continuar una instruccion en varios renglones
#==============================================
if 100 > 99 and \
    200 <= 30 and \
    true != False:
	print('Hola mundo')

#======================================
# Comandos diferentes en la misma línea
#======================================
print ("Hola "); print ("tu!!") #Se considera mala práctica o.O

#===============================================
# Usando paréntesis redondos, cuadrados o llaves
# se puede escribir en varios renglones
#===============================================
list = [1,2,3,4,
	5,6,7,8,
	9,10,11,12]

matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]

print(list)
print(matriz)

#==================================================================
# Indentación estricta para procesos dependientes de : (dos puntos)
#==================================================================
if 10 > 5:
  print ("diez es mayor que cinco") 
  print ("otra indentación")
for i in list:
  print (i)
print ("Ok")
if 10 > 5:
  print ("verdadero")
  if 10 < 20:
    print ("verdadero")
elif 5 > 3: # Comienza segundo condicional
  print ("esto no se imrpimirá")
else:
  print ("aquí nunca llega")

#==========       
# Funciones
#==========
def say_hello(name):
    print ("Hello", name)
    print ("Welcome to Python Tutorials")

say_hello("Hugo")


#----------------------------------------
#========================================
#		PARTE 2
#========================================
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

#====================================================
# Input permite obtener datos del usuario en prompter
#====================================================
nombre = input ("Dame tu nombre: ")
print ("Felicidades, cumples años en: ", nombre)

#=======================================
# Los enteros son de precisión ilimitada
#=======================================
y = 500000000000000000000000000000000
print (y)

#==================================================================
# Se pueden delimitar números con algún guión bajo pero no con coma
#==================================================================
y = 5_000_000
print (y)

#===================================================
# La función int() cambia strings y floats a enteros
#===================================================
numero = int(input("Dame tu edad: "))
type(numero)

#==================================================
# La notación científica de flotantes utiliza e o E
#==================================================
# 1.2 x 10^{-9}                  
#==============
y = 1.2E-09
print (y)

#========================================================
# La función float() convierte strings y enteros a floats
#========================================================
y = float("14.3")
print (y)

#===================================================
# Los complejos se escriben con la raíz de menos uno
# j siempre con un número como prefijo
# no acepta la j sola
#===================================================
z = 1+1j

# suma +
# resta -
# multiplicación *
# división /
# módulo %
# exponente **
# // función piso # (?)
# Funciones para transformar números int() float() complex()
# Operadores abs() round() pow()   

print(round(3.14159,4))

#=========================
# Strings de varias líneas
#=========================
parrafo = """En el bosque de la china
 la chinita se perdió """
print (parrafo)

#==============================================
# La función len() obtiene el tamaño del string
#==============================================
n = len(parrafo)
print (n)

#============================================================
# Las letras en un string ocupan lugares como en un arreglo
# (también de atrás para adelante comenzando en -1 el último)
#============================================================
palabra = "hola"
print(palabra[0])
print(palabra[-4])
