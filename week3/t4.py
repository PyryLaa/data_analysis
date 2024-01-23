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

#Average age of people with age > 0
filter_df = df[df["Age"] > 0] #Filter all the ages and leave age 0 out
filtered_avg = filter_df["Age"].mean()

#Change the age of all people with age 0 to the average age
df.loc[df["Age"] == 0, "Age"] = filtered_avg

#Unique values of Pclass
pclass_unique = df["PClass"].unique()

#Person with * PClass
star_person = df[df["PClass"] == "*"]

#Count of survived and non-survived people
survived = sum(df["Survived"] == 1)
not_survived = sum(df["Survived"] == 0)
survived_per = round(survived / person_count * 100, 1)
not_survived_per = round(not_survived / person_count * 100, 1)

print(f"Amount of people who survived: {survived}")
print(f"Amount of people who did not survive: {not_survived}")
print(f"Percentage of people who survived: {survived_per}")
print(f"Percentage of people who did not survive: {not_survived_per}\n")

#Survived and not survived males and females
survived_males = sum((df["Survived"] == 1) & (df["GenderCode"] == 0))
not_survived_males = sum((df["Survived"] == 0) & (df["GenderCode"] == 0))
survived_males_per = round(survived_males / person_count * 100, 1)
not_survived_males_per = round(not_survived_males / person_count * 100, 1)

survived_females = sum((df["Survived"] == 1) & (df["GenderCode"] == 1))
not_survived_females = sum((df["Survived"] == 0) & (df["GenderCode"] == 1))
survived_females_per = round(survived_females / person_count * 100, 1)
not_survived_females_per = round(not_survived_females / person_count * 100, 1)

print(f"Amount of survived males: {survived_males}")
print(f"Amount of not survived males: {not_survived_males}")
print(f"Amount of survived females: {survived_females}")
print(f"Amount of not survived females: {not_survived_females}\n")
print(f"Percentage of survived males of all the passengers: {survived_males_per}")
print(f"Percentage of not survived males of all the passengers: {not_survived_males_per}")
print(f"Percentage of survived females of all the passengers: {survived_females_per}")
print(f"Percentage of not survived females of all the passengers: {not_survived_females_per}")

