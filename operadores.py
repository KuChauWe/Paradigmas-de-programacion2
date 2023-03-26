#====================
# Conjuntos en python
#====================
even_nums = {2,4,6,8,10} #conjunto de números pares
print (even_nums)

# El bool no es parte del conjunto
emp = {1,'Steve',10.5,True} # conjunto de diferentes objetos (?)
print (emp)

nums = {1,2,2,3,4,4,5,5}
print (nums) #como en cualquier conjunto solo toma 1: 1,2,3,4,5

#===============================
# Convertir secuencia a conjunto
# No lo genera en orden
#===============================
s = set("Hello")
print (s)
s = set((1,2,3,4,5)) #tupla a conjunto
print (s)

#==============================================
# De diccionario a conjunto: conjunto de llaves
#==============================================
d = {1:'One', 2:'Two'}
s = set(d)
print (s)

s.add(100)
print (s)

s.update(nums) # (?)
print (s)

s.remove(100)
print (s)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

su = s1|s2 #unión
print (su)


