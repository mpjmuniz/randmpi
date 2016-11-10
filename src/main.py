#!/usr/bin/python
# - - coding: utf- 8 - -

import random
import math

#   Função responsável por criar uma lista com números aleatórios em cada uma das posições
#   seed: semente para geração dos números
#   size: tamanho da lista
#   ub: upper bound, limite superior para geração dos números
def getRandomList(seed, size, ub):
    random.seed(seed)
    # lista de tamanho size
    rdList = []
    for slot in rdList:
        # random.uniform: retorna um número aleatório entre a e b
        rdList.append(random.uniform(a = 1, b = ub))

    return rdList

#   Função responsável por verificar se um dado número num é primo ou não
#   num: número à ser verificado
def isPrime(num):
    # método ineficiente para verificação
    return num > 1 and all(num % i for i in range(2, int(math.sqrt(num))))

#   Função responsável por escrever lista no arquivo, no formato correto
def writeList(randomList, filePath):
    fileRef = open(filePath, 'w+')
    fileRef.write("%d\n" % len(randomList))

    for num in randomList:
        fileRef.write("%d " % num)

#   Função responsável por ler lista do arquivo, no formato correto
#   TODO: ler input formatado
def readList(fileRef):
    fileRef = open(filePath, 'r+')
    content = fileRef.read()

