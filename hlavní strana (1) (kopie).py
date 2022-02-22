import json
import os
import random
f = open('data.json')
data = json.load(f)
#Úvod hry
print("Vítejte u hry BlackJack.")
print("\nNejprve si prosím zvolte svou přezdívku. Máte možnost zadat jakékoliv znaky.")
#Vytvoření karet na hraní
hracovy_karty = []
dealerovy_karty = []
balicek = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += card
    return total
#karty hráče
def karty_zacatek():
    for i in range(2):
        random.shuffle(balicek)
        karta_2 = balicek.pop()
        if karta_2 == "J":
            karta_2 = 10
        if karta_2 == "Q":
            karta_2 = 10
        if karta_2 == "K":
            karta_2 = 10
        if karta_2 == "A":
            karta_2 = 10
        hracovy_karty.append(karta_2)
        print(karta_2)
def karta_random():
    for a in range(1):
        random.shuffle(balicek)
        karta_1 = balicek.pop()
        if karta_1 == "J":
            karta_1 = 10
        if karta_1 == "Q":
            karta_1 = 10
        if karta_1 == "K":
            karta_1 = 10
        if karta_1 == "A":
            karta_1 = 10
        hracovy_karty.append(karta_1)
        print(karta_1)
#karty dealera
def karty_zacatek_dealer():
    for i in range(2):
        random.shuffle(balicek)
        karta_2 = balicek.pop()
        if karta_2 == "J":
            karta_2 = 10
        if karta_2 == "Q":
            karta_2 = 10
        if karta_2 == "K":
            karta_2 = 10
        if karta_2 == "A":
            karta_2 = 10
        dealerovy_karty.append(karta_2)
        print(karta_2)
def karta_random_dealer():
    for a in range(1):
        random.shuffle(balicek)
        karta_1 = balicek.pop()
        if karta_1 == "J":
            karta_1 = 10
        if karta_1 == "Q":
            karta_1 = 10
        if karta_1 == "K":
            karta_1 = 10
        if karta_1 == "A":
            karta_1 = 10
        dealerovy_karty.append(karta_1)
        print(karta_1)
