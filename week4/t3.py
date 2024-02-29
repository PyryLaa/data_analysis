import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("emp-dep.csv", dtype={"phone1":str, "phone2":str})

emp_count = df["id"].count()
males = sum(df["gender"] == 0)
females = sum(df["gender"] == 1)
percentages = [males / emp_count * 100, females / emp_count * 100]
labels = ["Males", "Females"]

plt.pie(percentages, labels = labels, autopct="%1.0f%%")
plt.show()

cag = df.groupby(["age_group", "gender"]).size().unstack()
bars = cag.plot(kind="bar")
bars.legend(["male", "female"])
plt.ylabel("Amount")
plt.xlabel("Age group")