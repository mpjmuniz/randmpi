# - - coding: utf- 8 - -
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE
from rand import randutil as ru
import numpy
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
    recv_buffer = numpy.array([-1,-1])

    for i, num in enumerate(rd_list):
        comm.Send(numpy.array([num]), dest=(i % size), tag=0)
        comm.Recv(recv_buffer, source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG)
        print("G:" + str(recv_buffer[0]) + ":" + str(recv_buffer[1]))
        if recv_buffer[0]:
            prime.append(num)

    ru.writeList(prime, "primos_par")
else:
    # Escravo
    n = numpy.array([-1])
    comm.Recv(n, source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG)
    n_np = ru.isPrime(n[0])
    print("R:" + str(rank) + "|x|" + str(n_np[0]) + ":" + str(n_np[1]))
    comm.Send(n_np, dest=0, tag=rank)

