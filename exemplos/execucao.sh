#!/bin/bash
mpiexec  -n 5 python  $1.py

# MPI, a wrapper around whatever program you to pass into it
# The -n 5 option specifies the desired number of processes.

#para o trapParelelo
#mpiexec -n 4 python trapParallel_1.py 0.0 1.0 10000
