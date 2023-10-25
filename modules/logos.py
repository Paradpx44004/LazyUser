"""
SCRIPT RESPONSÁVEL PELA OS BANNERS
"""
from time import sleep as timeout
import os, sys, time
import urllib.request
from subprocess import check_output as inputstream
import platform as mode
import subprocess

# Defina códigos de escape ANSI para cores
vd = "\33[1;36m" # Ciano
vlh = "\33[1;31m" # vermelho 
bra = "\33[1;37m" # branco
az = '\033[34m' # Azul
ma = '\033[35m' # Magento
am = '\033[33m' # Amarelo 

## Função de verificação do istema
def verificar_sistema():
    system_info = os.popen("uname -o").read().strip()
    if "Android" in system_info:
        return "Termux"
    elif os.path.exists('/etc/os-release'):
        with open('/etc/os-release', 'r') as os_release_file:
            lines = os_release_file.readlines()
            for line in lines:
                if line.startswith('ID='):
                    distro_id = line.split('=')[1].strip().strip('"')
                    if distro_id.lower() == 'ubuntu':
                        return "Ubuntu"
                    elif distro_id.lower() == 'debian':
                        return "Debian"
                    elif distro_id.lower() == 'kali':
                        return "Kali"
    return "LazyUser"
sistema_atual = verificar_sistema()

# Função para identificar ser sistema e linux
def identificar_sistema():
    sistema = mode.system()
    if sistema == "Linux":
        os.system("clear")
        return "Linux"
    else:
        print(f"{vlh}Ferramenta não projetada para esse sistema operacional{bra}")
        sys.exit()

# Função para identificar a arquitetura do dispositivo
def identificar_arquitetura():
    arquitetura = mode.architecture()[0]
    return arquitetura

# Função principal
def banner_inicial():
    os.system("clear")
    sistema = identificar_sistema()
    arquitetura = identificar_arquitetura()
    ## banner de apresentação das categorias
    print(f"""
{vd} ▄{vlh}█          ▄████████  ▄███████▄  ▄██   ▄
{vd}███  {vlh}       ███    ███ ██▀     ▄██ ███   ██▄
{vd}███     {vlh}    ███    ███       ▄███▀ ███▄▄▄███
{vd}███         {vlh}███    ███  ▀█▀▄███▀▄▄ ▀▀▀▀▀▀███
{vd}███       ▀████{vlh}███████   ▄███▀   ▀ ▄██   ███
{vd}███         ███    ███{vlh} ▄███▀       ███   ███
{vd}███▌    ▄   ███    ███ ██{vlh}█▄     ▄█ ███   ███
{vd}█████▄▄██   ███    █▀   ▀███{vlh}█████▀  ▀█████▀
{bra}               .::[ By: AstralSec{vlh}Haxor ]::.                              
{vd}               ███    █▄     ▄██████{vlh}██    ▄████████    ▄████████ 
{vd}               ███    ███   ███    ███   {vlh}███    ███   ███    ███ 
{vd}               ███    ███   ███    █▀    ███ {vlh}   █▀    ███    ███ 
{vd}               ███    ███   ███         ▄███▄▄▄ {vlh}     ▄███▄▄▄▄██▀ 
{vd}               ███    ███ ▀███████████ ▀▀███▀▀▀     {vlh}▀▀███▀▀▀▀▀   
{vd}               ███    ███          ███   ███    █▄  ▀███{vlh}████████ 
{vd}               ███    ███    ▄█    ███   ███    ███   ███  {vlh}  ███ 
{vd}               ████████▀   ▄████████▀    ██████████   ███    {vlh}███ 
{bra}   {am}Selecione categoria da sua ferramenta preferida :) {vd}███    {vlh}███
{bra}     _________________________________________________{vd}███{bra}____{vd}█{vlh}██
{bra}    /                                                 {vd}███    ██{vlh}█
{bra}    |[ 01 ] Coletar de Informações                           |
    |                                                         |
    |[ 02 ] Análise de Vulnerabilidades                      |
    |                                                         |
    |[ 03 ] Web Hacking                                      |
    |                                                         |
    |[ 04 ] Avaliações de Banco de Dados                     |
    |                                                         |
    |[ 05 ] Ataques de Senha                                 |
    |                                                         |
    |[ 06 ] Ataques Sem Fio                                  |
    |                                                         |
    |[ 07 ] Engenharia Reversa                               |
    |                                                         |
    |[ 08 ] Ferramentas de Exploração                        |
    |                                                         |
    |[ 09 ] Sniffing e Spoofing                              |
    |                                                         |
    |[ 10 ] Ferramentas de Relatórios                        |
    |                                                         |
    |[ 11 ] Ferramentas de Forenses                          |
    |                                                         |
    |[ 12 ] Teste de Estresse                                |
    |                                                         |
    |[ 13 ] Instalar Distribuições Linux                     |
    |                                                         |
    |[ 14 ] Utilitário Termux                                |
    |                                                         |
    |[ 15 ] Análise de Malware                               |
    |                                                         |
    |[ 16 ] Ferramentas de Engenharia Social                 |
    |                                                         |
    |                                                        |
    |                                                         |
    |                                                        |
    |                                                         |
    |                                                        |
    |                                                         |
    |                                                        |
    |                                 [ {am}38{bra} ] Tool Disponível  |
    |[ 00 ] ~> Sair da LazyUser    __________________________/
    \_____________________________/{bra}Arquitetura:{az} {arquitetura} {bra}-{az} {mode.machine()}

""")