#Hlavní menu
def menu1(money, prezdivka):
    print("\nHrát novou hru- 1")
    print("Změna přezdívky- 2")
    print("Pravidla hry- 3")
    print("Ukončit hru- 4")

    menu = input("\nVaše volba: ")
    #Začátek hry
    if menu == str(1):
        hra(money, prezdivka)
    #Změna přezdívky
    elif menu == str(2):
        prezdivka1(money)
        menu1(money, prezdivka)
    #Pravidla
    elif menu == str(3):
        print("Pravidla hry BlackJack:")
        print("\nZáklad:")
        print("\nBlackjack je karetní hra často provozovaná v kasinu.",
              "\nOdlišná je především tím, že není jako většina hazardních her založena pouze na náhodě,",
              "\nale umožňuje pomocí různých strategií zvýšit pravděpodobnost výhry, především metoda",
              "\ntzv. počítání karet, kdy se hráč pokouší „zapamatovat“ tažené karty, má velkou publicitu.",
              "\nBlackjack se hraje s tzv. žolíkovými kartami.")
        print("\nCíl hry:")
        print("\nCílem hráče ve hře Black Jack je porazit krupiéra, a to tak,",
              "\nže bude mít vyšší součet karet než krupiér a současně nepřetáhne součet 21.",
              "\nNěkteří začátečníci se totiž mylně domnívají, že cílem při Black Jacku je dosáhnout součtu 21.",
              "\nNikoliv, je to jen nejvyšší (a tudíž velmi žádoucí) součet ve hře.",
              "\nHráč zkrátka musí mít víc než krupiér a nesmí přetáhnout.")
        print("\nPokud hráč součet 21 přetáhne – je tzv. „přes“",
              "\na prohrává vždy, bez ohledu na karty krupiéra. Jestliže součet 21 přetáhne krupiér,",
              "\nprohrává proti všem hráčům, kteří nepřetáhli. Dosáhne-li hráč stejného součtu jako krupiér,",
              "\njedná se o remízu a sázka se vrací.")
        print("\nBodování karet v Black Jacku se oproti Oko bere mírně liší.",
              "\nKarty 2 až 10 mají právě tu bodovou hodnotu, která je na kartě uvedena,",
              "\nzatímco Jack, Dáma a Král se počítají za 10 bodů.",
              "\nEso (A – Ace) může být počítáno za 1 bod nebo 11 bodů dle vlastního uvážení.",
              "\nOproti Oko bere se u hry Black Jack vyskytují také dva terminologické výrazy: měkký a tvrdý součet.",
              "\nPokud hráč počítá eso za 11 bodů, nazývá součet jako měkký, protože s přibráním další karty hráč nemůže přetáhnout 21;",
              "\nv opačném případě je součet označován jako tvrdý. Jako Black Jack je označována kombinace esa s desítkou nebo",
              "\njakoukoliv obrázkovou kartu (J, Q, K), barva nehraje žádnou roli.")
        print("\nRozdání karet a průběh hry:")
        print("\nPoté, co hráči umístí sázky před sebe na vyznačená pole, krupiér rozdá každému hráči i sobě,",
              "\nz jeho pohledu ve směru hodinových ručiček, nejprve jednu kartu a hráčům následně ve stejném pořadí ještě druhou kartu.",
              "\nVšechny karty jsou rozdávány lícem nahoru, tj. viditelně pro všechny hráče, krupiéra i přihlížející.")
        print(
            "\nNásledně se krupiér, ve stejném pořadí, v jakém byly rozdány karty, hráčů ptá, jak mají v úmyslu se svými kartami a sázkami naložit",
            "\na oznamuje rovněž výsledný součet karet.",
            "\nKrupiér provádí pokyny hráče, dokud se hráč nerozhodne stát nebo nepřetáhne.",
            "\nPřetáhne-li, jeho sázka je okamžitě sebrána.")
        print("\nJakmile krupiér takto obslouží všechny hráče, rozdá si druhou.",
              "\nPoté sebere prohrávající sázky, vyplatí vyhrávající sázky a vrátí sázky remízové.")
        print("\nTahy krupiéra a hráče:")
        print("\nPokud je součet karet krupiéra menší nebo roven 16, musí přibrat další karty,",
              "\npokud je součet vyšší nebo roven 17, musí zůstat stát.",
              "\nHráč má možnost vzít si další kartu nebo zůstat stát.")
        print("\nPřejeme hodně štěstí a zdaru ve hře!!!")
        menu1(money, prezdivka)
    #Konec hry
    elif menu == str(4):
        print("\nDěkujeme za vyzkoušení!!!")
        print("\nUkončuji program")
        quit()
    #Jiná možnost
    else:
        print("\nNeplatný znak!!!")
        menu1(money, prezdivka)
#Funkce na lízání karet
def karty_lizani(ztrata, vyhra, money, prezdivka):
    print("\nChcete dolíznout další kartu?")
    print("\nANO- 1")
    print("NE- 2")
    volba_karty = input("\nVaše volba->")
    #Volby hráče na líznutí či stání
    if volba_karty == str(1):
        print("\nDolízli jste si:")
        karta_random()
        if total(hracovy_karty) == 21:
            print("BlackJack, vyhráli jste!!!")
            money = vyhra
            print("Máte:", money, "KČ")
            menu1(money, prezdivka)
        elif total(hracovy_karty) > 21:
            print("\nBohužel jste prohráli!!!")
            money = ztrata
            print("Máte:", money, "KČ")
            menu1(money, prezdivka)
        else:
            karty_lizani(ztrata, vyhra, money, prezdivka)
    elif volba_karty == str(2):
        print("Dealerovy karty jsou:")
        karty_zacatek_dealer()
        if total(dealerovy_karty) == 21:
            print("BlackJack, prohráli jste!!!")
            money = ztrata
            print("Máte:", money, "KČ")
            menu1(money, prezdivka)
        elif total(dealerovy_karty) < 17:
            print("\nDealerova dolíznutá karta je:")
            karta_random_dealer()
            while total(dealerovy_karty) < 17:
                karta_random_dealer()
            if total(dealerovy_karty) < 21:
                if total(hracovy_karty) > total(dealerovy_karty):
                    print("\nVyhráli jste!!!")
                    money = vyhra
                    print("Máte:", money, "KČ")
                    menu1(money, prezdivka)
                elif total(hracovy_karty) < total(dealerovy_karty):
                    print("\nBohužel jste prohráli!!!")
                    money = ztrata
                    print("Máte:", money, "KČ")
                    menu1(money, prezdivka)
                elif total(hracovy_karty) == total(dealerovy_karty):
                    print("\nVyhráli jste, hodnota vašich karet byla stejná!!!")
                    money = vyhra
                    print("Máte:", money, "KČ")
                    menu1(money, prezdivka)
            elif total(dealerovy_karty) == 21:
                print("\nBlackJack, bohužel jste prohráli!!!")
                money = ztrata
                print("Máte:", money, "KČ")
                menu1(money, prezdivka)
            elif total(dealerovy_karty) > 21:
                print("\nVyhráli jste!!!")
                money = vyhra
                print("Máte:", money, "KČ")
                menu1(money, prezdivka)
        elif total(dealerovy_karty) >= 17:
            if total(hracovy_karty) > total(dealerovy_karty):
                print("\nVyhráli jste!!!")
                money = vyhra
                print("Máte:", money, "KČ")
                menu1(money, prezdivka)
            elif total(hracovy_karty) < total(dealerovy_karty):
                print("\nBohužel jste prohráli!!!")
                money = ztrata
                print("Máte:", money, "KČ")
                menu1(money, prezdivka)
            elif total(hracovy_karty) == total(dealerovy_karty):
                print("\nVyhráli jste, hodnota vašich karet byla stejná!!!")
                money = vyhra
                print("Máte:", money, "KČ")
                menu1(money, prezdivka)
    else:
        print("\nNeplatný znak!!!")
        karty_lizani(ztrata, vyhra, money, prezdivka)
