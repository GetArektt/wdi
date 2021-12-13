import random

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def generator_siatki(lista):
    siatka = []
    indicies = 0
    for _ in range(9):
        siatka.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    random.shuffle(lista)
    for i in range(3):
        for j in range(3):
            siatka[i][j] = lista[indicies]
            indicies += 1
    indicies = 0
    random.shuffle(lista)
    for i in range(3, 6):
        for j in range(3, 6):
            siatka[i][j] = lista[indicies]
            indicies += 1
    indicies = 0
    random.shuffle(lista)
    for i in range(6, 9):
        for j in range(6, 9):
            siatka[i][j] = lista[indicies]
            indicies += 1

    return siatka

def rozwiązywanie_sudoku(siatka):
    flaga1 = bool
    flaga2 = bool
    flaga3 = bool
    for i in range(len(siatka)):
        for j in range(len(siatka)):
            if siatka[i][j] == 0: #Przechodzimy po petli tak dlugo, az trafimy na jakies 0
                for x in range(1, 10): #Przechodzimy po kolei przez mozliwe wartosci
                    flaga1= True
                    flaga2 = True
                    flaga3 = True
                    for it in range(len(siatka)):
                        #print("it", it, "i", i, "j", j)
                        if siatka[i][it] == x: #Sprawdzamy, czy w danym wierszu wartosc, ktora chcemy wpisac, sie nie powtarza
                            flaga1= False
                        if siatka[it][j] == x:#Sprawdzamy, czy w danej kolumnie wartosc, ktora chcemy wpisac, sie nie powtarza
                            flaga2= False
                        # for ti in range(len(siatka)):
                        #     if(math.floor(it/3) == math.floor(i/3)) and (math.floor(ti/3) == math.floor(j/3)):
                        #         flaga3 = False
                    if flaga1 and flaga2: #Wpisujemy wartosc w prawidlowe miejsce
                        siatka[i][j] = x
    return siatka

def usuwanie_elementow(siatka):
    b= random.randint(1, 15)
    for _ in range(b):
        for i in range(len(siatka)):
            k = random.randint(0, 8)
            siatka[i][k] = 0

def wyswietlanie(siatka):
    for i in range(11):
        if i == 3 or i == 7:
            siatka.insert(i, "- - - - + - - - - + - - - -")
        for j in range(11):
            if i!=3 and i != 7:
                if j==3 or j==7: #Nie wiem czemu 7 a nie 6, ale wtedy program sie nie wywala
                    siatka[i].insert(j, "|")
    return siatka


siatka = generator_siatki(lista)
rozwiązywanie_sudoku(siatka)
# for a in range(len(siatka)): #Wyswietlanie gotowej, rozwiazanej siatki sudoku
#     print(siatka[a])
# print("\n")

usuwanie_elementow(siatka)
for a in range(len(siatka)): #Wyswietlanie siatki po usunieciu elementow
    print(siatka[a])
print("\n")

wyswietlanie(siatka)
# for a in range(len(siatka)): #Wyswietlanie siatki w formie przyjemnej dla oka
#     print(str(siatka[a]))

with open("Sudoku.txt", 'a') as wczytywanie:
    wczytywanie.write("\n".join(map(str, map(lambda x:x.replace("'"," ").replace(",",""),map(str,siatka))))) #Kod pozwalajacy dodawanie po jednym wierszu do pliku

wczytywanie = open("Sudoku.txt", "a") #Odzielanie macierzy zapisanych w pliku
print("\n", file=wczytywanie)
wczytywanie.close()

