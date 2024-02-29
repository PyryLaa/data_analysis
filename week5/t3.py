import pandas as pd
from scipy.stats import chi2_contingency

df = pd.read_excel("tt.xlsx")

edu = ["Peruskoulu", "2. aste", "Korkeakoulu", "Ylempi korkeakoulu"]
gender = ["mies", "nainen"]

gedu_df = pd.crosstab(index=df["koulutus"], columns=df["sukup"])
gedu_df.index = edu
gedu_df.columns = gender

p = chi2_contingency(gedu_df)[1]
#P arvo oli reilusti yli 5% joten riippuvuus ei ole tilastollisesti merkittävä
gedu_df.plot(kind="barh")
