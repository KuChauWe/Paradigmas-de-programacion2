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
    print ("Hola muy buenas",nombre;"o.O")
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
def saludos_multriples(nombre1,nombre2,nombre3):
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


