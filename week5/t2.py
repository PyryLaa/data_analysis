import pandas as pd

df = pd.read_excel("tt.xlsx")

edu = ["Peruskoulu", "2. aste", "Korkeakoulu", "Ylempi korkeakoulu"]
gender = ["mies", "nainen"]

gedu_df = pd.crosstab(index=df["koulutus"], columns=df["sukup"])
gedu_df.index = edu
gedu_df.columns = gender