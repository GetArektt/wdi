import random

print("Witaj w aplikacji kalkulator!")

symbol=["+", "-", "*", "/", "**", "^", "x"]

def podawanie():
    print("Podaj 2 liczby:")
    a=float(input())
    b=float(input())
    return a, b

def dodawanie(a,b):
    liczba=a+b
    print("Otrzymano:", liczba)

def odejmowanie(a,b):
    liczba=a-b
    print("Otrzymano:", liczba)

def mnozenie(a,b):
    liczba=a*b
    print("Otrzymano:", liczba)

def dzielenie(a,b):
    if b==0:
        print("Error! Nie mozna dzielic przez 0!")
        dzielenie(a,b)
    else:
        liczba=a/b
        print("Otrzymano:", liczba)

def potegowanie(a,b):
    liczba=a**b
    print("Otrzymano:", liczba)

def pierwiastkowanie(a,b):
    if b==0:
        print("Tak nie mozna!")
    else:
        liczba=a**(1/b)
        print("Otrzymano:", liczba)

def losowanie(a,b):
    x=random.randint(a,b)
    print("Wylosowano liczbe:", x)

def koniec():
    print("Nastepuje koniec dzialania programu!")
    exit()

n=0

while True:
    if n==0:
        a,b=podawanie()
        print("Wybierz jedna z ponizszych informacji:")
    else:
        print("Czy chcesz wprowadzic nowe dane? [T/N]")
        dane=input()
        if dane=="T" or dane=="t":
            a,b=podawanie()
        elif dane=="N"or dane=="n":
            print("Nie wprowadzono nowych danych")
        print("Co chcesz zrobic w kolejnym kroku?")
    print("[1] Dodawanie \n"
          "[2] Odejmowanie \n"
          "[3] Mnozenie \n"
          "[4] Dzielenie \n"
          "[5] Potegowanie \n"
          "[6] Pierwiastkowanie \n"
          "[7] Losowanie liczby z zakresu\n"
          "[8] Zakonczenie programu")
    wybor=input()
    if wybor=="1" or wybor=="Dodawanie" or wybor=="dodawanie" or wybor=="+":
        dodawanie(a,b)
    elif wybor=="2" or wybor=="Odejmowanie" or wybor=="odejmowanie" or wybor=="-":
        odejmowanie(a,b)
    elif wybor=="3" or wybor=="Mnozenie" or wybor=="mnozenie" or wybor=="*":
        mnozenie(a,b)
    elif wybor=="4" or wybor=="Dzielenie" or wybor=="dzielenie" or wybor=="/":
        dzielenie(a,b)
    elif wybor=="5" or wybor=="Potegowanie" or wybor=="potegowanie" or wybor=="**":
        potegowanie(a,b)
    elif wybor=="6" or wybor=="Pierwiastkowanie" or wybor=="pierwiastkowanie" or wybor=="^":
        pierwiastkowanie(a,b)
    elif wybor=="7" or wybor=="losowanie" or wybor=="Losowanie" or wybor=="x":
        losowanie(a,b)
    elif wybor=="8" or wybor=="Zakoczenie programu" or wybor=="zakonczenie programu":
        koniec()
    else:
        print("Blad.Sprobuj jeszcze raz.")
    n=1
