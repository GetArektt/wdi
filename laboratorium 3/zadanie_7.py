print("Podaj zakres:")
a = int(input())
b = int(input())
print("Twoj zakres to:", a, "-", b)
# Wypisujemy po kolei liczby z zakresu

if abs(a - b) <= 20:
    for n in range(a, b):
        print(n)
    print(n + 1)
elif abs(a - b) > 20:
    ilosc = abs(a - b) + 1
    srednia = ilosc + a
    if a > b:
        srodkowa = b + ilosc // 2
    elif b > a:
        srodkowa = a + ilosc // 2

    temp = srodkowa
    srodkowa -= 3
    srodkowa_licznik = srodkowa

    while srodkowa < srodkowa_licznik + 7:
        if srodkowa != temp:
            print(srodkowa)
        srodkowa = srodkowa + 1
