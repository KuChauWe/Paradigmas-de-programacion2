mi_lista = [1,2,3]
tu_lista = (10,20,30)
su_lista = (40,50,100)
def multiplicar_por2(elemento):
    return elemento*2

def solo_impar(elemento):
    return elemento % 2 != 0

# Lista de pares de datos de las dos listas
print(list(zip(mi_lista,tu_lista,su_lista)))

una_lista = ["a","b","c","b","d","m","n","n"]
duplicados = set([x for x in una_lista if una_lista.count(x)>1])
print(duplicados)
