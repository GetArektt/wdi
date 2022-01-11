# Wykorzystując algorytm Euklidesa napisz funkcję wyznaczającą
# Największy Wspólny Dzielnik (NWD) wprowadzonych przez użytkownika liczb.
# Zwizualizuj w konsoli rekurencyjny sposób działania programu.

class mniejsze(Exception):
    pass

def algorytm_Euklidesa(a, b):
    if b != 0:
        print(f"{b} | {a} mod {b} = {a%b}")
        return algorytm_Euklidesa(b, a % b)
    else:
        return a



while True:
    try:
        a = int(input("Wprowadz pierwsza liczbe:"))
        b = int(input("Wprowadz druga liczbe:"))
        if a < 1 or b < 1:
            raise mniejsze
        else:
            break
    except mniejsze:
        print("liczba mniejsza od 1. Sprobuj jeszcze raz")
        pass
    except ValueError:
        print("To ma byc liczba naturalna!")

print(a, "|", b)
print("NWD =", algorytm_Euklidesa(a,b))


#Przypadki testowe

#Proces dzialania programu

# Wprowadz pierwsza liczbe:75
# Wprowadz druga liczbe:50
# 75 | 50
# 50 | 75 mod 50 = 25
# 25 | 50 mod 25 = 0
# NWD = 25

#Exceptions

# Wprowadz pierwsza liczbe:b
# To ma byc liczba naturalna!
# Wprowadz pierwsza liczbe:0
# Wprowadz druga liczbe:1
# liczba mniejsza od 1. Sprobuj jeszcze raz
# Wprowadz pierwsza liczbe:0.5
# To ma byc liczba naturalna!
# Wprowadz pierwsza liczbe:132

#Potezne liczby

# Wprowadz pierwsza liczbe:12345678987654321
# Wprowadz druga liczbe:2345678995323672141
# 12345678987654321 | 2345678995323672141
# 2345678995323672141 | 12345678987654321 mod 2345678995323672141 = 12345678987654321
# 12345678987654321 | 2345678995323672141 mod 12345678987654321 = 12345666657005472
# 12345666657005472 | 12345678987654321 mod 12345666657005472 = 12330648849
# 12330648849 | 12345666657005472 mod 12330648849 = 11408356239
# 11408356239 | 12330648849 mod 11408356239 = 922292610
# 922292610 | 11408356239 mod 922292610 = 340844919
# 340844919 | 922292610 mod 340844919 = 240602772
# 240602772 | 340844919 mod 240602772 = 100242147
# 100242147 | 240602772 mod 100242147 = 40118478
# 40118478 | 100242147 mod 40118478 = 20005191
# 20005191 | 40118478 mod 20005191 = 108096
# 108096 | 20005191 mod 108096 = 7431
# 7431 | 108096 mod 7431 = 4062
# 4062 | 7431 mod 4062 = 3369
# 3369 | 4062 mod 3369 = 693
# 693 | 3369 mod 693 = 597
# 597 | 693 mod 597 = 96
# 96 | 597 mod 96 = 21
# 21 | 96 mod 21 = 12
# 12 | 21 mod 12 = 9
# 9 | 12 mod 9 = 3
# 3 | 9 mod 3 = 0
# NWD = 3