if __name__ == "__main__":
    banner_inicial()


def banner(): ## banner de apresentação do menu de opções do tool
    os.system("clear")
    print(f"""
{vd} █{vlh}████
{vd}░░██{vlh}█
{vd} ░███ {vlh}        ██████    █████████ █████ ████
{vd} ░███   {vlh}     ░░░░░███  ░█░░░░███ ░░███ ░███
{vd} ░███       {vlh}  ███████  ░   ███░   ░███ ░███
{vd} ░███      █ █{vlh}██░░███    ███░   █ ░███ ░███
{vd} ███████████░░██{vlh}██████  █████████ ░░███████
{vd}░░░░░░░░░░░  ░░░░░{vlh}░░░  ░░░░░░░░░   ░░░░░███
{vd}                    {vlh}     ░░░░░     ███ ░███
{vd}                      {vlh}   ░         ░░██████   
{bra}      .::[ By: AstralSec{vlh}Haxor ]::. ░░░░░░
{vd}            ███    █▄     {vlh}▄████████░░░████████    ▄████████ 
{vd}            ███    ███   ███{vlh}    ███░░ ███    ███   ███    ███ 
{vd}            ███    ███   ███   {vlh} █▀ ░  ███    █▀    ███    ███ 
{vd}            ███    ███   ███      {vlh}   ▄███▄▄▄      ▄███▄▄▄▄██▀ 
{vd}            ███    ███ ▀███████████ {vlh}▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
{vd}            ███    ███          ███   █{vlh}██    █▄  ▀███████████ 
{vd}            ███    ███    ▄█    ███   ███ {vlh}   ███   ███    ███ 
{vd}            ████████▀   ▄████████▀    ████████{vlh}██   ███    ███ 
    {am}Escolha a opção da sua ferramenta preferida :) {vd}█{vlh}██    ███
{bra}___________________________________________________{vd}███{vlh}{bra}____{vlh}███{bra}___________________
                                                   {vd}███  {vlh}  ███{bra}""")

    ## banner de instalação das ferramentas.
