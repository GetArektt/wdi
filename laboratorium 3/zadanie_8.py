import string
import random


print("Prosze wprowadzic wysokosc choinki: ")
x=int(input())

znaki=("*", "*", "*", "*" ,"O")

if x<0:
    print("Podano zla liczbe. Koniec dzialania programu.")
    exit()

for n in range(x):
    napis= " " * (x-n+1) , "*"*(n*2+1)
    if n==0:
        print(" " * (x+1) + "X")
    else:
        napis=''.join(random.choices(znaki, k=(n*2+1)))
        print(" " * (x-n+1), end='')
        print(napis)

print(" " * (x) ,"U")
