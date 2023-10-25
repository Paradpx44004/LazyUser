"""
BANCO DE DADOS DA CATEGORIA: coletar de informações
TODAS AS FERRAMENTAS RELACIONADAS COM ESSA CATEGORIA ESTARÃO AQUI.
"""
import os
from modules.logos import *
from os.path import isfile, isdir ,exists
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

#Obtém o caminho da pasta home do usuário atual
home = os.path.expanduser("~")

################ Instalações via APT
def nmap():
    if os.path.exists(f"{bIn}/nmap"):Installed_banner();print(f"O {am}Nmap{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando Nmap via APT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt-get install nmap')
	    if os.path.exists(f"{bIn}/nmap"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	        
	    
################ Instalações via PIP


################ Instalações via WGET
def userrecon():
	if os.path.exists(f"{bIn}/userrecon"):Installed_banner();print(f"O {am}UserRecon{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando UserRecon via WGET...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install wget dpkg curl -y')
	    os.system('wget https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/package/userrecon_1.0_all.deb')
	    os.system('dpkg -i userrecon_1.0_all.deb')
	    os.system('rm userrecon_1.0_all.deb')
	    if os.path.exists(f"{bIn}/userrecon") or os.path.exists(f"{bIn}/RED_HAWK"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	   
	   
################ Instalações via GIT
def red_hawk():
    if os.path.exists(f"{home}/RED_HAWK"):Installed_banner();print(f"O {am}RED_HAWK{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
    else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando RED_HAWK via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git php')
	    os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
	    os.system('mv RED_HAWK {}'.format(home))
	    if os.path.exists(f"{home}/RED_HAWK") or os.path.exists(f"{bIn}/RED_HAWK"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")


def fierce():
	if os.path.exists(f"{home}/fierce"):Installed_banner();print(f"O {am}Fierce{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando Fierce via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python -y')
	    os.system('git clone https://github.com/mschwager/fierce.git')
	    os.system('cd fierce && python -m pip install -r requirements.txt')
	    os.system(f'mv fierce {home}')
	    if os.path.exists(f"{home}/fierce"):
	        print(f"\n{vlh}User comando: {bra}python fierce/fierce.py")
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")


def dnsrecon():
	if os.path.exists(f"{home}/dnsrecon"):Installed_banner();print(f"O {am}DNSRecon{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando DNSRecon via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python')
	    os.system('git clone https://github.com/darkoperator/dnsrecon.git')
	    os.system(f"mv dnsrecon {home}")
	    os.system(f"cd {home}/dnsrecon && pip install -r requirements.txt")
	    if os.path.exists(f"{home}/dnsrecon"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")

	    
	    
def dtect():
    if os.path.exists(f"{home}/D-TECT"):Installed_banner();print(f"O {am}D-TECT{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
    else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando D-TECT via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python2 git')
	    os.system('git clone https://github.com/bibortone/D-Tech')
	    os.system('mv D-Tech {}/D-TECT'.format(home))
	    if os.path.exists(f"{home}/D-TECT"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")

def sqlmap():
    if os.path.exists(f"{home}/sqlmap"):Installed_banner();print(f"O {am}SQLMap{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
    else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalado SQLMap via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2')
	    os.system('git clone https://github.com/sqlmapproject/sqlmap')
	    os.system('mv sqlmap {}'.format(home))
	    if os.path.exists(f"{home}/sqlmap"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")


def reconDog():
    if os.path.exists(f"{home}/ReconDog"):Installed_banner();print(f"O {am}ReconDog{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
    else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando ReconDog via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python2 git -y')
	    os.system('git clone https://github.com/s0md3v/ReconDog')
	    os.system('mv ReconDog {}'.format(home))
	    if os.path.exists(f"{home}/ReconDog"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    
def androZenmap():
    if os.path.exists(f"{home}/AndroZenmap"):Installed_banner();print(f"O {am}AndroZenmap{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
    else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando AndroZenmap via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install nmap curl')
	    os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/androzenmap.sh')
	    os.system('mkdir {}/AndroZenmap'.format(home))
	    os.system('mv androzenmap.sh {}/AndroZenmap'.format(home))
	    if os.path.exists(f"{home}/AndroZenmap"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def sqlmate():
    if os.path.exists(f"{home}/sqlmate"):Installed_banner();print(f"O {am}SQLMate{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
    else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando SQLMate via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python2 git')
	    os.system('python2 -m pip install mechanize bs4 HTMLparser argparse requests urlparse2')
	    os.system('git clone https://github.com/s0md3v/sqlmate')
	    os.system('mv sqlmate {}'.format(home))
	    if os.path.exists(f"{home}/sqlmate"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def astraNmap():
	if os.path.exists(f"{home}/AstraNmap"):Installed_banner();print(f"O {am}AstraNmap{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando AstraNmap via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git nmap')
	    os.system('git clone https://github.com/Gameye98/AstraNmap')
	    os.system('mv AstraNmap {}'.format(home))
	    if os.path.exists(f"{home}/AstraNmap"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def mapeye():
	if os.path.exists(f"{home}/MapEye"):Installed_banner();print(f"O {am}MapEye{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando MapEye via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git php python -y')
	    os.system('python -m pip install requests')
	    os.system('git clone https://github.com/bhikandeshmukh/MapEye')
	    os.system('mv MapEye {}'.format(home))
	    if os.path.exists(f"{home}/MapEye"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def easyMap():
	if os.path.exists(f"{home}/Easymap"):Installed_banner();print(f"O {am}EasyMap{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando EasyMap via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install php -y')
	    os.system('apt install git -y')
	    os.system('git clone https://github.com/Cvar1984/Easymap')
	    os.system('mv Easymap {}'.format(home))
	    os.system('cd {}/Easymap && sh install.sh'.format(home))
	    if os.path.exists(f"{home}/Easymap"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def crips():
	if os.path.exists(f"{home}/Crips"):Installed_banner();print(f"O {am}Crips{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando Crips via GIT...\n')
	    os.system("apt update && apt upgrade")
	    os.system("apt install git python2 openssl curl libcurl wget")
	    os.system("git clone https://github.com/Manisso/Crips")
	    os.system("mv Crips {}".format(home))
	    if os.path.exists(f"{home}/Crips"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def evilURL():
	if os.path.exists(f"{home}/EvilURL"):Installed_banner();print(f"O {am}EvilURL{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	    
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando EvilURL via GIT...\n')
	    os.system("apt update && apt upgrade")
	    os.system("apt install git python2 python3")
	    os.system("git clone https://github.com/UndeadSec/EvilURL")
	    os.system("pip install python-nmap python-whois")
	    os.system("mv EvilURL {}".format(home))
	    if os.path.exists(f"{home}/EvilURL"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def striker():
	if os.path.exists(f"{home}/Striker"):Installed_banner();print(f"O {am}Striker{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando Striker via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2')
	    os.system('git clone https://github.com/s0md3v/Striker')
	    os.system('mv Striker {}'.format(home))
	    os.system('cd /Striker && python2 -m pip install -r requirements.txt'.format(home))
	    if os.path.exists(f"{home}/Striker"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def xshell():
	if os.path.exists(f"{home}/Xshell"):Installed_banner();print(f"O {am}Xshell{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando Xshell via GIT...\n')
	    os.system("apt update && apt upgrade")
	    os.system("apt install lynx python2 figlet ruby php nano w3m")
	    os.system("git clone https://github.com/Ubaii/Xshell")
	    os.system("mv Xshell {}".format(home))
	    if os.path.exists(f"{home}/Xshell"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def owscan():
	if os.path.exists(f"{home}/OWScan"):Installed_banner();print(f"O {am}OWScan{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando OWScan via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git php')
	    os.system('git clone https://github.com/Gameye98/OWScan')
	    os.system('mv OWScan {}'.format(home))
	    if os.path.exists(f"{home}/OWScan"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def osif():
	if os.path.exists(f"{home}/OSIF"):Installed_banner();print(f"O {am}OSIF{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando OSIF via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2')
	    os.system('python2 -m pip install requests')
	    os.system('git clone https://github.com/CiKu370/OSIF')
	    os.system('mv OSIF {}'.format(home))
	    if os.path.exists(f"{home}/OSIF"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def namechk():
	if os.path.exists(f"{home}/Namechk"):Installed_banner();print(f"O {am}Namechk{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando Namechk via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git')
	    os.system('git clone https://github.com/HA71/Namechk')
	    os.system('mv Namechk {}'.format(home))
	    if os.path.exists(f"{home}/Namechk"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def auxile():
	if os.path.exists(f"{home}/AUXILE"):Installed_banner();print(f"O {am}AUXILE{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando AUXILE via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2 && python2 -m pip install requests bs4 pexpect')
	    os.system('git clone https://github.com/CiKu370/AUXILE')
	    os.system('mv AUXILE {}'.format(home))
	    if os.path.exists(f"{home}/AUXILE"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def inther():
	if os.path.exists(f"{home}/inther"):Installed_banner();print(f"O {am}inther{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando inther via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git ruby')
	    os.system('git clone https://github.com/Gameye98/inther')
	    os.system('mv inther {}'.format(home))
	    if os.path.exists(f"{home}/inther"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    
def ginf():
	if os.path.exists(f"{home}/GINF"):Installed_banner();print(f"O {am}GINF{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando GINF via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git php')
	    os.system('git clone https://github.com/Gameye98/GINF')
	    os.system('mv GINF {}'.format(home))
	    if os.path.exists(f"{home}/GINF"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def asu():
	if os.path.exists(f"{home}/ASU"):Installed_banner();print(f"O {am}ASU{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando ASU via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2 php')
	    os.system('python2 -m pip install requests bs4 mechanize')
	    os.system('git clone https://github.com/LOoLzeC/ASU')
	    os.system('mv ASU {}'.format(home))
	    if os.path.exists(f"{home}/ASU"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")

def fim():
	if os.path.exists(f"{home}/fim"):Installed_banner();print(f"O {am}Fim{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando Fim via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python && python -m pip install requests bs4')
	    os.system('git clone https://github.com/karjok/fim')
	    os.system('mv fim {}'.format(home))
	    if os.path.exists(f"{home}/fim"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    
def pwnedOrNot():
	if os.path.exists(f"{home}/pwnedOrNot"):Installed_banner();print(f"O {am}PwnedOrNot{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando PwnedOrNot via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python')
	    os.system('python -m pip install requests')
	    os.system('git clone https://github.com/thewhiteh4t/pwnedOrNot')
	    os.system('mv pwnedOrNot {}'.format(home))
	    if os.path.exists(f"{home}/pwnedOrNot"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")

def zphisher():
	if os.path.exists(f"{home}/zphisher"):Installed_banner();print(f"O {am}Zphisher{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando Zphisher via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git php openssh curl')
	    os.system('git clone https://github.com/htr-tech/zphisher')
	    os.system('mv zphisher {}'.format(home))
	    if os.path.exists(f"{home}/zphisher"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    
	    
def mrsip():
	if os.path.exists(f"{home}/Mr.SIP"):Installed_banner();print(f"O {am}Mr.SIP{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando Mr.SIP via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python -y')
	    os.system('python -m pip install netifaces ipaddress scapy pyfiglet')
	    os.system('git clone https://github.com/meliht/Mr.SIP')
	    os.system('mv Mr.SIP {}'.format(home))
	    if os.path.exists(f"{home}/Mr.SIP"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	   
def phoneinfoga():
	if os.path.exists(f"{home}/PhoneInfoga"):Installed_banner();print(f"O {am}PhoneInfoga{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando PhoneInfoga via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python git -y')
	    os.system('git clone https://github.com/ExpertAnonymous/PhoneInfoga')
	    os.system('mv PhoneInfoga {}'.format(home))
	    if os.path.exists(f"{home}/PhoneInfoga"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def sitebroker():
	if os.path.exists(f"{home}/SiteBroker"):Installed_banner();print(f"O {am}SiteBroker{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando SiteBroker via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python php git -y')
	    os.system('git clone https://github.com/Anon-Exploiter/SiteBroker')
	    os.chdir("SiteBroker")
	    os.system('python -m pip install -r requirements.txt')
	    os.system('python -m pip install html5lib')
	    os.chdir("..")
	    os.system('mv SiteBroker {}'.format(home))
	    if os.path.exists(f"{home}/SiteBroker"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def gathetool():
	if os.path.exists(f"{home}/GatheTOOL"):Installed_banner();print(f"O {am}GatheTOOL{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando GatheTOOL via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git php python -y')
	    os.system('python -m pip install requests')
	    os.system('git clone https://github.com/AngelSecurityTeam/GatheTOOL')
	    os.system('mv GatheTOOL {}'.format(home))
	    if os.path.exists(f"{home}/GatheTOOL"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def adbtk():
	if os.path.exists(f"{home}/ADB-Toolkit"):Installed_banner();print(f"O {am}ADB-Toolkit{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando ADB-Toolkit via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git -y')
	    os.system('git clone https://github.com/ASHWIN990/ADB-Toolkit')
	    os.system('mv ADB-Toolkit {}'.format(home))
	    if os.path.exists(f"{home}/ADB-Toolkit"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def tekdefense():
	if os.path.exists(f"{home}/TekDefense-Automater"):Installed_banner();print(f"O {am}TekDefense-Automater{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando TekDefense-Automater via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2 -y')
	    os.system('python2 -m pip install requests')
	    os.system('git clone https://github.com/1aN0rmus/TekDefense-Automater')
	    os.system('mv TekDefense-Automater {}'.format(home))
	    if os.path.exists(f"{home}/TekDefense-Automater"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def eagleeye():
	if os.path.exists(f"{home}/EagleEye"):Installed_banner();print(f"O {am}EagleEye{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando EagleEye via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python -y')
	    os.system('apt install pip -y')
	    os.system('pip install termcolor')
	    os.system('pip install selenium')
	    os.system('pip install requests_html')
	    os.system('pip install opencv-python')
	    os.system('git clone https://github.com/ThoughtfulDev/EagleEye')
	    os.system('mv EagleEye {}'.format(home))
	    if os.path.exists(f"{home}/EagleEye"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def eyewitness():
	if os.path.exists(f"{home}/EyeWitness"):Installed_banner();print(f"O {am}EyeWitness{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando EyeWitness via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python -y')
	    os.system('git clone https://github.com/FortyNorthSecurity/EyeWitness')
	    os.system('mv EyeWitness {}'.format(home))
	    if os.path.exists(f"{home}/EyeWitness"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    

def inspy():
	if os.path.exists(f"{home}/InSpy"):Installed_banner();print(f"O {am}InSpy{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando InSpy via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2 -y')
	    os.system('python2 -m pip install requests==2.20.1 BeautifulSoup==3.2.1')
	    os.system('git clone https://github.com/leapsecurity/InSpy')
	    os.system('mv InSpy {}'.format(home))
	    if os.path.exists(f"{home}/InSpy"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    
	    
def gasmask():
	if os.path.exists(f"{home}/gasmask"):Installed_banner();print(f"O {am}Gasmask{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando Gasmask via GIT...\n')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2 -y')
	    os.system('python2 -m pip install validators python-whois dnspython requests shodan censys')
	    os.system('git clone https://github.com/twelvesec/gasmask')
	    os.system('mv gasmask {}'.format(home))
	    if os.path.exists(f"{home}/gasmask"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    
	    
def sherlock():
	if os.path.exists(f"{home}/sherlock"):Installed_banner();print(f"O {am}Sherlock{ma} já está presente no diretório {am}{home}{ma}");timeout(1)
	else:
	    install_banner()
	    print(f'{vd}\n{bra}[{am}-{bra}] instalando Sherlock via GIT...\n')
	    os.system("apt update -y && apt upgrade -y")
	    os.system("apt install git -y")
	    os.system("apt install python -y")
	    os.system("git clone https://github.com/sherlock-project/sherlock.git")
	    os.system("mv sherlock {}".format(home))
	    if os.path.exists(f"{home}/sherlock"):
	        print(f"\n{bra}[{vd}✔{bra}] Instalação concluida.")
	    else:
	        print(f"\n{bra}[{vlh}!{bra}] Falha na Instalação.")
	    