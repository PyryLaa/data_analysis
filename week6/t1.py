import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("salary.csv")
corr = df.corr()
sns.heatmap(corr, annot=True)
plt.scatter(df["YearsExperience"], df["Salary"])
plt.show()
nans = df.isna().sum()
p = pearsonr(df["YearsExperience"], df["Salary"])[1]
ps = spearmanr(df["YearsExperience"], df["Salary"])[1]

x = df.loc[:,["YearsExperience"]]
y = df.loc[:,["Salary"]]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

model = LinearRegression()
model.fit(x_train, y_train)
coef = model.coef_[0][0]
intrcpt = model.intercept_[0]
print(f"Suoran yhtälö on: {round(coef, 3)} * x + {round(intrcpt, 3)}")

y_pred = model.predict(x_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

plt.scatter(x_train, y_train, color="red")
plt.plot(x_test, y_pred, color="blue")
plt.title("Testidatalla palkka vs kokemus")
plt.xlabel("Kokemus (vuosia)")
plt.ylabel("Palkka (eur)")
plt.show()

new_sal = model.predict([[7]])[0][0]
print(f"Uuden työntekijän palkkaennuste 7v työkokemuksella on: {round(new_sal, 2)}")
'''
Malli toimii hyvin tiettyyn pisteeseen asti, mutta lineaarisuus
ei enää esimerkiksi pidemmällä työkokemuksella ole enää luotettava
'''