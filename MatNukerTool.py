# -*- coding: utf-8 -*-
#Made with love by Mat

### IMPORT ###
import os
import requests, os, sys, re, time, os.path, ctypes, getpass
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import Fore
from urllib.request import Request, urlopen
import nextcord

### COLORI E VAR ###
VERSIONETOOL = "0.0.1 [BETA]"
c = Fore.LIGHTCYAN_EX
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
m = Fore.LIGHTMAGENTA_EX


### SETUP DISCORD ###
import nextcord
from nextcord.errors import LoginFailure
from nextcord.ext import commands
from nextcord.utils import get
intents = nextcord.Intents.default()
intents.members = True
intents.guild_messages = True 
intents.messages = True
intents.guilds = True
#nuker = commands.Bot(command_prefix=";",intents=intents)

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

nuker = Bot()


global statobot
statobot = 'Offline'

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
#    print(f"""\n\n
#                ╭━╮╱╭┳╮╱╭┳╮╭━┳━━━┳━━━╮╭━━━━┳━━━┳━━━┳╮
#                ┃┃╰╮┃┃┃╱┃┃┃┃╭┫╭━━┫╭━╮┃┃╭╮╭╮┃╭━╮┃╭━╮┃┃
#                ┃╭╮╰╯┃┃╱┃┃╰╯╯┃╰━━┫╰━╯┃╰╯┃┃╰┫┃╱┃┃┃╱┃┃┃
#                ┃┃╰╮┃┃┃╱┃┃╭╮┃┃╭━━┫╭╮╭╯╱╱┃┃╱┃┃╱┃┃┃╱┃┃┃╱╭╮
#                ┃┃╱┃┃┃╰━╯┃┃┃╰┫╰━━┫┃┃╰╮╱╱┃┃╱┃╰━╯┃╰━╯┃╰━╯┃
#                ╰╯╱╰━┻━━━┻╯╰━┻━━━┻╯╰━╯╱╱╰╯╱╰━━━┻━━━┻━━━╯   
#\n""".replace('█', f'{g}█{y}'))
    print(f"""\n\n
                                 __  __       _       _   _       _               _______          _ 
                                |  \/  |     | |     | \ | |     | |             |__   __|        | |
                                | \  / | __ _| |_    |  \| |_   _| | _____ _ __     | | ___   ___ | |
                                | |\/| |/ _` | __|   | . ` | | | | |/ / _ \ '__|    | |/ _ \ / _ \| |
                                | |  | | (_| | |_    | |\  | |_| |   <  __/ |       | | (_) | (_) | |
                                |_|  |_|\__,_|\__|   |_| \_|\__,_|_|\_\___|_|       |_|\___/ \___/|_|
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
    caricamento()
    clear()

def caricamento():
	carattere = ['|', '/', '-', '\\']
	for i in carattere+carattere+carattere:
		sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Caricamento... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)

@nuker.event
async def on_ready():
    global statobot
    statobot = 'Online'
    print("Bot loggato:")
    print("ID: " + str(nuker.user.id))
    print("Nome: " + str(nuker.user.name))
    main()

from scripts import *
def main():
    impostatitolo(f"Mat Nuker Tool {VERSIONETOOL} - Caricamento")
    System.Size(160, 40) #120, 30
    Anime.Fade(Center.Center(banner), Colors.green_to_red, Colorate.Vertical, time=1)
    clear()
    try:
        filetoken = open("token.txt", "r")
        token = 'Trovato'
    except:
        token = 'Non Trovato'
    try:
        fileserver = open("server.txt", "r")
        server = fileserver.read()
    except:
        server = 'Non Trovato'
    global statobot
    impostatitolo(f"Mat Nuker Tool {VERSIONETOOL}")
    titolohome()
    print(f"""      {y}[{b}+{y}]{g} Main:                                                                            {y}[{b}+{y}]{c} Settings:
          {y}[{w}1{y}]{g} Banna tutti i membri                                                             {y}[{w}10{y}]{c} Imposta bot token
          {y}[{w}2{y}]{g} Elimina tutti i canali                                                           {y}[{w}11{y}]{c} Imposta il server da grieffare              
          {y}[{w}3{y}]{g} Elimina tutti i ruoli                                                            {y}[{w}12{y}]{c} Avvia bot 
          {y}[{w}4{y}]{g} Dai a @everyone l'amministratore
          {y}[{w}5{y}]{g} Crea canali
          {y}[{w}6{y}]{g} Modifica nome server
          {y}[{w}7{y}]{g} Elimina emoji server

                                                                                     {m}Made by Mat#3616 | github.com/itsmat
                                                                                     {m}Token     : {b}{token}
                                                                                     {m}Server    : {b}{server}
                                                                                     {m}Stato bot : {b}{statobot}
\t\t\t\t\t\t\t\t\t\t\t\t\t""")
    global scelta
    scelta = input(f"""{y}[{b}#{y}]{w} [{getpass.getuser()}]: """)
    if scelta == '1' or scelta == '01':
        if statobot == 'Online':
            try:
                fileserver = open("server.txt", "r")
                server = fileserver.read()
                serverr = nuker.get_guild(int(server))
                os.system('python3 ./scripts/1_BanAll.py')
            except FileNotFoundError:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Server ID mancante [tasto 11 nella home]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Avvia il bot [tasto 12 nella home]!")
            main()
    elif scelta == '2' or scelta == '02':
        if statobot == 'Online':
            try:
                fileserver = open("server.txt", "r")
                server = fileserver.read()
                serverr = nuker.get_guild(int(server))
                os.system('python3 ./scripts/2_EliminaCanali.py')
            except FileNotFoundError:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Server ID mancante [tasto 11 nella home]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Avvia il bot [tasto 12 nella home]!")
            main()
    elif scelta == '3' or scelta == '03':
        if statobot == 'Online':
            try:
                fileserver = open("server.txt", "r")
                server = fileserver.read()
                serverr = nuker.get_guild(int(server))
                os.system('python3 ./scripts/3_EliminaRuoli.py')
            except FileNotFoundError:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Server ID mancante [tasto 11 nella home]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Avvia il bot [tasto 12 nella home]!")
            main()
    elif scelta == '4' or scelta == '04':
        if statobot == 'Online':
            try:
                fileserver = open("server.txt", "r")
                server = fileserver.read()
                serverr = nuker.get_guild(int(server))
                os.system('python3 ./scripts/4_ModificaEveryone.py')
            except FileNotFoundError:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Server ID mancante [tasto 11 nella home]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Avvia il bot [tasto 12 nella home]!")
            main()
    elif scelta == '5' or scelta == '05':
        if statobot == 'Online':
            try:
                fileserver = open("server.txt", "r")
                server = fileserver.read()
                serverr = nuker.get_guild(int(server))
                os.system('python3 ./scripts/5_CreaCanali.py')
            except FileNotFoundError:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Server ID mancante [tasto 11 nella home]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Avvia il bot [tasto 12 nella home]!")
            main()
    elif scelta == '6' or scelta == '06':
        if statobot == 'Online':
            try:
                fileserver = open("server.txt", "r")
                server = fileserver.read()
                serverr = nuker.get_guild(int(server))
                os.system('python3 ./scripts/6_CambiaNomeServer.py')
            except FileNotFoundError:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Server ID mancante [tasto 11 nella home]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Avvia il bot [tasto 12 nella home]!")
            main()
    elif scelta == '7' or scelta == '07':
        if statobot == 'Online':
            try:
                fileserver = open("server.txt", "r")
                server = fileserver.read()
                serverr = nuker.get_guild(int(server))
                os.system('python3 ./scripts/7_EliminaEmoji.py')
            except FileNotFoundError:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Server ID mancante [tasto 11 nella home]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Avvia il bot [tasto 12 nella home]!")
            main()
    elif scelta == '10' or scelta == '010':
        transizione()
        diocane = input(f'{y}[{b}#{y}]{w} Inserisci il token del bot:    ')
        file = open(f"token.txt", 'w')
        file.write(f"{diocane}")
        file.close()
        main()
    elif scelta == '11' or scelta == '011':
        transizione()
        diocane = input(f'''{y}[{b}#{y}]{w} Inserisci l'id del server da nukkare:    ''')
        file = open(f"server.txt", 'w')
        file.write(f"{diocane}")
        file.close()
        main()
    elif scelta == '12' or scelta == '012':
        transizione()
        try:
            filetoken = open("token.txt", "r")
            token = filetoken.read()
            try:
                nuker.run(f'{token}')
            except LoginFailure:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Il token inserito non è valido!")
        except Exception as errore:
            print(errore)
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Devi prima impostare il token del bot e l'id del server!")
            main()
    elif scelta == 'exit' or scelta == 'chiudi':
        transizione()
        sys.exit()
    else:
        clear()
        main()




main()
