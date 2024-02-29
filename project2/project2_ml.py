import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

#Data source: 
#https://www.kaggle.com/datasets/kukuroo3/mosquito-indicator-in-seoul-korea

df = pd.read_csv("mosquito_Indicator.csv")
df = df.drop("date", axis=1) #Date not needed in this project

#For x data, pick all but mosquito indicator, that's what we are predicting
X = df.iloc[:,1:]
y = df.loc[:,["mosquito_Indicator"]]
y_max = df["mosquito_Indicator"].max()
y_min = df["mosquito_Indicator"].min()

#Split the data into training and testing data with 20/80 ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Scale the data
X_scaler = StandardScaler()
X_train = X_scaler.fit_transform(X_train)
X_test = X_scaler.transform(X_test)

y_scaler = StandardScaler()
y_train = y_scaler.fit_transform(y_train)

#Train the model with linear regression
model = LinearRegression()
model.fit(X_train, y_train)

#Intercept and coefficient values
coef = model.coef_
inter = model.intercept_
print(f"Coefficients: {coef}")
print(f"Intercept: {inter}")

#Prediction
y_pred = y_scaler.inverse_transform(model.predict(X_test))

#Metrics from regression
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"R2: {round(r2, 3)}")
print(f"Mae: {round(mae, 3)}")
print(f"Rmse: {round(rmse, 3)}")

df_new = pd.read_csv("new_mosquito.csv")
df_new = X_scaler.transform(df_new)
y_new = y_scaler.inverse_transform(model.predict(df_new))

for i in y_new:
    print(f"Predicted mosquito amounts: {i}")