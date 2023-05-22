from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#=========================
# Clase storemanager
# NO TIENE VARIABLES (OJO)
#=========================
class ManejoDeInscripciones:
    #==========================================================
    # Decorador staticmethod
    # El objeto sólo tiene la funcion incribirUsuario
    # Envuelve la función sin llamar variables locales O.o
    # El objeto ManejoDeInscripciones es la interface cambiable
    #==========================================================
    @staticmethod
    def inscribirUsuario(usuario:Usuario,repositorioDeUsuarios:RepositorioDeUsuarios)->None:
        print (".-.-.-.-.-Guardando usuario.-.-.-.-.-.\n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()
