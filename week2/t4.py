import random as rand

def rand_sum(a, b):
    return a + b

print("Ohjelma antaa kahden satunnaisluvun summan, luvut välillä 0-10")

num1 = rand.randint(0,10)
num2 = rand.randint(0,10)

print(f"Lukujen {num1} ja {num2} summa on {rand_sum(num1, num2)}")