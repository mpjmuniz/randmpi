# - - coding: utf- 8 - -
#hello.py
#makes available the MPI module from the mpi4py package
from mpi4py import MPI
#MPI.COMM_WORLD is a static reference to a Comm object of which the current process can learn about its rank
comm = MPI.COMM_WORLD

#A “communicator” represents a system of computers or processors which can communicate with each other via MPI commands

#root mpi4py class, Comm, which stands for Communicator
rank = comm.Get_rank()
#A rank is the process’s id within a communicator.

# each process has its own separate copy of local variables.

print "hello world from process ", rank
