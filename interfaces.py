#=========================================================
# Del directorio aplicación, el subdirectorio repositorio,
# el archivo basededatos.py : trae el objeto "BaseDeDatos"
#=========================================================
from aplicacion.repositorio.basededatos import BaseDeDatos

#=========================================================
# Del directorio aplicación, el subdirectorio repositorio,
# el arhivo s3.py : trae el objeto "S3"
#=========================================================
from aplicacion.repositorio.s3 import S3

#=========================================================
# Del directorio aplicación, el subdirectorio repositorio,
# el archivo sistemadearchivos.py : trae el objeto
# "SistemDeArchivos"
#=========================================================
from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos

#=====================================================
# Del directorio aplicación, el subdirectorio modelos,
# el archivo usuario.py : trae el objeto "Usuario"
#=====================================================
from aplicacion.modelos.usuario import Usuario

#======================================================
# Del directorio aplicación, el subdirectorio negocios,
# el archivo manejodeinscripciones.py : trae el objeto 
# "ManejoDeInscripciones"
#======================================================
from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones

#========================
# Crear el objeto Usuario
#========================
usuario = Usuario("Roberto","Jimenez",18)

#===================
# Crear un objeto S3
#===================
repositorioS3 = S3("321221321","sfd324223","MiCubeta")

#============================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#============================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")

#====================================
# Crear el objeto sistema de archivos
#====================================
repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")

#=============================================================
# Interface inscribirUsuario  del objeto ManejoDeInscripciones
#=============================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDeArchivos)
print("\n")

#=============================
#  Crear el objeto basededatos
#=============================
repositorioBaseDeDatos = BaseDeDatos("localhost","admin","admin123")

#=============================================================
# Interfase inscribir usuario del objeto ManejoDeInscripciones
#=============================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")