def install_banner():
    os.system("clear")
    print(f"""{ma}
.------------------------------------------------------------------------.
 )                                                                      (
(    {vd}       ___           _        _                 _           {ma}        )
 )   {vd}      |_ _|_ __  ___| |_ __ _| | __ _ _ __   __| | ___      {ma}       (
(    {vd}       | || '_ \/ __| __/ _` | |/ _` | '_ \ / _` |/ _ \     {ma}        )
 )   {vd}       | || | | \__ \ || (_| | | (_| | | | | (_| | (_) |    {ma}       (
(    {vd}      |___|_| |_|___/\__\__,_|_|\__,_|_| |_|\__,_|\___/ ••• {ma}        )
 )   {vd}                                                            {ma}       (
'------------------------------------------------------------------------'""")

    ## banner de verificação ser a ferramenta já existente em algum diretório.
def Installed_banner(): 
    os.system("clear")
    print(f"""{vd}
.___________________________________________________________________________.
 )_{vlh}oooo{vd}_________________{vlh}oo{vd}____________{vlh}ooo{vd}________________{vlh}oo{vd}____________{vlh}oo{vd}__(
(___{vlh}oo{vd}__{vlh}oo{vd}_{vlh}ooo{vd}___{vlh}oooo{vd}___{vlh}oo{vd}_____{vlh}ooooo{vd}___{vlh}oo{vd}____{vlh}ooooo{vd}___{vlh}oooooo{vd}__{vlh}ooooo{vd}_____{vlh}oo{vd}___)
 )__{vlh}oo{vd}__{vlh}ooo{vd}___{vlh}o{vd}_{vlh}oo{vd}___{vlh}o{vd}_{vlh}oooo{vd}___{vlh}oo{vd}___{vlh}oo{vd}__{vlh}oo{vd}___{vlh}oo{vd}___{vlh}oo{vd}_{vlh}oo{vd}___{vlh}oo{vd}_{vlh}oo{vd}___{vlh}oo{vd}____{vlh}oo{vd}__(
(___{vlh}oo{vd}__{vlh}oo{vd}____{vlh}o{vd}___{vlh}oo{vd}____{vlh}oo{vd}____{vlh}oo{vd}___{vlh}oo{vd}__{vlh}oo{vd}___{vlh}oo{vd}___{vlh}oo{vd}_{vlh}oo{vd}___{vlh}oo{vd}_{vlh}oo{vd}___{vlh}oo{vd}____{vlh}oo{vd}___)
 )__{vlh}oo{vd}__{vlh}oo{vd}____{vlh}o{vd}_{vlh}o{vd}___{vlh}oo{vd}__{vlh}oo{vd}__{vlh}o{vd}_{vlh}oo{vd}___{vlh}oo{vd}__{vlh}oo{vd}___{vlh}oo{vd}___{vlh}oo{vd}_{vlh}oo{vd}___{vlh}oo{vd}_{vlh}oo{vd}___{vlh}oo{vd}________(
(__{vlh}oooo{vd}_{vlh}oo{vd}____{vlh}o{vd}__{vlh}oooo{vd}____{vlh}ooo{vd}___{vlh}oooo{vd}_{vlh}o{vd}_{vlh}ooooo{vd}__{vlh}oooo{vd}_{vlh}o{vd}__{vlh}oooooo{vd}__{vlh}ooooo{vd}_____{vlh}oo{vd}___)
 )_____________________________________________________________________{vlh}oo{vd}__(
(___________________________________________________________________________)
""")


# BANNERS DE OPÇÕES DE NAVEGAR PELO SCRIPT
def backmenu(): ## menu de opções para voltar ao menu  anterior ou sair 
    print(f"""
    {bra}[ {vlh}00 {bra}] ~> {vd}Sair da LazyUser.
    {bra}[ {vlh}enter {bra}] ~> {vd}Voltar ao menu anterior.
 """)
 
