# - - coding: utf- 8 - -
from mpi4py import MPI
import sys
import numpy
from rand import randutil as ru
from mpi4py.MPI import ANY_SOURCE

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

recv_buffer = numpy.array([-1,-1])
rd_list = ru.getRandomList(sys.argv[1], sys.argv[2], sys.argv[3])
prime = []
for i in rd_list:
    print(i)
    
if rank == 0:
    for i in range(1, size):
        comm.Recv(recv_buffer, source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG)
        print("G:" + str(recv_buffer[0]) + ":" + str(recv_buffer[1]))
        if(recv_buffer[0]): #Se número é primo ou não
            prime.append(recv_buffer[1]) #NÚMERO PRIMO            
else:
    n = rd_list.pop() #PROBLEMA AQUI ELE NÃO DÁ POP CERTO, PRECISA FAZER O ACESSO CONCORRENTE A ESSA LISTA!!!
    n_np = ru.isPrime(n)
    print("R:" + str(rank) + "|" + str(n) + "|" + str(n_np[0]) + ":" + str(n_np[1]))
    comm.Send(n_np, dest=0, tag=rank)

if comm.rank == 0:
    ru.writeList(prime, "primos_seq")
