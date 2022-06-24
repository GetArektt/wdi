# Proszę napisać program, który umożliwia obliczenie wartości N! dla N zakresu od 1 do M,
# gdzie M jest wartością wpisaną przez użytkownika.
# Należy obsłużyć wyjątek, gdy użytkownik podaje liczbę mniejszą od 1
# oraz taki gdy M jest większe od 10000.
# Program powinien też wypisywać na końcu różnice pomiędzy kolejnymi wartościami N!.

import timeit


class mniejsze(Exception):
    pass


class wieksze(Exception):
    pass


silnia = []
def wczytywanie():
    M = int(input("Wprowadz liczbe M:"))
    return M
M=wczytywanie()
# while True:
#     try:
#         M = int(input("Wprowadz liczbe M:"))
#         if M < 1:
#             raise mniejsze
#         elif M > 10000:
#             raise wieksze
#         else:
#             break
#     except mniejsze:
#         print("M mniejsze od 1. Sprobuj jeszcze raz")
#         #pass
#     except wieksze:
#         print("M wieksze od 10000. Sprobuj jeszcze raz")
#         #pass
#     except ValueError:
#         print("To ma byc liczba naturalna!")

start = timeit.default_timer()
x = 1

for i in range(1, M + 1):
    x = x * i  # Obliczanie silni
    silnia.append(x)  # Wpisywanie wartosci do listy
    #print(i, "! = ", x)

a = 2
for _ in range(1, len(silnia) + 1):       #Petle wykonujemy tyle razy, ile jest elementow w liscie
    if a <= len(silnia):
        print(a, "! - ", a-1, "! wynosi", silnia[a - 1] - silnia[a - 2])        #Wypisywanie roznicy na ekranie
    else:
        break
    a += 1

stop = timeit.default_timer()
print('Czas: ', stop - start)

# Dla inputu: np. "a" lub "0.5127" program odpowie: To ma byc liczba naturalna!
# Dla np. -5 lub 0 program odpowie: M mniejsze od 1.
# Dla inputu 10001 program:  M wieksze od 10000.

# Dla inputu np.12 program:
# N! = 2 - N! = 1 wynosi 1
# N! = 3 - N! = 2 wynosi 4
# N! = 4 - N! = 3 wynosi 18
# N! = 5 - N! = 4 wynosi 96
# N! = 6 - N! = 5 wynosi 600
# N! = 7 - N! = 6 wynosi 4320
# N! = 8 - N! = 7 wynosi 35280
# N! = 9 - N! = 8 wynosi 322560
# N! = 10 - N! = 9 wynosi 3265920
# N! = 11 - N! = 10 wynosi 36288000
# N! = 12 - N! = 11 wynosi 439084800

# Dla M=1 program nie wypisze nic (Bo nie ma roznicy kolejnych wyrazow)

# Dla  bardzo duzych liczb np. 9999!-9998! = 28459750264835194599486267921566605824282646178842470956575869169672531830540690977940155901594491637770985951894080061248888203542009081261172223993903...
# Czas wykonywania takiej operacji to ok 50 sekund^
