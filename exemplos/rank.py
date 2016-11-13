# - - coding: utf- 8 - -
from mpi4py import MPI
#Determines the rank of the calling process in the communicator.
rank = MPI.COMM_WORLD.Get_rank()
print(rank)
