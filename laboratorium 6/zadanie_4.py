# Proszę napisać program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
# czy liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem:
# A(n)=n∗n+n+1
#    -Należy sprawdzić przypadki użycia dla kilku wczytywanych liczb naturalnych.
#    -Należy obsłużyć wyjątek wczytania danej niebędącej liczbą naturalną.

while True:
    try:
        a = int(input("Ile liczb chcialbys podac?"))
        if a > 0:
            break
        else:
            print("To musi byc liczba naturalna!")
    except:
        print("To musi byc liczba naturalna!")

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
            if x >= 0:
                break
            else:
                print("To musi byc liczba naturalna!")
        except:
            print("To musi byc liczba naturalna!")

    while (flag == True) and (n < x + 1):
        # print("n", n)
        A = n * n + n + 1
        # print("A", A)
        if x == A:
            flag = False
            break
        if x % A == 0:
            # print("Mamy dzielnik", A)
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
    if flag == True:
        print("Nie znaleziono wielokrotnosci")
    else:
        print("Znaleziono wielokrotnosc")

i += 1
