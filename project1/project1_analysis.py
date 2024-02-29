import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr

#Data source: 
#https://www.kaggle.com/datasets/kukuroo3/mosquito-indicator-in-seoul-korea

df = pd.read_csv("mosquito_Indicator.csv")
df = df.drop("date", axis=1) #Date not needed in this analysis

#Check if NaN values exist (none in this dataset)
nan_count = df.isna().sum()

#Scatterplot of mosquitos and temperature mean
plt.scatter(df["mean_T(℃)"], df["mosquito_Indicator"])
plt.title("Mosquitos relative to temperature mean")
plt.ylabel("Mosquitos")
plt.xlabel("Temperature mean (℃)")
plt.show()

#Scatterplot of mosquitos and rain
plt.scatter(df["rain(mm)"], df["mosquito_Indicator"])
plt.title("Mosquitos relative to rain amount")
plt.ylabel("Mosquitos")
plt.xlabel("Rain(mm)")
plt.show()

#Correlation matrix for mosquitos, temp mean and rain
corr_df = df.loc[:,["mosquito_Indicator", "mean_T(℃)", "rain(mm)"]]
corr = corr_df.corr()

#Correlation heatmap
sns.heatmap(corr, annot=True)
plt.show()

#Pearson and Spearman p-values
ppears_temp = pearsonr(corr_df["mosquito_Indicator"], corr_df["mean_T(℃)"])[1]
pspear_temp = spearmanr(corr_df["mosquito_Indicator"], corr_df["mean_T(℃)"])[1]

#p-values for rain too, significantly bigger than with temperature but still showing 
#statistical significance since it's <0.05
ppears_rain = pearsonr(corr_df["mosquito_Indicator"], corr_df["rain(mm)"])[1]
pspear_rain = spearmanr(corr_df["mosquito_Indicator"], corr_df["rain(mm)"])[1]

print(f"Pearson p-value for correlation between temperature mean and mosquitos: {ppears_temp}")
print(f"Spearman p-value for correlation between temperature mean and mosquitos: {pspear_temp}")

print(f"Pearson p-value for correlation between rain and mosquitos: {ppears_rain}")
print(f"Spearman p-value for correlation between rain and mosquitos: {pspear_rain}")