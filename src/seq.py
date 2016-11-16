# - - coding: utf- 8 - -
from mpi4py import MPI
import sys
import numpy
from rand import randutil as ru
from mpi4py.MPI import ANY_SOURCE

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n_prime = -1

if(rank == 0):
    rd_list = ru.getRandomList(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    rd_list = None

rd_list = comm.scatter(rd_list, root = 0)
n_np = ru.isPrime(rd_list)
#print("R:" + str(rank) + "|" + str(n_np[0]) + ":" + str(n_np[1]))
if(n_np[0] == 1):
    n_prime = n_np[1]
    
comm.Barrier()
n_prime = comm.gather(n_prime, root=0)
if(rank == 0):
    while -1 in n_prime:
        n_prime.remove(-1)
    ru.writeList(n_prime, "primos_seq")
