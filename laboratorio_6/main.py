from aplicacion.banco.cliente_bancario import ClienteBancario

#===========================================
# try: intenta (correr las intrucciones)
# except: atrapar el error en una variable e
# e se puede convertir a string
#===========================================

#========================================
# Error por sacar más diero del que tiene
#========================================
try:
  cliente = ClienteBancario("Jaime Andrade","Hernández Sánchez",28,0.0)
  cliente.guardarDinero(500) #El error sería si fuese menor a 400
  print(cliente.imprimirInfo())
  cliente.retirarDinero(400)
  print(cliente.imprimirInfo())
#============================================
# Exception es el objeto más general de error
#============================================
except Exception as e:
    print("Error(1): "+str(e))

#===================================
# Error por usar un atributo privado
#===================================
#try:
#  print(cliente.__nombres)
#except Exception as ex:
#  print("Error(2): "+str(ex))

#===============
# Forma correcta
#===============
print(cliente.nombres)


