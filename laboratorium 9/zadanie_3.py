# Proszę napisać program wczytujący macierz o ustalonych wymiarach n×n i dokonujący odwrócenia tej macierzy.
# Wymiar macierzy powinien być definiowany przez użytkownika.

class wieksza_od_jeden(Exception):
    pass


def wczytywanie_wymiaru():
    while True:
        try:
            print("Podaj wymiar macierzy kwadratowej:")
            wymiar = int(input())
            if wymiar > 1:
                break
            elif wymiar <= 1:
                raise wieksza_od_jeden
        except wieksza_od_jeden:
            print("Liczba ma byc wieksza od 1!")
        except ValueError:
            print("To ma byc liczba calkowita!")
    return wymiar

def wyznacznik(macierz, wynik=0):
    indices = list(range(len(macierz)))
    if len(macierz) == 2 and len(macierz[0]) == 2: #Przypadek dla wyznacznika macierzy 2x2
        det = macierz[0][0] * macierz[1][1] - macierz[1][0] * macierz[0][1]
        return det

    for kolumna in indices: # Przechodzenie po kazdej kolumnie
        macierz_kopia = macierz # Kopiujemy macierz
        macierz_kopia = macierz_kopia[1:] #Usuwamy pierwszy wiersz
        wysokosc = len(macierz_kopia)

        for i in range(wysokosc):

            macierz_kopia[i] = macierz_kopia[i][0:kolumna] + macierz_kopia[i][kolumna+1:] #Skreslamy dana kolumne

        x = (-1) ** (kolumna % 2)
        podwyznacznik = wyznacznik(macierz_kopia) #Za pomoca rekurencji otrzymujemy wyznacznik minora, az do skutku

        wynik += x * macierz[0][kolumna] * podwyznacznik

    return wynik

def wypelnianie_macierzy(wymiar):
    macierz = []
    for _ in range(wymiar):  # Tworzymy pusta macierz o wymiarach n x n
        macierz.append([])
    for i in range(wymiar):
        for j in range(wymiar):
            #macierz[i].append(random.randint(1, 9))  # Wypelniamy ja losowymi liczbami z danego zakresu
            while True:
                try:
                    x = int(input()) #Wypelniamy macierz za pomoca wczytanych wartosci
                    macierz[i].append(x)
                    break
                except ValueError:
                    print("Zla wartosc")

        print(macierz[i])
    return macierz


def jednostka(wymiar):
    macierz_jednostkowa = []
    for _ in range(wymiar):  # Tworzymy pusta macierz o wymiarach n x n
        macierz_jednostkowa.append([])
    for i in range(wymiar):
        for j in range(wymiar):
            macierz_jednostkowa[i].append(0)
            if i == j:
                macierz_jednostkowa[i][j] = 1
        # print(macierz_jednostkowa[i])
    return macierz_jednostkowa


def odwracanie_macierzy(A, I, n):
    if wyznacznik(A) ==0:
        print("Wyznacznik rowny 0. Nie ma macierzy odwrotnej")
        exit(2137)
    indices = list(range(n))
    for x in range(n):  # x - zmienna nad ktora pracujemy, praca na kolumnach
        wspolczynnik = 1.0 / A[x][x]  # Wspolczynnik liczby z przekatnej glownej
        # Skalujemy x-owy wiersz przez wspolczynnik (odwrotnosc wyrazu x)
        for j in range(n):  # Petla wymnazajaca kazdy wyraz z danego wiersza dla obu macierzy
            A[x][j] *= wspolczynnik
            I[x][j] *= wspolczynnik
            # print(A[j])
        print("\n")
        for i in indices[0:x] + indices[x + 1:n]:  # Petla pracujaca na wszystkich indeksach oprocz indeksu = x
            wspolczynnik_wiersza = A[i][x]
            # print("Przed")
            # for p in range(n):
            #     print(A[p])
            for j in range(n):
                A[i][j] = A[i][j] - wspolczynnik_wiersza * A[x][j]  # kazdy wyraz z wiersza - wspolczynnik*wyraz z wiersza nad ktorym pracujemy
                I[i][j] = I[i][j] - wspolczynnik_wiersza * I[x][j]
            print("Po")
            for p in range(n):
                print(A[p])
    return I


wymiar = wczytywanie_wymiaru()
macierz = wypelnianie_macierzy(wymiar)
print("Wyznacznik macierzy wynosi", wyznacznik(macierz))

print("\n")
macierz_jednostkowa = jednostka(wymiar)

odwracanie_macierzy(macierz, macierz_jednostkowa, wymiar)

print("\n")
for a in range(wymiar):
    print(macierz[a])
print("\n")
for b in range(wymiar):
    print(macierz_jednostkowa[b])

# Przypadki testowe:
# -exception errors
# >a
# To ma byc liczba calkowita!
# >-532
# Liczba ma byc wieksza od 1!
# >0
# Liczba ma byc wieksza od 1!

# [1, 5, 1]
# [7, 7, 3]
# [3, 2, 5]
#
# [-0.26851851851851855, 0.21296296296296297, -0.07407407407407411]
# [0.24074074074074073, -0.018518518518518517, -0.03703703703703704]
# [0.06481481481481483, -0.12037037037037038, 0.2592592592592593]

# Dla wiekszych
# [8, 3, 7, 9, 4]
# [4, 9, 6, 2, 8]
# [2, 6, 1, 6, 8]
# [5, 3, 5, 4, 3]
# [2, 2, 7, 4, 1]
#
# [0.35193133047210257, 0.18454935622317592, -0.20600858369098707, -0.33047210300429164, -0.24463519313304724]
# [4.5407725321888455, 2.6738197424892727, -1.6824034334763969, -8.532188841201727, -0.4978540772532194]
# [-1.639484978540774, -0.8841201716738205, 0.545064377682404, 2.9785407725321917, 0.3347639484978543]
# [1.5321888412017177, 0.7424892703862667, -0.43347639484978584, -2.8412017167381993, -0.07725321888412029]
# [-4.437768240343352, -2.497854077253221, 1.6952789699570832, 8.240343347639493, 0.4506437768240348]

# Dla macierzy
# [3, -1, 1]
# [5, 1, 4]
# [-1, 3, 2]
# Wyznacznik macierzy wynosi 0
# Wyznacznik rowny 0. Nie ma macierzy odwrotnej
