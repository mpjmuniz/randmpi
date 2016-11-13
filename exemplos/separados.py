# - - coding: utf- 8 - -
#seperateCodes.py
from mpi4py import MPI
rank = MPI.COMM_WORLD.Get_rank()

a = 6.0
b = 3.0
if rank == 0:
        print(str(rank) + '|' + str(a + b))
if rank == 1:
        print(str(rank) + '|' + str(a * b))
if rank == 2:
        print(str(rank) + '|' + str(max(a,b)))
