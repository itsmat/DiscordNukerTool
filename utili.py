import os, os.path
from colorama import Fore
import requests, os, sys, re, time, random, os.path, string, subprocess, random, threading, ctypes, shutil
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

VERSIONETOOL = "0.0.1 [BETA]"
c = Fore.LIGHTCYAN_EX
g = Fore.LIGHTGREEN_EX
r = Fore.LIGHTRED_EX
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
m = Fore.LIGHTMAGENTA_EX

### SCHERMATA ###
def impostatitolo(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | github.com/itsmat")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} | github.com/itsmat\x07")
    else:
        pass

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def titolohome():
    print(f"""\n\n
                ╭━╮╱╭┳╮╱╭┳╮╭━┳━━━┳━━━╮╭━━━━┳━━━┳━━━┳╮
                ┃┃╰╮┃┃┃╱┃┃┃┃╭┫╭━━┫╭━╮┃┃╭╮╭╮┃╭━╮┃╭━╮┃┃
                ┃╭╮╰╯┃┃╱┃┃╰╯╯┃╰━━┫╰━╯┃╰╯┃┃╰┫┃╱┃┃┃╱┃┃┃
                ┃┃╰╮┃┃┃╱┃┃╭╮┃┃╭━━┫╭╮╭╯╱╱┃┃╱┃┃╱┃┃┃╱┃┃┃╱╭╮
                ┃┃╱┃┃┃╰━╯┃┃┃╰┫╰━━┫┃┃╰╮╱╱┃┃╱┃╰━╯┃╰━╯┃╰━╯┃
                ╰╯╱╰━┻━━━┻╯╰━┻━━━┻╯╰━╯╱╱╰╯╱╰━━━┻━━━┻━━━╯   
\n""".replace('█', f'{g}█{y}'))

banner = r"""
░█████╗░░█████╗░██████╗░██╗░█████╗░░█████╗░███╗░░░███╗███████╗███╗░░██╗████████╗░█████╗░
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗████╗░████║██╔════╝████╗░██║╚══██╔══╝██╔══██╗
██║░░╚═╝███████║██████╔╝██║██║░░╚═╝███████║██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░██║░░██║
██║░░██╗██╔══██║██╔══██╗██║██║░░██╗██╔══██║██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░██║░░██║
╚█████╔╝██║░░██║██║░░██║██║╚█████╔╝██║░░██║██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░╚█████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░
"""[1:]

def transizione():
    clear()
    Spinner()
    clear()

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Caricamento... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)