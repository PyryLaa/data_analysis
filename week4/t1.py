import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("emp-dep.csv", dtype={"phone1":str, "phone2":str})

#Scatter plot of the age and salary of employees
plt.scatter(df["age"], df["salary"])
plt.show()

#Bar diagram of the employees per department
#First make a dictionary of the departments and their counts
#to extract that info from the csv
dep_count = df["dname"].value_counts().sort_index().to_dict()
deps = list(dep_count.keys())
emps = list(dep_count.values())
plt.bar(deps, emps)
plt.show()

#Turn the bar diagram around
plt.barh(deps, emps)
plt.show()

