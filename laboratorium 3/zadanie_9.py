from time import sleep

numer_pin=int(2137)
saldo=int(420)

def pin():
    print("Prosze podac numer pin:")
    x=int(input())
    if x==numer_pin:
        print("Numer pin prawidlowy...")
        sleep(1)

    elif x!=numer_pin:
        print("Podano bledny pin. Prosze sprobowac jeszcze raz:")
        pin()

def wyplata():
    global saldo
    pin()
    print("Rozpoczynasz wyplate pieniedzy. Prosze podac kwote:")
    kwota=int(input())
    if kwota<=0:
        print("Tak nie mozna.")
        wyplata()
    else:
        while kwota> saldo:
            print("Niewystarczajaco srodkow na koncie. Prosze podac mniejsza kwote")
            print("Rozpoczynasz wyplate pieniedzy. Prosze podac kwote:")
            kwota=int(input())
        saldo -= kwota
        print("Twoje saldo po wykonaniu operacji:", saldo)


def wplata():
    global saldo
    pin()
    print("Rozpoczynasz wplate pieniedzy. Prosze podac kwote:")
    kwota=int(input())
    if kwota>0:
        saldo+=kwota
        print("Twoje saldo wynosi:", saldo)
    else:
        print("Nastapil blad. Prosze sprobowac jeszcze raz.")
        wplata()

print("Witaj w aplikacji Bankomat!")

while True:
    print("Co chcesz zrobic w kolejnym kroku?")
    sleep(1)
    print("Wybierz jedna z ponizszych operacji:")
    print("[1] Wyplata")
    print("[2] Wplata")
    print("[3] Sprawdz saldo")
    print("[4] Zakoncz korzystanie z programu")
    wybor=input()
    if wybor=="1" or wybor=="Wyplata" or wybor=="wyplata":
        wyplata()
    elif wybor=="2" or wybor=="Wplata" or wybor=="wplata":
        wplata()
    elif wybor=="3" or wybor=="saldo" or wybor=="Saldo":
        print("Sprawdzanie salda:", saldo)

    elif wybor=="4":
        sleep(1)
        print("Dziekujemy za skorzystanie z aplikacji. Milego dnia!")
        break

exit()
