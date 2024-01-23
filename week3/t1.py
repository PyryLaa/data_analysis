import pandas as pd

df_dep = pd.read_csv("departments.csv")
df_emp = pd.read_csv("employees.csv", dtype={"phone1":str, "phone2":str})

desc = df_emp.describe()


print(df_emp['lname'].unique())
print(df_emp['salary'].nlargest(5))
print(df_emp['phone2'].isnull())

df = pd.merge(df_emp, df_dep, how="inner", on="dep")
df.drop("image", axis=1, inplace=True)