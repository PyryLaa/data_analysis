import pandas as pd
from datetime import datetime, timedelta
import seaborn as sns


df_dep = pd.read_csv("departments.csv")
df_emp = pd.read_csv("employees.csv", dtype={"phone1":str, "phone2":str})

desc = df_emp.describe()

"""
print(df_emp['lname'].unique())
print(df_emp['salary'].nlargest(5))
print(df_emp['phone2'].isnull())
"""

#Merge (inner join) employees.csv and departments.csv by department
df = pd.merge(df_emp, df_dep, how="inner", on="dep")
df.drop("image", axis=1, inplace=True)

#Count the amount of employees
emp_count = df["id"].count()

#Count the amount of male and females
male_count = df["gender"].value_counts()[0]
female_count = sum(df["gender"]==1)

#Percentages of genders from total employee count
male_percentage = round(male_count / emp_count * 100, 1)
female_percentage = round(female_count / emp_count * 100, 1)

#Min, max and avg salary
max_salary = max(df["salary"])
min_salary = min(df["salary"])
avg_salary = round(sum(df["salary"]) / df["salary"].count(), 2)

#Average salary of "Tuotekehitys"
avg_salary_all = df.groupby("dname")["salary"].mean()
avg_salary_tkeh = avg_salary_all.get("Tuotekehitys", 0)

#Count of employees without phone2
no_phone2 = sum(df["phone2"].isna())

#Calculate every person's age from their birthdate
df["age"] = (datetime.now() - pd.to_datetime(df["bdate"])) // timedelta(days=365.2425)

#Age groups
bins = list(range(15,75,5))
labels = bins[1:]
df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels, right=False)

#TODO make new df with salary, age and gender, make correlation matrix and visualize it
#New dataframe with salary, age and gender
new_df = df[["gender", "age", "salary"]]

#Correlation matrix of the new df
corr_matrix = new_df.corr()

#Heatmap of the correlation
sns.heatmap(corr_matrix, annot=True)












