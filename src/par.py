# - - coding: utf- 8 - -
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE
from rand import randutil as ru
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = size = comm.Get_size()

seed = int(sys.argv[1])
list_size = int(sys.argv[2])
max_num = int(sys.argv[3])


if rank == 0:
    # Mestre
    rd_list = ru.getRandomList(seed, list_size, max_num)
    prime = []
    ans = {0:True}

    for i, num in enumerate(rd_list):
        comm.send(num, dest=(i % size))
        ans = comm.recv(ANY_SOURCE)
        if ans :
            prime.append(i)

    ru.writeList(prime, "nums_primos")
else:
    # Escravo
    numero = comm.recv()
    comm.Send(ru.isPrime(numero))

