import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diabetes.csv')

desc = df.describe()

df.hist()
plt.show()

corr = df.corr()

sns.heatmap(corr, annot=True)
plt.show()
print("****Minimums****")
print(f"{df.min()}")

print("\n****Maximums****")
print(f"{df.max()}")

print("\n****Counts****")
print(f"{df.count()}")

