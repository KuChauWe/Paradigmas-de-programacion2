#=========================================
# Listas
# Las listas pueden ser objetos diferentes
#=========================================
miprimeralista = [] # lista vacía
print (miprimeralista)

#=================
# Llenado de lista
#=================
miprimeralista = [1,"Javier",1.34,"Bosco","Angel","Abigail",True]
print(miprimeralista)

#=====================================
# list: hacer una lista
# range(i,j): secuencia de i hasta j-1
#=====================================
nums = list(range(1,61))

for i in nums:
    print (i)

#=====================================
# Incluir nuevos elementos en la lista
#=====================================
nums.append(61)
nums.append(62)
nums.append(61)
print(nums)

