import pandas as pd

df_data = pd.read_csv("Titanic_data.csv")
df_names = pd.read_csv("Titanic_names.csv")

#Describe the both datasets
print(df_data.describe())
print(df_names.describe())

#Show the info of both sets
print("\nTitanic data info\n")
print(df_data.info())
print("\nTitanic names info\n")
print(df_names.info())

#Histogram of titanic data
df_data.hist(bins=4)

#Merge names and data dataframes
df = pd.merge(df_data, df_names, how="inner", on="id")

#Count of persons in data
person_count = df["id"].count()
print(f"\nPerson count: {person_count}")

#Count of genders
males = sum(df["GenderCode"]==0)
females = sum(df["GenderCode"]==1)
print(f"\nAmount of males: {males}")
print(f"\nAmount of females: {females}")

#Average age of passengers
avg_age = round(df["Age"].mean(), 1)
print(f"Average age of passengers: {avg_age}")

#Count of passengers with age = 0
zero_age = sum(df["Age"] == 0)
print(f"Sum of people with age 0: {zero_age}")
