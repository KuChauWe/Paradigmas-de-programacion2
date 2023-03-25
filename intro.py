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


