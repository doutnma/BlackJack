import random
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
#Funkce na přezdívky
def prezdivka1():
    prezdivka = input("\nVaše přezdívka:")
    print("\nVaše přezdívka byla nastavena na: ", prezdivka)
prezdivka1()
def karty_lizani():
    print("\nChcete dolíznout další kartu?")
    print("\nANO- 1")
    print("NE- 2")
    volba_karty = input("\nVaše volba->")
    if volba_karty == str(1):
        print("Dolízli jste si:")
        karta_random()
        print("Hodnota vašich karet je ", total(hracovy_karty))
        if total(hracovy_karty) == 21:
            print("Vyhráli jste!!!")
            menu1()
        elif total(hracovy_karty) > 21:
            print("\nBohužel jste prohráli!!!")
            menu1()
        else:
            karty_lizani()
    elif volba_karty == str(2):
        print("Dealerovy karty jsou:")
        karty_zacatek_dealer()
        if total(dealerovy_karty) == 21:
            print("Prohráli jste!!!")
            menu1()
        elif total(dealerovy_karty) < 17:
            print("Dealerova dolíznutá karta byla:")
            karta_random_dealer()
            if total(dealerovy_karty) < 17:
                karta_random_dealer()
            else:
                if total(hracovy_karty) > total(dealerovy_karty):
                    print("Vyhráli jste!!!")
                    menu1()
                elif total(hracovy_karty) < total(dealerovy_karty):
                    print("Bohužel jste prohráli!!!")
                    menu1()
                elif total(hracovy_karty) == total(dealerovy_karty):
                    print("Vyhráli jste, hodnota vašich karet byla stejná")
                    menu1()
    else:
        print("\nNeplatný znak!!!")
        karty_lizani()
def hra():
    print("\nZačněmě:")
    #Sázka
    castka_zacatek = 1000
    print("\nZe začátku máte 1000KČ")
    while True:
        sazka = input("\nKolik chcete vsadit?")
        # Podmínky sázky
        zbyle_penize = castka_zacatek - int(sazka)
        if sazka.isnumeric():
            if int(sazka) == int(0):
                print("\nMusíte něco vsadit!!!")
                continue
            elif int(sazka) <= castka_zacatek:
                print("\nVsadili jste:", sazka, "KČ")
                print("\n Hra začíná!!!")
                #Průběh hry
                print("\nVaše karty jsou: ")
                karty_zacatek()
                print("Hodnota vašich karet je ", total(hracovy_karty))
                if total(hracovy_karty) == 21:
                    print("Vyhráli jste!!!")
                    menu1()
                else:
                    karty_lizani()
                break
            else:
                print("\nNemůžete vsadit více peněz než máte!!!")
                continue
        else:
            print("\nNeplatný znak!!!")
            continue
#Hlavní menu
def menu1():
    print("\nHrát novou hru- 1")
    print("Změna přezdívky- 2")
    print("Žebříček- 3")
    print("Pravidla hry- 4")
    print("Ukončit hru- 5")

    menu = input("\nVaše volba: ")
    #Začátek hry
    if menu == str(1):
        hra()
    #Změna přezdívky
    elif menu == str(2):
        prezdivka1()
        menu1()
    #Pravidla
    elif menu == str(4):
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
            "\na oznamuje rovněž výsledný součet karet. Na rozdíl od Oko bere není rozhodnutí hráčů zúženo pouze na to, zdali přibrat další kartu (karty),",
            "\nči stát.Krupiér provádí pokyny hráče, dokud se hráč nerozhodne stát nebo nepřetáhne.",
            "\nPřetáhne-li, jeho sázka je okamžitě sebrána.")
        print("\nJakmile krupiér takto obslouží všechny hráče, rozdá si druhou.",
              "\nPoté sebere prohrávající sázky, vyplatí vyhrávající sázky a vrátí sázky remízové.")
        print("\nTahy krupiéra a hráče:")
        print("\nPokud je součet karet krupiéra menší nebo roven 16, musí přibrat další karty,",
              "\npokud je součet vyšší nebo roven 17, musí zůstat stát.",
              "\nHráč má možnost vzít si další kartu nebo zůstat stát.")
        print("\nPřejeme hodně štěstí a zdaru ve hře!!!")
        menu1()
    #Konec hry
    elif menu == str(5):
        print("\nHra byla ukončena.")
        print("\nDěkujeme za vyzkoušení!!!")
    #Jiná možnost
    else:
        print("\nNeplatný znak!!!")
        menu1()
#Konečné volání funkce
menu1()

