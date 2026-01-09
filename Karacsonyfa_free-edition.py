import os
import random
from colorama import init, Fore
os.system('cls')
init(autoreset=True)

#Bemenet:

szint_szam = int(input('Mond meg a karácsonyfa szintjének számát (páratlan számot adj meg!): '))
díszek = input('Díszítés bekabcsolása (igen/nem):')

csillag = Fore.GREEN +'*'
dísz1 = csillag
dísz2 = csillag
dísz3 = csillag

if díszek == 'igen':                 # \033[38;5;SZÍN m SZÖVEG \033[0m
    dísz1 = '\033[38;5;203m' + input('Válassz egy ' + '\033[38;5;203mPiros\033[0m' + ' díszt: ' ) + '\033[0m'
    dísz2 = '\033[38;5;220m' + input('Válassz egy ' + '\033[38;5;220mSárga\033[0m' + ' díszt: ' ) + '\033[0m'
    dísz3 = '\033[38;5;45m' + input('Válassz egy ' + '\033[38;5;45mKék\033[0m' + ' díszt: ' ) + '\033[0m'


#Változók:


díszek_lista = [csillag, dísz1, dísz2, dísz3]
chances = [85, 5, 5, 5] #esélyek a díszekre
aktuális_csillag_szam = 0
közép = (szint_szam*2)//2-2
sor_lista = []


#listák, elemek:


for lista_szint in range(szint_szam*2-1): #fa hosszának a 2szöröse kell hogy legyen
    sor_lista.append(' ')
print(' '*(közép+1) + '\033[38;5;221m☆\033[0m')

#print(''.join(sor_lista).replace('*', '\033[38;5;221m☆\033[0m'))

#Függvények:



def aktuális_sor_lista ():
    global sor_lista
    global aktuális_csillag_szam
    global közép

    for i in range((közép+1)-aktuális_csillag_szam,(közép+1)+aktuális_csillag_szam+1):
        sor_lista[i] = random.choices(díszek_lista, weights=chances, k=1)[0]
    sor_kiírás = ''.join(sor_lista)
    print(sor_kiírás)
    #return sor_lista

#Old code:  -----> Unrandom seed
    #sor_lista[(közép+1)+aktuális_csillag_szam] = random.choices(díszek_lista, weights=chances, k=1)[0] #bal oldal
    #sor_lista[(közép+1)-aktuális_csillag_szam] = random.choices(díszek_lista, weights=chances, k=1)[0] #jobb oldal


#Rajzolás:


#aktuális_csillag_szam += 1
for loop in range(szint_szam-1):
    aktuális_csillag_szam += 1
    aktuális_sor_lista()



rönk = szint_szam // 8
for tönk in range(szint_szam//4):  #rönk hossz
    print(' '*(közép-rönk)  + f'\033[38;5;137m|\033[0m'+ ' ' + '  '*rönk+ f'\033[38;5;137m|\033[0m') #rönk vastagság