#Funkce sázky
def hra(money, prezdivka):
    while True:
        print("\nAktuálně máte:", money, "KČ")
        sazka = input("\nKolik chcete vsadit?")
        # Podmínky sázky
        if sazka.isnumeric():
            if int(sazka) == int(0):
                print("\nMusíte něco vsadit!!!")
                continue
            elif int(sazka) <= money:
                ztrata = money - int(sazka)
                vyhra = money + int(sazka)
                print("\nVsadili jste:", sazka, "KČ")
                #Průběh hry
                print("\nVaše karty jsou: ")
                karty_zacatek()
                if total(hracovy_karty) == 21:
                    print("BlackJack, vyhráli jste!!!")
                    money = vyhra
                    print("Máte:", money, "KČ")
                    menu1(money, prezdivka)
                else:
                    karty_lizani(ztrata, vyhra, money, prezdivka)
                break
            else:
                print("\nNemůžete vsadit více peněz než máte!!!")
                continue
        else:
            print("\nNeplatný znak!!!")
            continue
#Funkce na přezdívky
def prezdivka1(hra):
    prezdivka = input("\nVaše přezdívka:")
    if len(prezdivka) == 0:
        print("\nMusí být zadán alespoň 1 znak!!!")
        prezdivka1(hra)
    elif len(prezdivka) > 15:
        print("\nPřezdívka nesmí obsahovat více než 20 znaků")
        prezdivka1(hra)
    elif len(prezdivka) <= 15:
        for attrs in data:
            if attrs['name'] == prezdivka:
                name = attrs['name']
                money = attrs['penize']
                stats = attrs['pocet_her']
                userData = {"name": name, "money": money, "stats": stats}
                print("\nVítejte uživateli:", prezdivka)
                menu1(money, prezdivka)
                break
            else:
                print("Uživatel nebyl nalezen. Chcete vytvořit nového uživatele ? Y/N")
                while True:
                    vytvorit = input("Y/N ->")
                    if (vytvorit == "Y" or vytvorit == "y"):
                        aDict = {"name": prezdivka, "penize": 1000, "pocet_her": 0}
                        fw = open("data.json", "w")
                        jsonString = json.dumps(aDict)
                        data.append(aDict)
                        fw.write(json.dumps(data))
                        for attrs in data:
                            if attrs['name'] == prezdivka:
                                name = attrs['name']
                                money = attrs['penize']
                                stats = attrs['pocet_her']
                                userData = {"name": name, "money": money, "stats": stats}
                                print("\nZe začátku máte: ", money, "KČ")
                                menu1(money, prezdivka)
                                break
                    elif (vytvorit == "n" or vytvorit == "N"):
                        print("\nUkončuji program")
                        quit()
                    else:
                        continue
prezdivka1(hra)
#Konečné volání funkce
menu1()

