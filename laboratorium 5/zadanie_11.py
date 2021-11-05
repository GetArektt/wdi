#Napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb.

#Funkcja wyznaczajaca najwiekszy wspolny dzielnik 2 liczb
def najwiekszy_wspolny_dzielnik (a,b):
    if b>a:     #Sprawdzanie, ktora liczba jest mniejsza, poniewaz najwiekszym wspolnym dzielnikiem nie moze byc liczba wieksza od mniejszej z tych liczb
        mniejsza=a
    else:
        mniejsza=b

    for i in range(1,mniejsza+1):
        if a % i==0 and b % i ==0: #Sprawdzanie za pomoca petli kazdego mozliwego dzielenia obu liczb bez reszty
            nwd = i                #Wybieramy najwieksze mozliwe rozwiazanie powyzszego ukladu
    return nwd

def najmniejsza_wspolna_wielokrotnosc(a, b):
    nww=(a*b)//najwiekszy_wspolny_dzielnik(a, b) #Wiemy z wzoru matematycznego, ze najmniejsza wspolna wielokrotnosc liczb jest iloczynem tych liczb podzielonym przez
    return nww                                   #ich najwiekszy wspolny dzielnik

#Wczytanie 3 liczb od uzytkownika
print("Wpisz 3 liczby:")
a=int(input())
b=int(input())
c=int(input())

#Petla pozwalajaca odrzucic 0, poniewaz wtedy najmniejsza wspolna wielokrotnosc nie ma sensu matematycznego
while a==0 or b==0 or c==0:
    print("Nie mozna uzyc 0. Jeszcze raz wpisz 3 liczby:")
    a=int(input())
    b=int(input())
    c=int(input())

#By uzyskac NWW trzech liczb, potrzebujemy rekurencyjne obliczyc NWW 2 liczb (a, b), potem NWW tej nowopowstalej liczby i trzeciej liczby c
y=najmniejsza_wspolna_wielokrotnosc(najmniejsza_wspolna_wielokrotnosc(a, b), c)

#Wyswietlanie wyniku na ekranie
print("Najmniejsza wspolna wielokrotnosc tych liczb to: ", y)

