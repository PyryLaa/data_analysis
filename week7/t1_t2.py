import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("startup.csv")
X = df.iloc[:,:-1]
y = df.iloc[:, [-1]]

#Yksi metodi luoda kategorisista muuttujista dummy muuttujia
dummies = pd.get_dummies(df["State"], drop_first=True)

#Parempi metodi
X_org = X
ct = ColumnTransformer(transformers=[('encoder', 
OneHotEncoder(drop="first"), ["State"])], remainder="passthrough")
X = ct.fit_transform(X)

#Tehdään jako opetus ja testidataan
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Skaalataan data
X_scaler = StandardScaler()
X_train = X_scaler.fit_transform(X_train)
X_test = X_scaler.transform(X_test)

y_scaler = StandardScaler()
y_train = y_scaler.fit_transform(y_train)

#Opetetaan malli
model = LinearRegression()
model.fit(X_train, y_train)

#Suoran yhtälön osat
coef = model.coef_
inter = model.intercept_

#Tehdään ennuste
#y_pred = model.predict(X_test)
y_pred = y_scaler.inverse_transform(model.predict(X_test))

#Regression metriikkaa
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)


df_new = pd.read_csv("new_company_ct.csv")
df_new = ct.transform(df_new)
df_new = X_scaler.transform(df_new)
y_comp = y_scaler.inverse_transform(model.predict(df_new))

print(f"Uuden yrityksen tuotto: {round(y_comp[0][0], 2)}")

