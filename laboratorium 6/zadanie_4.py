# Proszę napisać program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
# czy liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem:
# A(n)=n∗n+n+1
#    -Należy sprawdzić przypadki użycia dla kilku wczytywanych liczb naturalnych.
#    -Należy obsłużyć wyjątek wczytania danej niebędącej liczbą naturalną.


class NieDodatnia(Exception):
    pass


class Ujemna(Exception):
    pass


while True:
    try:
        a = int(input("Ile liczb chcialbys podac?"))
        if type(a) != int:
            raise ValueError
        if a > 0:
            break
        elif a <= 0:
            raise NieDodatnia

    except NieDodatnia:
        print("Liczba niedodatnia! Sprobuj jeszcze raz")
        pass
    except ValueError:
        print("To musi byc liczba naturalna!")
        pass

i = 0
global x
global flag

while i < a:
    n = 1
    flag = True
    b = True

    while True:
        try:
            x = int(input("Prosze podac liczbe naturalna:"))
            if type(x) != int:
                raise ValueError
            if 0 <= x:
                break
            if x < 0:
                raise Ujemna
        except Ujemna:
            print("Liczba ujemna! Sprobuj jeszcze raz")
            pass
        except ValueError:
            print("To musi byc liczba naturalna!")

    while flag and (n < x + 1):
        # print("n", n)
        A = n * n + n + 1
        # print("A", A)
        if x == A:
            flag = False
            break
        if x % A == 0:
            print("Mamy dzielnik", A)
            tmp = x  # Dodajemy pomocnicza zmienna, zeby  w razie czego moc powrocic do pierwotnej petli for
            while b:
                # print("x", tmp)
                tmp = tmp / A
                # print("po x", tmp)
                if tmp == 1:  # Jesli liczba dzieli sie przez dany dzielnik i daje 1, to wiemy ze jest wielokrotnoscia.
                    flag = False
                    break
                if (tmp - round(
                        tmp)) != 0:  # Jesli liczba jest zmiennoprzecinkowa, konczymy petle. Liczenie nie ma dalszego sensu, poniewaz wiemy ze nie bedzie wielokrotnoscia danego dzielnika.
                    # print(x-round(x))
                    b = False
        n += 1
    if flag:
        print("Nie znaleziono wielokrotnosci")
    else:
        print("Znaleziono wielokrotnosc")

i += 1

# Przypadki testowe
# Litera, liczba zmiennoprzecinkowa, ujemna - program odrzuca
# 241 - wielokrotnosc 7, program zwraca prawde
# 333 - ma dzielniki 3 i 111, ale nie jest to wielokrotnosc 3 lub 7
# 10101 lub 8430313 - dla duzych liczb rowniez znajduje wielokrotnosc
