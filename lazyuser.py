#!/usr/bin/env python
"""_____________________________________________________
+=[ BY: AstralSec from BRAZIL                           
+=[ Version 0.2                                         
+=[ YouTube: https://youtube.com/@AstralSec_Haxor       
+=[ Github: https://github.com/AstralSecHaxor/LazyUser  
   —————————————————————————————————————————————————————
SCRIPT DO USUÁRIO 
AQUI ESTARÃO TODAS AS FUNÇÕES DAS CATEGORIAS 
QUE O USUÁRIO USARÁ PARA NAVEGAR PELO TOOL."
"""
import os
from time import sleep as timeout
from modules.gerenciador import *
from modules.logos import *
from os.path import isdir

# Defina códigos de escape ANSI para cores
vd = "\33[1;36m" # Ciano
vrd='\033[0;32m'   # Verde
vlh = "\33[1;31m" #vermelho 
bra = "\33[1;37m" # branco
az = "\033[34m" # Azul
ma = "\033[35m" #Magento
am = "\033[33m" #Amarelo 

banner_inicial()
while True:
    try:
        lazyscript = input(f"{vd}┬─{az}[{am}A.S.H{vlh}♘{bra}{sistema_atual}{az}]{vd}─{az}[{ma}~/{az}]\n{vd}╰─>{vlh}$ {bra}")
        option_control  = lazyscript.replace(" ", "")
        
    except KeyboardInterrupt:
        sair_do_programar().exit()
    except EOFError:
        sair_do_programar().exit()
            
    ## Categoria: Coletar de informações
    if option_control == "1" or option_control == "01":
        coletar_informacoes()
        
    ## Categoria: análise de vulnerabilidades
    elif option_control == "2" or option_control == "02":
        analise_vulnerabilidades()
    
    ## Categoria: Web Hacking
    elif option_control == "3" or option_control == "03":
        web_hacking()
        
    ## Categoria: Avaliações de Banco de dados.
    elif option_control == "4" or option_control == "04":
        avaliacoes_databases()
        
    ## Categoria: Ataque Senhas
    elif option_control == "5" or option_control == "05":
        ataque_senhas()
    
    ## Categoria: ataques Sem Fio
    elif option_control == "6" or option_control == "06":
        ataque_sem_fio()
        
    elif option_control == "7" or option_control == "07":
        pass
    
    elif option_control == "8" or option_control == "08":
        pass
    
    elif option_control == "9" or option_control == "09":
        pass
    
    elif option_control == "10":
        pass
    
    elif option_control == "11":
        pass
    
    elif option_control == "12":
        pass
    
    elif option_control == "13":
        pass
    
    elif option_control == "14":
        pass
    
    elif option_control == "15":
        pass
    
    elif option_control == "16":
         ferramentas_engenharia_social()
    
    elif option_control == "00" or option_control =="0": sair_do_programar() ## Sair do Script
    
    else:
        print(f"{vlh}\nUps! {bra}'{option_control}'{vlh} opção inválida :({vd}");timeout(1);
        banner_inicial()
