import random
from pathlib import Path
import platform
import os
import time
from colorama import init, Fore, Style
import colorama
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-p","--path",dest="path",help="dosya yolu")
(options,args) = parser.parse_args()
colorama.init()

if not options.path:
    print(Fore.YELLOW+"Hata: Dosya yolu girin.")
    parser.print_help()
    exit()
init(autoreset=True)

print("[*] Gerekli Modüller Kontrol Ediliyor.....")
if platform.system().startswith("Linux"):
    try:
        from pystyle import *
    except ImportError:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *
elif platform.system().startswith("Windows"):
    try:
        from pystyle import *
    except ImportError:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *

def catc():
    try:
        if platform.system().startswith("Windows"):
            os.system('cls')
            check()
        else:
            os.system('clear')
            check()
    except KeyboardInterrupt:
        print()
        print(Fore.RED + "\n[*] Çıkış Tuşuna Bastınız!")
        quit()



def check():
    dosya_yolu = 'ith.py'
    path = Path(dosya_yolu)
    if path.is_file():
        print(Fore.RED + '[*] Şifrelenmiş Eski Dosya Zaten Var! Lütfen Kaldırın veya Yeniden Adlandırın...')
        print()
        print(Fore.YELLOW + "[1] Dosyayı Kaldırmak İçin: Yazın:- del\n[2] Dosyayı Yeniden Adlandırmak İçin: Yazın:- ren")
        print()
        a = input(Fore.BLUE + "[+] Eski Dosyayı Kaldırmak mı Yoksa Yeniden Adlandırmak mı İstiyorsunuz: ")
        print()

        if a == "del":
            os.remove('ith.py')
            time.sleep(2)
            print(Fore.GREEN + '[*] Dosya Başarıyla Silindi')
            print()
            enc()
        elif a == "ren":
            os.rename('ith.py', 'old_ith.py')
            time.sleep(2)
            print(Fore.GREEN + '[*] Dosya Başarıyla Yeniden Adlandırıldı')
            print()
            enc()
        else:
            print(Fore.RED + "Lütfen! Manuel Olarak Kaldırın veya Yeniden Adlandırın")
    else:
        enc()

def enc():
    try:
        from pyfiglet import Figlet
    except ImportError:
        os.system("python3 -m pip install pyfiglet")
    f = Figlet(font='slant')
    print(Fore.MAGENTA+f.renderText('IHT'))
    print(Fore.YELLOW+"                         Coded by @wqlsz")
    firstnum = options.path
    with open(firstnum) as f:
        içerik = f.read()
    string = içerik
    a = 0
    time.sleep(2)
    print()
    print(Fore.GREEN + "[*] Dosya Doğrulama Başarılı...")
    xnd = ""
    while a < 100:
        xnd = xnd + str(random.randint(0, 9))
        a += 1

    no_of_itr = len(string)
    output_string = ""
    for i in range(no_of_itr):
        current_string = string[i]
        current_key = xnd[i % len(xnd)]
        output_string += chr(ord(current_string) ^ ord(current_key))
    c = repr(output_string)
    time.sleep(2)
    print()

    print(Fore.MAGENTA + "[*] Dosya Şifreleme Başladı...")
    d = c.replace("'", "")
    time.sleep(2)
    print()
    print(Fore.BLUE + "[*] Şifreleme Anahtarı Oluşturuluyor...")
    try:
        with open('ith.py', 'w') as f:
            f.write(f"wopvEaTEcopFEavc =\"{d}\" \n")
            f.write(f"\niOpvEoeaaeavocp = \"{xnd}\"\n")
            f.write(
                "uocpEAtacovpe = len(wopvEaTEcopFEavc)\noIoeaTEAcvpae = \"\"\nfor fapcEaocva in range(uocpEAtacovpe):\n    nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[fapcEaocva]\n    qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[fapcEaocva % len(iOpvEoeaaeavocp)]\n    oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))\n\n\neval(compile(oIoeaTEAcvpae, '<string>', 'exec'))")
    except FileNotFoundError:
        print("")
    time.sleep(2)
    print()
    print(Fore.GREEN + "\n[+] Dosya Başarıyla Şifrelendi...")

catc()
