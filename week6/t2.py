import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("housing.csv")

plt.scatter(df["median_income"], df["median_house_value"])
plt.xlabel("Median income (10k$)")
plt.ylabel("Median value")
plt.show()
nans_inc = df["median_income"].isna().sum()
nans_val = df["median_house_value"].isna().sum()

df = df.dropna(axis=0)

x = df.loc[:, ["median_income"]]
y = df.loc[:, ["median_house_value"]]
p = pearsonr(df["median_income"], df["median_house_value"])[1]
ps = spearmanr(df["median_income"], df["median_house_value"])[1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(x_train, y_train)
coef = model.coef_[0][0]
intrcpt = model.intercept_[0]
print(f"Suoran yhtälö on: {round(coef, 3)} * x + {round(intrcpt, 3)}")

y_pred = model.predict(x_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

new_value = model.predict([[3]])[0][0]
