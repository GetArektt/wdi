#Definiowanie zmiennych
print("Podaj dwie liczby wieksze od 0:")
a=int(input(""))
b=int(input(""))

if a<0 and b<10:
    print("Wylaczanie programu.")
    exit()
elif a<0:
    a=abs(a)
elif b<0:
    b=abs(b)

if a>=0 and b>0:
    print("Suma=", a+b)
    print("Roznica=", a-b)
    print("Iloczyn=", a*b)
    if a*b==10:
        print("Yay!")
    print("Iloraz=", a/b)
    print("Kwadrat a=", a**2)
    print("Kwadrat b=", b**2)
    print("Pierwiastek a=", a**(1/2))
    print("Pierwiastek b=", b**(1/2))

#Procedura konczona dzialanie programu
#jesli liczba podana przez uzytkownika wynosi 0
#Teoretycznie w pythonie wystepuje komentarz wielolinowy w postaci '''text''' aczkolwiek jest to swego rodzaju polsrodek, ktory czasem moze miec negatywny wplyw na kod

elif b==0:
    print("Koniec dzialania programu. Nastepuje autodestrukcja")
    exit()

