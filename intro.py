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

#==============================================
# Para saber el tipo de objeto qque se usa type
#==============================================
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
