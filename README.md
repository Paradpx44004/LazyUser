# LazyUser

## In development

## Description
LazyUser is a tool that will make your daily life easier. Its goal is to assist you in installing and using various penetration testing and hacking tools on the *Android* system with ease. It allows users to easily install and use a variety of popular tools such as *Nmap, Gobuster, SQLMap, MetaSploit, Hash Identify, etc*. LazyUser is easy and straightforward to use, simply by typing a command to install and use any of the tools.
## Disclaimer
LazyUser was developed for the ethical audience; the tool can be very useful for ethical hacking discoveries and tasks.

## language used
![python](https://img.shields.io/badge/Python-3-faea11?labelColor=faea11&style=for-the-badge&logo=python&logoColor=000000&link=https://www.python.org/downloads)
![shell-script](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)

## Platforms:
![Debian](https://img.shields.io/badge/Debian-gnu?style=for-the-badge&logo=Debian&logoColor=%23ca1717ff&color=%23000000ff)
![Ubuntu](https://img.shields.io/badge/Ubuntu-gnu?style=for-the-badge&logo=Ubuntu&logoColor=%23c1600bff&color=%23000000ff)
![Static Badge](https://img.shields.io/badge/Kal_linux-gnu?style=for-the-badge&logo=Kali%20linux&color=%23000000ff)
![Termux](https://img.shields.io/badge/Termux-linux?style=for-the-badge&logo=android&logoColor=%23ffffffff&color=%23000000ff)
<img loading="lazy" src="src/parrotlogo.jpg" width="110" height="28"/>

## How to install?
#### automatic installation
```
curl -sL https://raw.githubusercontent.com/AstralSecHaxor/LazyUser/main/install.sh | bash
```
#### ou
```
apt-get update && apt-get upgrade
apt-get install python3 -y
apt-get install git -y
git clone https://github.com/AstralSecHaxor/LazyUser
cd LazyUser
python install.py
```
## execution commands
```
UserTool

usertool
```
If you are going to use • Termux
 Use these commands to avoid unexpected errors before running the script.
 
 #### Example:
```      
  termux-chroot
  unset LD_PRELOAD 
```