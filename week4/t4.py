import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("unemployment.xlsx")

df_total_unemp = df.loc[:, ["Period", "Unemployed"]].groupby("Period").sum().reset_index()

#Lineplot the whole unemployment data
sns.set_theme()
sns.lineplot(data=df_total_unemp, x="Period", y="Unemployed").set_title("Total unemployment")
plt.ticklabel_format(style="plain", axis="y")
plt.show()

#Lineplot the unemployment data for males and females
df_gender_unemp = df.loc[:, ["Period", "Unemployed", "Gender"]].groupby(["Period", "Gender"]).sum().reset_index()
sns.lineplot(df_gender_unemp, x="Period", y="Unemployed", hue="Gender")
plt.ticklabel_format(style="plain", axis="y")
plt.show()

#Lineplot the unemployment data, grouped by ages
df_ages_unemp = df.loc[:, ["Period", "Unemployed", "Age"]].groupby(["Period", "Age"]).sum().reset_index()
sns.lineplot(df_ages_unemp, x="Period", y="Unemployed", hue="Age")
plt.ticklabel_format(style="plain", axis="y")
plt.show()