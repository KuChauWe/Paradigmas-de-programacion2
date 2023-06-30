#==================================
# mpirun -n 4 python3 tareas_mpi.py
#==================================
from mpi4py import MPI

#========================
# Objeto de comunicadores
#========================
comm = MPI.COMM_WORLD

#=======================
# Cuántos somos en total
#=======================
size = comm.Get_size()

#====================
# Quién soy??????????
#====================
rank = comm.Get_rank()

#===================
# Si yo soy el cero:
#===================
if rank == 0:
    print("Yo soy el proceso 0")

#====================
# Si soy el uno hago:
#====================
elif rank == 1:
    print("Yo soy el proceso 1")

#====================================
# Si yo no soy los 2 anteriores hago:
#====================================
else:
    print("Yo no soy ninguno de los dos primeros procesos :d")

print("Reportándome, soy el proceso ", str(rank), " de ", str(size))

