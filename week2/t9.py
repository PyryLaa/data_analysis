import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("diabetes.csv")

ages = df["Age"].value_counts().sort_values(ascending=False)

plt.figure(figsize=(10,6))
ages.plot(kind="bar", color="blue")
plt.title("Patients by age")
plt.xlabel("Age")
plt.ylabel("Amount")
plt.show()

has_diabetes = df["Outcome"].value_counts().get(1,0)
no_diabetes = df["Outcome"].value_counts().get(0,0)
print(f"Count of diabetes cases: {has_diabetes}")
print(f"Count of no diabetes cases: {no_diabetes}")