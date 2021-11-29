# Stwórz funkcję, która przyjmuje jako argument listę liczb naturalnych i
# zwraca sumę liczb z listy, dla których kolejne dzielniki są dzielnikami pierwszymi.
#
# sum_prime([7, 13, 18, 23, 24]) ➞ "(2 42)(3 42)(7 7)(13 13)(23 23)"
# sum_prime([3, 5, 7, 9, 11, 13]) ➞ "(3 12)(5 5)(7 7)(11 11)(13 13)"

class niedodatnia(Exception):
    pass


class naturalna(Exception):
    pass


def wczytywanie(moja_lista):
    while True:
        try:
            print("Wprowadz dlugosc swojej listy:")
            dlugosc = int(input())
            if dlugosc > 0:
                break
            elif dlugosc <= 0:
                raise niedodatnia
        except ValueError:
            print("To ma byc liczba calkowita!")
        except niedodatnia:
            print("Liczba musi byc liczba dodatnia!")
    print("Wprowadz po kolei swoja liste liczb naturalnych.")
    for _ in range(dlugosc):
        while True:
            try:
                liczba = int(input())
                if liczba < 0:
                    raise naturalna
                else:
                    moja_lista.append(liczba)
                    break
            except ValueError:
                print("To nie liczba calkowita")
            except naturalna:
                print("To musi byc liczba naturalna")
    return moja_lista


def znajdywanie_dzielnikow(moja_lista):
    suma = {} # Definiujemy pusty slownik, do ktorego beda wpisywane dzielniki i wartosci liczb posiadajacych owe dzielniki
    for i in range(0, len(moja_lista)):  # Petla przechodzaca po kazdym elemencie z listy
        for n in range(2, moja_lista[i] + 1):  # Petla sprawdzajaca brute-forcem kazdy mozliwy dzielnik
            if moja_lista[i] % n == 0:  # Dzielniki naszej liczby
                flaga = 1 #Flaga przydatna do wykonania pewnej czesci kodu
                for j in range(2, (n // 2 + 1)):  # Sprawdzamy rozklad naszego dzielnika na jak najmniejsze dzielniki
                    if n % j == 0:  # Jesli dzielnik da sie podzielic przez dana liczbe, to znaczy ze nie jest ona liczba pierwsza
                        flaga = 0  # Dzieki wartosci 0 na fladze, unikamy zapisania liczby do sumy, bo nie jest pierwsza(3 linie nizej)
                        break
                if flaga == 1:  # Flaga sluzy do wypisywania podzielnika(warunek z petli z j sie nie wykonal)
                    if n not in suma:  # Tworzymy liste naszych dzielnikow, zeby potem mozna ja bylo wystwielic w dogodnej formie
                        suma[n] = 0 #Tworzenie klucza n w slowniku
                    suma[n] += moja_lista[i] # Dodanie wartosci danej liczby z listy do slownika (klucz to wartosc dzielnika)

    print("Suma", suma)


moja_lista = []
wczytywanie(moja_lista)
znajdywanie_dzielnikow(moja_lista)


# Przypadki testowe
# Dla liter, liczb ujemnych, zmiennoprzecinkowych program zglosi blad i nie pozwoli pojsc dalej
# 7
# 13
# 18
# 23
# 24
# Suma {7: 7, 13: 13, 2: 42, 3: 42, 23: 23}

# 3126356
# 1352465
# 6245745
# 41256437
# 21378086
# Suma {2: 24504442, 781589: 3126356, 5: 7598210, 270493: 1352465, 3: 6245745, 11: 6245745, 37853: 6245745, 41256437: 41256437, 23: 21378086, 464741: 21378086}
