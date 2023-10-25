"""
BANCO DE DADOS DA CATEGORIA: Ataques de Senhas
TODAS AS FERRAMENTAS RELACIONADAS COM ESSA CATEGORIA ESTARÃO AQUI.
"""

import os
from modules.logos import *
from os.path import exists

# Defina códigos de escape ANSI para cores
vd = "\33[1;36m" # Ciano
vlh = "\33[1;31m" #vermelho 
bra = "\33[1;37m" # branco
az = '\033[34m' # Azul
ma = '\033[35m' #Magento
am = '\033[33m' #Amarelo 

#variável com caminho até o diretório bin
Dirbin= "/bin"
#variável com caminho até o diretório home
CasaDir = "/home"

def banner_ataque_senhas():
    banner()
    banner_ataque_senhas = open("modules/banners/categ_ataque_senhas.txt")
    print(banner_ataque_senhas.read())
    backmenu_inicial()

##################### Repositório
