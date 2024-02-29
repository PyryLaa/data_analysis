import random as rand


def compare(a, b):
    if a > b:
        print("a on isompi")
    elif a < b:
        print("b on isompi")
    elif a == b:
        print("yhtäsuuret")
        
print("Ohjelma vertaa kahta satunnaista numeroa")

num1 = rand.randint(0, 100)
num2 = rand.randint(0, 100)
print(f"Numero a: {num1}")
print(f"Numero b: {num2}")

compare(num1, num2)