def backmenu_inicial(): ## menu de opções para voltar ao menu inicial ou sair
    print(f"""{bra}
   [ {vlh}00 {bra}] ~> {vd}Sair da LazyUser.{bra}
   [ {vlh}enter {bra}] ~> {vd}Voltar ao menu Inicial.{bra}
   [ {vlh}multi install{bra} ] ~> {vd}Faça uma sequência de opções separadas por vírgulas.
      {am}Ex{bra}: 3,23,6,19
""")

def sair_do_programar(): ## Sair do script
    print(f"\n\n{vd}Você saiu da LazyUser !{bra}\n")
    sys.exit()
    
def banner_coletar_informacoes():
    banner()
    print(f"""{vlh}┏━━{bra}[ {vlh}Requer Privilégio #Root{bra} ]{vlh}
{vlh}┃
{vlh}┃
{vlh}┃{bra}[ 01 ] Nmap: Utilitário para descoberta de rede e auditoria de segurança.
{vlh}┃{bra}[ 02 ] Red Hawk: Coleta de informações, verificação de vulnerabilidades e rastreamento.
{vlh}┃{bra}[ 03 ] D-TECT: Ferramenta multifuncional para testes de penetração.
{vlh}┃{bra}[ 04 ] sqlmap: Ferramenta automática de injeção SQL e controle de banco de dados.
{vlh}┃{bra}[ 05 ] ReconDog: Ferramenta de coleta de informações e verificação de vulnerabilidades.
{vlh}┃{bra}[ 06 ] AndroZenmap: ?
{vlh}┃{bra}[ 07 ] sqlmate: Um amigo do SQLmap que fará o que você sempre esperou do SQLmap.
{vlh}┃{bra}[ 08 ] AstraNmap: Verificador de segurança usado para localizar hosts e serviços em uma rede de computadores.
{vlh}┃{bra}[ 09 ] MapEye: Rastreador de localização GPS preciso Android, IOS, Windows phones.
{vlh}┃{bra}[ 10 ] Easymap: Atalho do Nmap.
{vlh}┃{bra}[ 11 ] Crips: Esta ferramenta é uma coleção de ferramentas IP on-line que podem ser usadas para obter rapidamente informações sobre endereços IP, páginas da Web e registros DNS.
{vlh}┃{bra}[ 12 ] EvilURL: Gere domínios malignos unicode para ataque homógrafo de IDN e detecte-os.
{vlh}┃{bra}[ 13 ] Striker: Conjunto de verificação de reconhecimento e vulnerabilidade.
{vlh}┃{bra}[ 14 ] Xshell: Conjunto de ferramentas (ToolKit).
{vlh}┃{bra}[ 15 ] OWScan: Verificador da Web OVID.
{vlh}┃{bra}[ 16 ] OSIF: Informações de código aberto Facebook.
{vlh}┃{bra}[ 17 ] Namechk: Ferramenta OSINT baseada em namechk.com para verificar nomes de usuários em mais de 100 sites, fóruns e redes sociais.
{vlh}┃{bra}[ 18 ] AUXILE: Estrutura de análise de aplicativos da Web.
{vlh}┃{bra}[ 19 ] inther: Coleta de informações usando shodan, censys e hackertarget.
{vlh}┃{bra}[ 20 ] GINF: Ferramenta de coleta de informações do GitHub.
{vlh}┃{bra}[ 21 ] ASU: Kit de ferramentas para hackear o Facebook.
{vlh}┃{bra}[ 22 ] Fim: Downloader de imagens do Facebook.
{vlh}┃{bra}[ 23 ] PwnedOrNot: Ferramenta OSINT para encontrar senhas de contas de e-mail comprometidas.
{vlh}┃{bra}[ 24 ] DNSRecon: Avaliação de segurança e solução de problemas de rede.
{vlh}┃{bra}[ 25 ] Zphisher: Ferramenta automatizada de phishing.
{vlh}┃{bra}[ 26 ] Mr.SIP: Ferramenta de auditoria e ataque baseada em SIP.
{vlh}┃{bra}[ 27 ] UserRecon: Encontre nomes de usuário em mais de 75 redes sociais.
{vlh}┃{bra}[ 28 ] PhoneInfoga: Uma das ferramentas mais avançadas para escanear números de telefone usando apenas recursos gratuitos.
{vlh}┃{bra}[ 29 ] SiteBroker: Um utilitário multiplataforma baseado em python para coleta de informações e automação de testes de penetração.
{vlh}┃{bra}[ 30 ] GatheTOOL: Coleta de informações - API hackertarget.com
{vlh}┃{bra}[ 31 ] ADB-ToolKit: ?
{vlh}┃{bra}[ 32 ] TekDefense-Automater: Automater - URL IP e análise MD5 OSINT.
{vlh}┃{bra}[ 33 ] EagleEye: Persiga seus amigos. Encontre seus perfis do Instagram, FB e Twitter usando reconhecimento de imagens e pesquisa reversa de imagens.
{vlh}┃{bra}[ 34 ] EyeWitness: EyeWitness foi projetado para fazer capturas de tela de sites, fornecer algumas informações de cabeçalho do servidor e identificar credenciais padrão, se possível.
{vlh}┃{bra}[ 35 ] InSpy: Uma ferramenta de enumeração do LinkedIn baseada em python.
{vlh}┃{bra}[ 36 ] Fierce: Uma ferramenta de reconhecimento de DNS para localizar espaço IP não contíguo.
{vlh}┃{bra}[ 37 ] Gasmask: Ferramenta de coleta de informações - OSINT.
{vlh}┃{bra}[ 38 ] SherLock: Sherlock é uma ferramenta de código aberto que ajuda a rastrear perfis de mídia social e presença online de indivíduos, facilitando a coleta de informações públicas.
{vlh}┗[]{bra}
""")
    backmenu_inicial()
    
