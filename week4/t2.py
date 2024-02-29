import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("emp-dep.csv", dtype={"phone1":str, "phone2":str})

#Create a new column to data which tells
#in which age group employee belongs
bins = list(range(15,75,5))
labels = bins[1:]
df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels, right=False)

#Create a dictionary from the age group
#column and it's value counts
ages_dict = df["age_group"].value_counts().to_dict()

#Remove all keys whose value is 0
groups = {}

for x, y in ages_dict.items():
    if y != 0:
        groups[x] = y

ages = list(groups.keys())
counts = list(groups.values())

plt.bar(ages, counts)
plt.show()