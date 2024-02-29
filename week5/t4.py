import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr

df = pd.read_excel("tt.xlsx")

#Valitaan nämä sarakkeet alkuperäisestä dataframesta
cols = ['sukup', 'ikä', 'perhe', 'koulutus', 'palkka']
df_corr = df[cols]

#Korrelaatio heatmap valituista sarakkeista
sns.heatmap(df_corr.corr(), annot=True)
plt.show()
#Korrelaatiota näkyy olevan koulutuksen ja palkan sekä iän ja perheen välillä
#koska näiden kohdalla korrelaatiokerroin on >0.4

#Palkan ja iän p arvo
#Valitaan pearson rutiinin palauttamasta oliosta toinen arvo, joka on p arvo
p = pearsonr(df_corr["palkka"], df_corr["ikä"])[1]
p_percentage = round(p*100, 3)
#P arvo on 0,676% eli tämä korrelaatio on tilastollisesti merkittävä

#Tutkitaan myös spearman rutiinilla
#Tästä myös toinen palautuva arvo on p arvo
ps = spearmanr(a=df_corr["palkka"], b=df_corr["ikä"])[1]
ps_percentage = round(ps*100, 3)

#Spearman rutiinin mukaan p arvo on 0,465% eli myös tilastollisesti merkittävä
#Voidaan siis sanoa että palkan ja iän suhde on tilastollisesti huomioitava

#Regressiosuora sovitettuna palkan ja iän pisteisiin
sns.regplot(data=df_corr, x="ikä", y="palkka")
plt.show()