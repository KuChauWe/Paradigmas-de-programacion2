#================
# Primera función
#================
def saludo():
    #====================================
    # Documentación rápida de lla función
    #====================================
    """Esta función saluda"""
    print ('¡Q onda¡, ¿Cómo estás?')

#======================
# Llamado de la función
#======================
saludo()

#=============================
# Se ejecuta pero no se asigna
#=============================
salida = saludo ()

#=================
# Esto no funciona
#=================
print (salida)

#======================
# Mostrar documentación
#======================
#help(saludo) (?)

#======================
# Función con argumento
#======================
def salu2(nombre):
    """Esta función te saluda por tu nombre"""
    print ("Hola muy buenas",nombre,"o.O")
salu2("Julián")
salu2("Hugo")

#==========================================
# Ahorrar trabajo del intérprete
# nombre:str (la variable nombre es un str)
#==========================================
def saludos(nombre:str):
    """Esta función te saluda por tu nombre estrictamente"""
    print ("Hola muy buenas",nombre,"O.o")

saludos("Julián")
a = 123
print (type(a))
saludos(a)

#==============================
# Función con muchos argumentos
#==============================
def saludos_multiples(nombre1,nombre2,nombre3):
    """Esta función saluda a 3 personas al mismo tiempo"""
    print ("Hola ",nombre1,", ",nombre2," y ",nombre3)

saludos_multiples("Hugo","Paco","Luis")

#===========================================
# Función con cualquier número de argumentos
#===========================================
def muchos_saludos(*nombres):
    """Esta función saluda a todos los que quieras"""
    i = 0
    #================================
    # end= (para ponerlo de corrido) (?)
    #================================
    print ("Hola ", end="")
    while len(nombres) > i:
        # último nombre
        if (i==len(nombres)-1):
          print(nombres[i])
        else:
        # cualquier otro nombre
          print(nombres[i],end=", ")
        i += 1

muchos_saludos("Bosco","Angel","David","Tamara","Mili","Edwin","Lev","Luis","Abigail")

def greet(firstname,lastname):
    print ("Hello", firstname,lastname)

#===============================================
# Llamar a la función con argumentos en desorden
#===============================================
greet(lastname = 'Jobs',firstname='Steve') #Se pueden especificar las variables en desorden

#=====================================
# Función con argumentos escondidos **
#=====================================
def greet(**person): # (?)
    #===================================================
    # persona tiene características firstname y lastname
    #===================================================
    print('Hola',person['firstname'],person['lastname'])

greet(firstname='Steve',lastname='Jobs')
greet(lastname="Jobs",firstname='Steve')
greet(firstname="Bill",lastname="Gates",age=55) #Se pueden pasar más parámetros de los necesarios

#================================
# Función con valores por defecto
#================================
def greet(name='Guest'):
    print( 'Hola',name)

greet() #Utiliza el valor predeterminado (Guest)
greet('Steve')

#=======================
# Función como resultado
#=======================
def suma (a,b):
    return a + b

#========================================
# Programación funcional
# Se puede hacer una función de funciones
#========================================
total = suma (5,suma(10,20))
print (total)

#================================================
# Cálculo lambda
# nombre de la función = lambda variable : función
#================================================
x_al_cuadrado = lambda x : x * x
a1 = x_al_cuadrado(5)
print (a1)

#===========================
# Lambda de varias variables
#===========================
suma = lambda x1,x2,x3: x1+x2+x3
print (suma(99,98,97))

sumas = lambda *x: x[0]+x[1]+x[2]+x[3]

print (sumas(100,200,300,400))

#===========================
# Uso de una función anónima 
#===========================
print ((lambda x : x * x)(6)) # Función anónima

#============================
# Función con variable global
# EVITAR EL EXCESOOOOOOOOO
#============================
name = 'Steve'
def greet():
    global name # para utilizar ua variable global (que viene afuera del bloque)
    name = 'Bill'
    print ('Hola',name)

greet()
