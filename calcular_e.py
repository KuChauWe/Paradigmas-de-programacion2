#==============================
# Algoritmo 1
#==============================
# Serie exponencial
# Factorización de x
# Negativos con función inversa
#==============================
n = 200
x = -100.0
flag= false
if x < 0:
    flag = true
    x = -x
s = 1.0
for i in range(n,0,-1):
     s *= x/float(i)
     s += 1.0
if flag == true 
 s = 1/s
 print (s)

