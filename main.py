from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored

import os
import ctypes
from ctypes import wintypes
import msvcrt
import subprocess

from num2words import num2words

ctypes.windll.kernel32.SetConsoleTitleW("QWERTY Decryption - Jam - 2022")
os.system('mode con: cols=100 lines=40')
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
user32 = ctypes.WinDLL('user32', use_last_error=True)

SW_MAXIMIZE = 3

kernel32.GetConsoleWindow.restype = wintypes.HWND
kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)

def maximize_console(lines=None):
    fd = os.open('CONOUT$', os.O_RDWR)
    try:
        hCon = msvcrt.get_osfhandle(fd)
        max_size = kernel32.GetLargestConsoleWindowSize(hCon)
        if max_size.X == 0 and max_size.Y == 0:
            raise ctypes.WinError(ctypes.get_last_error())
    finally:
        os.close(fd)
    cols = max_size.X
    hWnd = kernel32.GetConsoleWindow()
    if cols and hWnd:
        if lines is None:
            lines = max_size.Y
        else:
            lines = max(min(lines, 9999), max_size.Y)
        subprocess.check_call('mode.com con cols={} lines={}'.format(
                                cols, lines))
        user32.ShowWindow(hWnd, SW_MAXIMIZE)

maximize_console(lines=None)

init(autoreset=True)

global r
global g
global b
global w
global y
global c
global m
global bl

r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
w = Fore.WHITE
y = Fore.YELLOW
c = Fore.CYAN
m = Fore.MAGENTA
bl = Fore.BLACK

global rbg
global gbg
global bbg
global wbg
global ybg
global cbg
global mbg

rbg = Back.RED
gbg = Back.GREEN
bbg = Back.BLUE
wbg = Back.WHITE
ybg = Back.YELLOW
cbg = Back.CYAN
mbg = Back.MAGENTA

global bright
global dim

bright = Style.BRIGHT
dim = Style.DIM

def p(t, color):
    text = color + t
    return text

def bg(t, color):
    text = color + t
    return text

def sty(t, level):
    text = level + t
    return text

def find_qwerty_value(letter):
    
    if letter == "Q":
        return "A"
    elif letter == "q":
        return "a"
    
    elif letter == "W":
        return "B"
    elif letter == "w":
        return "b"

    elif letter == "E":
        return "C"
    elif letter == "e":
        return "c"

    elif letter == "R":
        return "D"
    elif letter == "r":
        return "d"

    elif letter == "T":
        return "E"
    elif letter == "t":
        return "e"

    elif letter == "Y":
        return "F"
    elif letter == "y":
        return "f"

    elif letter == "U":
        return "G"
    elif letter == "u":
        return "g"

    elif letter == "I":
        return "H"
    elif letter == "i":
        return "h"

    elif letter == "O":
        return "I"
    elif letter == "o":
        return "i"

    elif letter == "P":
        return "J"
    elif letter == "p":
        return "j"

    elif letter == "A":
        return "K"
    elif letter == "a":
        return "k"

    elif letter == "S":
        return "L"
    elif letter == "s":
        return "l"

    elif letter == "D":
        return "M"
    elif letter == "d":
        return "m"

    elif letter == "F":
        return "N"
    elif letter == "f":
        return "n"

    elif letter == "G":
        return "O"
    elif letter == "g":
        return "o"

    elif letter == "H":
        return "P"
    elif letter == "h":
        return "p"

    elif letter == "J":
        return "Q"
    elif letter == "j":
        return "q"

    elif letter == "K":
        return "R"
    elif letter == "k":
        return "r"

    elif letter == "L":
        return "S"
    elif letter == "l":
        return "s"

    elif letter == "Z":
        return "T"
    elif letter == "z":
        return "t"

    elif letter == "X":
        return "U"
    elif letter == "x":
        return "u"

    elif letter == "C":
        return "V"
    elif letter == "c":
        return "v"

    elif letter == "V":
        return "W"
    elif letter == "v":
        return "w"

    elif letter == "B":
        return "X"
    elif letter == "b":
        return "x"

    elif letter == "N":
        return "Y"
    elif letter == "n":
        return "y"

    elif letter == "M":
        return "Z"
    elif letter == "m":
        return "z"
    
    else:
        return letter
    

def decrypt(phrase):

    new_phrase = ""

    for i in range(len(phrase)):
        
        letter = phrase[i]

        letter_value = find_qwerty_value(letter)

        new_phrase += letter_value

    print(p(" Decrypted: ", g) + fix + "| " + new_phrase)

fix = '\033[0m'

print("")
print(sty(p(" QWERTY Encryption | by Jam | 2022", g), bright))
print("")

def main():

    up = True

    while up:
        print("------------------------------------------------------------------------------------------------")
        phrase = input(p(" Phrase:   ", c) + fix + "| ")
        decrypt(phrase)

main()
