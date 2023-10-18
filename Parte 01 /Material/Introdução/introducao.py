# Importações de pacotes
import sys
import math

# Importações de partes de pacotes
from math import pi
from numpy import arange, array
from numpy import (
    amax,
    amin,
    ceil,
    floor
)

# Declaração de variáveis
numero = 4
numero_impar = 5

# Declaração de funções
def soma(x, y):
    return x + y

# Declaração de estruturas de dados
saudacao = ["Bom dia", "Boa tarde", "Boa noite"]

# Declaração de função
def define_saudacao(hora):
    if(hora >= 6 and hora <= 12):
        op = 0
    elif(hora >= 13 and hora <= 18):
        op = 1
    else:
        op = 2
    print(saudacao[op])

# Chamada de Função
define_saudacao(15)
