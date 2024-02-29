import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("tt.xlsx")

desc = df.describe()
df_info = df.info()
df_hist = df.hist()
plt.show()

edu = ["Peruskoulu", "2. aste", "Korkeakoulu", "Ylempi korkeakoulu"]

edu_df = pd.crosstab(index=df["koulutus"], columns="Lukumäärä")
edu_df.index = edu
edu_sum = sum(edu_df["Lukumäärä"])
edu_df["Prosenttiosuus"] = round((edu_df["Lukumäärä"] / edu_sum) * 100, 2)

edu_df = edu_df.reset_index()

edu_df.columns = ["Koulutus", "Lukumäärä", "Prosenttiosuus"]

sns.barplot(data=edu_df, x="Lukumäärä", y="Koulutus", hue="Koulutus")
plt.show()
