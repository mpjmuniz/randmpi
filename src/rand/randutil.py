#!/usr/bin/python
# - - coding: utf- 8 - -

import random
import math
import numpy as np

#   Função responsável por criar uma lista com números aleatórios em cada uma das posições
#   seed: semente para geração dos números
#   size: tamanho da lista
#   ub: upper bound, limite superior para geração dos números
#
#   retorna: lista gerada
def getRandomList(seed, size, ub):
    random.seed(seed)
    # lista de tamanho size
    rdList = []
    for i in range(1, int(size)):
        # random.uniform: retorna um número aleatório entre a e b
        rdList.append(int(random.uniform(a = 1, b = int(ub))))

    return rdList

#   Função responsável por verificar se um dado número num é primo ou não
#   num: número à ser verificado
def isPrime(num):
    n = int(num)
    return np.array([int(n > 1 and all(n % i for i in range(2, int(n)))), n])
    

#   Função responsável por escrever lista no arquivo, no formato correto
#   randomList: lista à ser escrita
#   filePath: arquivo à receber lista
def writeList(randomList, filePath):
    #with fecha arquivo sozinho, propriamente
    with open(filePath, 'w+') as fileRef:
        fileRef.write("%d\n" % len(randomList))

        for num in randomList:
            fileRef.write("%d " % num)

#   Função responsável por ler lista do arquivo, no formato correto
#   filePath: caminho do arquivo à ser lido
#   retorna: lista com números do arquivo
def readList(filePath):
    with open(filePath, 'r+') as fileRef:
        size = int(fileRef.readline())
        numbers = fileRef.readline().split(' ')
        numbers.pop()
        randomNumbers = []
        for i in numbers:
            randomNumbers.append(int(i))
        return randomNumbers

