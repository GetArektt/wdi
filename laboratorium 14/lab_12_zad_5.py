# Liczby zespolone są reprezentowane przez krotkę (Re,Im).
# Gdzie: Re – część rzeczywista liczby, Im -$ część urojona liczby.
# Proszę napisać funkcje realizujące podstawowe operacje na liczbach zespolonych,
# m.in. dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, wypisywanie i wczytywanie.
# Używając tych funkcji proszę napisać funkcję rozwiązującą równanie kwadratowe o współczynnikach zespolonych.

def wczytywanie():
    while True:
        try:
            print("Podaj czesc rzeczywista liczby zespolonej")
            re = float(input())
            print("Podaj czesc urojona liczby zespolonej")
            im = float(input())
            break
        except ValueError:
            print("Podano zła wartosc")
    z = re, im
    return z


def wypisywanie(a, b):
    if b >= 0:
        print(f"Liczba zespolona: {a} + {b}i")
    else:
        print(f"Liczba zespolona: {a} - {abs(b)}i")


def dodawanie(a, b):
    return a[0] + b[0], a[1] + b[1]


def odejmowanie(a, b):
    return a[0] - b[0], a[1] - b[1]


def mnozenie(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


# def dzielenie(a, b):
#     try:
#         return (a[0] * b[0] + a[1] * b[1]) / (b[0] * b[0] + b[1] * b[1]), (a[1] * b[0] - a[0] * b[1]) / (
#                 b[0] * b[0] + b[1] * b[1])
#     except ZeroDivisionError:
#         print("Nie mozna dzielic przez 0")
#         exit()

def dzielenie(a, b):
        return (a[0] * b[0] + a[1] * b[1]) / (b[0] * b[0] + b[1] * b[1]), (a[1] * b[0] - a[0] * b[1]) / (
                b[0] * b[0] + b[1] * b[1])

def potegowanie(a, b): #Przekorwentowanie krotki na liczby zespolone, ktorych uzywa Python dla ulatwienia obliczen
    c = complex(a[0], a[1])
    d = complex(b[0], b[1])
    return c ** d

def konwertowanie(z):  # Konwertowanie liczby zespolonej w postaci a + bj na krotke (Re,Im), przydatne po uzyciu funkcji potegowania
    return z.real, z.imag

def liczba_przeciwna(a): #Przydatne we wzorze na pierwiastki  -b
    c = -a[0]
    d = -a[1]
    return c, d


def delta(a, b, c):
    return b[0] * b[0] - b[1] * b[1] - 4 * a[0] * c[0] + 4 * a[1] * c[1], 2 * b[0] * b[1] - 4 * a[0] * c[1] - 4 * a[1] * c[0]


def kwadratoowa(a, b, delta):
    pierwiastek_delta = potegowanie(delta, (1 / 2, 0))  # Liczenie piewiastka z delty
    pierwiastek_delta = konwertowanie(pierwiastek_delta)
    # wypisywanie(pierwiastek_delta[0], pierwiastek_delta[1])

    licznik = dodawanie(liczba_przeciwna(b), pierwiastek_delta)  # Liczenie najpierw licznika pierwiastka
    wynik1 = dzielenie(licznik, mnozenie(a, (2, 0)))  # Licznik dzielimy przez 2a

    licznik = odejmowanie(liczba_przeciwna(b), pierwiastek_delta)
    wynik2 = dzielenie(licznik, mnozenie(a, (2, 0)))
    print("\nWynik 1:")
    wypisywanie(wynik1[0], wynik1[1])
    print("Wynik 2:")
    wypisywanie(wynik2[0], wynik2[1])
    return wynik1, wynik2

# z1 = wczytywanie()
# z2 = wczytywanie()
# z3 = wczytywanie()

z1 = (40, 20.137)
z2 = (0, 0.5)
z3 = (222222.25133, 12220)

suma = dodawanie(z1, z2)
roznica = odejmowanie(z1, z2)
iloczyn = mnozenie(z1, z2)
iloraz = dzielenie(z1, z2)
potega = potegowanie(z1, z2)
potega = konwertowanie(potega)

wypisywanie(z1[0], z1[1])
wypisywanie(z2[0], z2[1])
wypisywanie(z3[0], z3[1])

print("Suma:")
wypisywanie(suma[0], suma[1])
print("Roznica:")
wypisywanie(roznica[0], roznica[1])
print("Iloczyn:")
wypisywanie(iloczyn[0], iloczyn[1])
print("Iloraz:")
wypisywanie(iloraz[0], iloraz[1])
print("Potega:")
wypisywanie(potega[0], potega[1])

print(f"\n\nRownanie kwadratowe ma postac: ({z1[0]} + {z1[1]}i)x*x + ({z2[0]} + {z2[1]}i)x + {z3[0]} + {z3[1]}i")

print("Delta wynosi:")
deltson = delta(z1, z2, z3)
wypisywanie(deltson[0], deltson[1])
kwadratoowa(z1, z2, delta(z1, z2, z3))








#Przypadki Testowe
#Gdy użytkownik wpisze cos, nie bedace liczba, program odrzuci


#Wyniki sprawdzone z uzyciem wolframalpha - dzieki, dziala  ( ͡❛ ͜ʖ ͡❛)
# Liczba zespolona: 2 + 2i
# Liczba zespolona: 2 + 2i
# Liczba zespolona: 2 + 2i
# Suma:
# Liczba zespolona: 4 + 4i
# Roznica:
# Liczba zespolona: 0 + 0i
# Iloczyn:
# Liczba zespolona: 0 + 8i
# Iloraz:
# Liczba zespolona: 1.0 + 0.0i
# Potega:
# Liczba zespolona: -1.4525046270557027 - 0.8098895463353005i
#
#
# Rownanie kwadratowe ma postac: (2 + 2i)x*x + (2 + 2i)x + 2 + 2i
# Delta wynosi:
# Liczba zespolona: 0 - 24i
#
# Wynik 1:
# Liczba zespolona: -0.4999999999999999 - 0.8660254037844385i
# Wynik 2:
# Liczba zespolona: -0.5 + 0.8660254037844386i


# Liczba zespolona: 40 + 20.137i
# Liczba zespolona: 0 + 0.5i
# Liczba zespolona: 222222.25133 + 12220i
# Suma:
# Liczba zespolona: 40 + 20.637i
# Roznica:
# Liczba zespolona: 40 + 19.637i
# Iloczyn:
# Liczba zespolona: -10.0685 + 20.0i
# Iloraz:
# Liczba zespolona: 40.274 - 80.0i
# Potega:
# Liczba zespolona: -0.25672926338618474 + 0.7492373086813732i
#
#
# Rownanie kwadratowe ma postac: (40 + 20.137i)x*x + (0 + 0.5i)x + 222222.25133 + 12220i
# Delta wynosi:
# Liczba zespolona: -34571263.902799994 - 19854757.90012884i
#
# Wynik 1:
# Liczba zespolona: -14.403238794940657 - 69.01469405373176i
# Wynik 2:
# Liczba zespolona: 14.398218348079439 + 69.00472147219287i