def banner_analise_vulnevabilidade():
    banner()
    print(f"""{vlh}┏━━{bra}[ {vlh}Requer Privilégio #Root{bra} ]{vlh}
┃
┃
┃{bra}[ 01 ] SQLiv: scanner massivo de vulnerabilidade de injeção SQL.
{vlh}┃{bra}[ 02 ] sqlscan: Scanner SQL rápido, Dorker, injetor Webshell PHP.
{vlh}┃{bra}[ 03 ] Wordresscan: PScan rewritten in Python + some WPSeku ideas.
{vlh}┃{bra}[ 04 ] WPScan: Scanner de segurança WordPress gratuito.
{vlh}┃{bra}[ 05 ] termux-wordpresscan: ?
{vlh}┃{bra}[ 06 ] TM-scanner: scanner de vulnerabilidade de sites para termux.
{vlh}┃{bra}[ 07 ] Rang3r: Scanner IP + Porta Multi Thread.
{vlh}┃{bra}[ 08 ] Routersploit: Estrutura de exploração para dispositivos incorporados.
{vlh}┃{bra}[ 09 ] SH33LL: Shell Scanner.
{vlh}┃{bra}[ 10 ] XPL-SEARCH: Pesquise exploits em vários bancos de dados de exploits.
{vlh}┃{bra}[ 11 ] AndroBugs_Framework: Um scanner de vulnerabilidades Android eficiente que ajuda desenvolvedores ou hackers a encontrar possíveis vulnerabilidades de segurança em aplicativos Android.
{vlh}┃{bra}[ 12 ] Clickjacking-Tester: Um script em python projetado para verificar se o site é vulnerável a clickjacking e criar um poc.
{vlh}┗[{bra} 13 {vlh}]{bra} Sn1per: Plataforma de gerenciamento de superfície de ataque | Sn1perSecurity LLC.
""")
    backmenu_inicial()




def ferramentas_engenharia_social():
    banner()
    print("""
[ 01 ] DataSocial: Coleta informações de redes sociais por meio de páginas modificadas usando a técnica de phishing com engenharia social.
    """)
    backmenu_inicial()


## {vlh}┣{vlh}