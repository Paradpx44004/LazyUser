"""
BANCO DE DADOS DA CATEGORIA: Análise de Vulnerabilidades 
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

## Buscando diretório /bin do sistema do usuário no logos.py
def obter_diretorio_base(sistema):
    if sistema == "Termux":
        return "/data/data/com.termux/files/usr/bin"
    elif sistema in ["Ubuntu", "Debian", "Kali"]:
        return "/usr/bin"
    else:
        return None

sistema_atual = verificar_sistema()
bIn = obter_diretorio_base(sistema_atual)

# Obtém o caminho da pasta home do usuário atual
home = os.path.expanduser("~")
################ Instalações via APT



################ Instalações via PIP


################ Instalações via WGET



################ Instalações via GIT

def sqliv():
	if os.path.exists(f"{home}/sqliv"):Installed_banner();print(f"O {am}SQLiv{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando SQLiv via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python2 git')
	    os.system('git clone https://github.com/the-robot/sqliv')
	    os.system('mv sqliv {}'.format(home))
	    if os.path.exists(f"{home}/sqliv"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    
	    
def sqlscan():
	if os.path.exists(f"{home}/sqlscan"):Installed_banner();print(f"O {am}SQLScan{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando SQLScan via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git php')
	    os.system('git clone http://www.github.com/Cvar1984/sqlscan')
	    os.system('mv sqlscan {}'.format(home))
	    if os.path.exists(f"{home}/sqlscan"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    
	    
def wordpreSScan():
	if os.path.exists(f"{home}/Wordpresscan"):Installed_banner();print(f"O {am}Wordpresscan{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando Wordpresscan via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('git clone https://github.com/swisskyrepo/Wordpresscan')
	    os.system('mv Wordpresscan {}'.format(home))
	    if os.path.exists(f"{home}/Wordpresscan"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	        
	        
def wpscan():
	if os.path.exists(f"{home}/wpscan"):Installed_banner();print(f"O {am}WPScan{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando WPScan via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git ruby curl')
	    os.system('git clone https://github.com/wpscanteam/wpscan')
	    os.system('mv wpscan {0} && cd {0}/wpscan'.format(home))
	    os.system('gem install bundle && bundle config build.nokogiri --use-system-libraries && bundle install && ruby wpscan.rb --update')
	    if os.path.exists(f"{home}/wpscan"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    
	    
def wordpresscan():
	if os.path.exists(f"{home}/termux-wordpresscan"):Installed_banner();print(f"O {am}Termux-Wordpresscan{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando Termux-Wordpresscan via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install nmap figlet git')
	    os.system('git clone https://github.com/silverhat007/termux-wordpresscan')
	    os.system('cd termux-wordpresscan && chmod +x * && sh install.sh')
	    os.system('mv termux-wordpresscan {}'.format(home))
	    print(f"{vlh}\nUser comando:{bra} wordpresscan para começar")
	    if os.path.exists(f"{home}/termux-wordpresscan"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    
	    
def tmscanner():
	if os.path.exists(f"{home}/TM-scanner"):Installed_banner();print(f"O {am}TM-scanner{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando TM-scanner via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python python2 nmap git -y')
	    os.system('python -m pip install colorama requests')
	    os.system('python2 -m pip install colorama requests')
	    os.system('git clone https://github.com/TechnicalMujeeb/TM-scanner')
	    os.system('mv TM-scanner {}'.format(home))
	    if os.path.exists(f"{home}/TM-scanner"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    
	    
def rang3r():
	if os.path.exists(f"{home}/rang3r"):Installed_banner();print(f"O {am}Rang3r{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando Rang3r via GIT...\n')
	    os.system("apt update && apt upgrade")
	    os.system("apt install git python")
	    os.system("git clone https://github.com/floriankunushevci/rang3r")
	    os.system("mv rang3r {}".format(home))
	    if os.path.exists(f"{home}/rang3r"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	        
	        
def routersploit():
	if os.path.exists(f"{home}/routersploit"):Installed_banner();print(f"O {am}RouterSploit{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando RouterSploit via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python2 git')
	    os.system('python2 -m pip install requests')
	    os.system('git clone https://github.com/threat9/routersploit')
	    os.system('mv routersploit {}'.format(home))
	    if os.path.exists(f"{home}/routersploit"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	        
	        
def sh33ll():
	if os.path.exists(f"{home}/SH33LL"):Installed_banner();print(f"O {am}SH33LL{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando SH33LL via GIT...\n')
	    os.system("apt update && apt upgrade")
	    os.system("apt install git python2")
	    os.system("git clone https://github.com/LOoLzeC/SH33LL")
	    os.system("mv SH33LL {}".format(home))
	    if os.path.exists(f"{home}/SH33LL"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	        
	        
def xplsearch():
	if os.path.exists(f"{home}/XPL-SEARCH"):Installed_banner();print(f"O {am}XPL-SEARCH{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando XPL-SEARCH via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git php -y')
	    os.system('git clone https://github.com/r00tmars/XPL-SEARCH')
	    os.system('mv XPL-SEARCH {}'.format(home))
	    if os.path.exists(f"{home}/XPL-SEARCH"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	        
	        
def androbugs():
	if os.path.exists(f"{home}/AndroBugs_Framework"):Installed_banner();print(f"O {am}AndroBugs_Framework{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando AndroBugs_Framework via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2 -y')
	    os.system('python2 -m pip install pymongo')
	    os.system('git clone https://github.com/AndroBugs/AndroBugs_Framework')
	    os.system('mv AndroBugs_Framework {}'.format(home))
	    if os.path.exists(f"{home}/AndroBugs_Framework"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def clickjacking():
	if os.path.exists(f"{home}/Clickjacking-Tester"):Installed_banner();print(f"O {am}Clickjacking-Tester{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando Clickjacking-Tester via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python -y')
	    os.system('git clone https://github.com/D4Vinci/Clickjacking-Tester')
	    os.system('mv Clickjacking-Tester {}'.format(home))
	    if os.path.exists(f"{home}/Clickjacking-Tester"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def sn1per():
	if os.path.exists(f"{home}/Sn1per"):Installed_banner();print(f"O {am}Sn1per{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando Sn1per via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python -y')
	    os.system('git clone https://github.com/1N3/Sn1per')
	    os.chdir("Sn1per")
	    os.chdir("..")
	    os.system('mv Sn1per {}'.format(home))
	    if os.path.exists(f"{home}/Sn1per"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	        