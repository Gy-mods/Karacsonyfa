import os
import random
import time
from colorama import init, Fore
os.system('cls')
init(autoreset=True)

#Bemenet:
print('Ez a Python Karacsonyfa project fizetős verziója köszönjük, hogy megvette! \n A program teljes értékű személyre szabást engedélyez, több információért letogasson el ide(https://github.com/Gy-mods/Karacsonyfa)\n A színpaletta megtekintéséhez pedig látogasson el erre a linkre (https://hexdocs.pm/color_palette/ansi_color_codes.html)\n Jó szórakozást!\n')
szint_szam = int(input('Mond meg a karácsonyfa szintjének számát: '))


díszek_be = input('Díszítés bekabcsolása (igen/nem):')

össz_dísz_száma = 0
csillag = Fore.GREEN +'*'
dísz1 = csillag
dísz2 = csillag
dísz3 = csillag
dísz_karakterek = []
dísz_chances = []
dísz_színek = []
dísz_pos = []
össz_dísz_száma = 0
def fg(n):      #Színek
    return f"\033[38;5;{n}m"    # \033[38;5;SZÍN m SZÖVEG \033[0m



if díszek_be == 'igen':
    össz_dísz_száma = int(input('Mennyi féle díszt szeretnél? '))
    for hanyadik_fajta_dísz in range(össz_dísz_száma):
        dísz_karakter = input('Add meg a kívánt karaktert a díszhez: ')
        dísz_szine = input('Dísz színe (a fenti linken megtalálható a színpaletta) 0-255: ')
        dísz_chance = input('A dísz valószínűsége (100-at ne haladja meg az össz valószínűség): ')

        dísz_karakterek.append(dísz_karakter)
        dísz_színek.append(fg(dísz_szine))
        dísz_chances.append(int(dísz_chance))
        dísz_pos.append([])

        #mindenből kereken ugyan annyi van pont kijön dízsek,dísz_chances

dísz_karakterek.append("*")
dísz_színek.append(Fore.GREEN)
dísz_chances.append(100-sum(dísz_chances))
dísz_pos.append([])
#print(dísz_karakterek, dísz_színek, dísz_chances)

os.system('cls')
print('\033[?25l')

#Változók:


#díszek_lista = [csillag, dísz1, dísz2, dísz3]   új változó --> díszek
#chances = [85, 5, 5, 5] #esélyek a díszekre    új változó --> dísz_chances
aktuális_csillag_szam = 0
közép = (szint_szam*2)//2-2
sor_lista = []
tick = 1








#listák, elemek:


for lista_szint in range(szint_szam*2-1): #fa hosszának a 2szöröse kell hogy legyen
    sor_lista.append(' ')
print(' '*(közép+1) + '\033[38;5;221m☆\033[0m')

#print(''.join(sor_lista).replace('*', '\033[38;5;221m☆\033[0m'))

#Függvények:


def move_cursor(row, col):      #Kurzor mozgatás
    print(f"\033[{row};{col}H", end="")


def aktuális_sor_lista ():      #Fő kód, sor elemeinek meghatározása
    global sor_lista
    global aktuális_csillag_szam
    global közép
    global loop_pos

    for oszlop_pos in range((közép+1)-aktuális_csillag_szam,(közép+1)+aktuális_csillag_szam+1):
        disz_index = random.choices(range(len(dísz_karakterek)), weights=dísz_chances, k=1)[0]  #randomizáló

        # if disz in [dísz1]: 
        #     dísz1pos.append([loop_pos,oszlop_pos])
        # if disz in [dísz2]: 
        #     dísz2pos.append([loop_pos,oszlop_pos])
        # if disz in [dísz3]: 
        #     dísz3pos.append([loop_pos,oszlop_pos])
        dísz_pos[disz_index].append([oszlop_pos,loop_pos])

        sor_lista[oszlop_pos] = dísz_színek[disz_index] + dísz_karakterek[disz_index]     # Dísz szín összerakás
    sor_kiírás = ''.join(sor_lista)
    print(sor_kiírás)
  


#Rajzolás:


    #aktuális_csillag_szam += 1
for loop_pos in range(szint_szam-1):
    aktuális_csillag_szam += 1
    aktuális_sor_lista()



rönk = szint_szam // 8
for tönk in range(szint_szam//4):  #rönk hossz
    print(' '*(közép-rönk)  + f'\033[38;5;137m|\033[0m'+ ' ' + '  '*rönk+ f'\033[38;5;137m|\033[0m') #rönk vastagság


#print(dísz_pos)
dísz_színek.pop() #zold csillag nem kell


#Újra rajzolás

for _ in range(9999):
    time.sleep(tick)
    dísz_színek = dísz_színek[1:] + dísz_színek[:1] # odebb forgatijuk a szineket eggyel
    for hanyadik_fajta_dísz in range(össz_dísz_száma):
        aktuális_dísz_pos = dísz_pos[hanyadik_fajta_dísz]
        for dísz_koordinata in aktuális_dísz_pos:
            move_cursor(dísz_koordinata[1]+3, dísz_koordinata[0]+1) #  y és x koordináta
            print(dísz_színek[hanyadik_fajta_dísz]+dísz_karakterek[hanyadik_fajta_dísz])
    



    
    




