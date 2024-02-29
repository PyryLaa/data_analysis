def compare(a, b):
    if a > b:
        print("a on isompi")
    elif a < b:
        print("b on isompi")
    elif a == b:
        print("yhtäsuuret")
        
print("Ohjelma vertaa kahta antamaasi numeroa")
num1 = int(input("Anna numero a: "))
num2 = int(input("Anna numero b: "))

compare(num1, num2)