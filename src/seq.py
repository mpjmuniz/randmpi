# - - coding: utf- 8 - -
from mpi4py import MPI
import sys
import numpy
from rand import randutil as ru
from mpi4py.MPI import ANY_SOURCE

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

recv_buffer = False
rd_list = ru.getRandomList(sys.argv[1], sys.argv[2], sys.argv[3])
prime = []

if rank == 0:
    for i in range(1, size):
        comm.Recv(recv_buffer, ANY_SOURCE)
        if(recv_buffer[0]): #Se número é primo ou não
            prime.append(recv_buffer[1]) #NÚMERO PRIMO            
else:
    comm.Send(ru.isPrime(rd_list.pop()))

if comm.rank == 0:
    ru.writeList(prime, "output")
