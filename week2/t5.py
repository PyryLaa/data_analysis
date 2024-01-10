import random as rand

def calc(a, b):
    return a * b


ans = []
usr = []
strings = []

for i in range(5):
    num1 = rand.randint(0, 10)
    num2 = rand.randint(0, 10)
    ans.append(calc(num1, num2))
    usr.append(int(input(f"{num1} * {num2} = ")))
    strings.append(f"{num1} * {num2}")
    
for i in range(5):
    if ans[i] != usr[i]:
        print(f"Lasku {strings[i]} väärin, vastauksesi {usr[i]} ja oikea vastaus {ans[i]} ")
    elif ans[i] == usr[i]:
        print(f"Lasku {strings[i]} oikein, vastaus on {ans[i]}")



