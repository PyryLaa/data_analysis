import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("housing.csv")
df = df.dropna() #Poistetaan NaN arvot
dropped = ["population", "households", "median_house_value"]
#X dataan kaikki sarakkeet paitsi population, households ja
#median_house_value
X = df.drop(columns=dropped)
y = df.iloc[:, [-2]]

#Luodaan dummy muuttujat
X_org = X
ct = ColumnTransformer(transformers=[('encoder', 
OneHotEncoder(drop="first"), ["ocean_proximity"])], remainder="passthrough")
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

#Mielestäni virheiden suuruus on jo huomioitava, sillä rmse on luokkaa 70000
#ja mae luokkaa 50000 jolloin näiden ero on 20000 ja ennustettava data sadoissa
#tuhansissa, tosin  r2 on >0.5 joten malli sopii ennustamiseen tämän metriikan
#mukaan jotakuinkin hyvin

df_new = pd.read_csv("new_house_ct.csv")
df_new = ct.transform(df_new)
df_new = X_scaler.transform(df_new)
y_comp = y_scaler.inverse_transform(model.predict(df_new))

print("Uusien talojen ennustetut arvot (tuhatta dollaria):")
print(f"1. {round(y_comp[0][0], 2)}")
print(f"1. {round(y_comp[1][0], 2)}")
print(f"1. {round(y_comp[2][0], 2)}")
print(f"1. {round(y_comp[3][0], 2)}")
print(f"1. {round(y_comp[4][0], 2)}")