# - - coding: utf- 8 - -
from mpi4py import MPI
#Returns the number of processes in the communicator. It will return the same number to every process.
size = MPI.COMM_WORLD.Get_size()

print("tamanho: ", size)
