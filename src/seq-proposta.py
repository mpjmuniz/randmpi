# - - coding: utf- 8 - -
from mpi4py import MPI
import sys
from rand import randutil as ru
from mpi4py.MPI import ANY_SOURCE

'''lendo a especificação, me pareceu que não é necessário o uso de MPI na versão serial. Colocarei aqui uma versão alternativa. quando der, decidimos a utilizada'''

rd_list = ru.getRandomList(sys.argv[1], sys.argv[2], sys.argv[3])
prime = []

for i in rd_list:
    if ru.isPrime(i)[0]:
        prime.append(i)

ru.writeList(prime, "primos_seq-proposta")

