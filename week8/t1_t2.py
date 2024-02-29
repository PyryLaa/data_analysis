import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("titanic-class-age-gender-survived.csv")
X = df.loc[:, ["Age", "Gender"]]
y = df.iloc[:, [-1]]

X_org = X
ct = ColumnTransformer(transformers=[('encoder', 
OneHotEncoder(drop="first"), ["Gender"])], remainder="passthrough")
X = ct.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=0)
'''
X_scaler = StandardScaler()
X_train = X_scaler.fit_transform(X_train)
X_test = X_scaler.transform(X_test)
'''

model = LogisticRegression()
model.fit(X_train, y_train)

#model.predict_proba näyttää todennäköisyyden esimerkiksi 0 tai 1
y_pred = model.predict(X_test)
y_pred_pros = model.predict_proba(X_test)

#Lasketaan metriikoita
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
pre = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)

sns.heatmap(cm, annot=True, fmt='g')
plt.show()

#Ennusteet uusilla matkustajilla
df_new = pd.read_csv("titanic-new.csv")
df_new = df_new.loc[:, ["Age", "Gender"]]
df_new = ct.transform(df_new)

y_pred_new = model.predict(df_new)
y_pred_new_probs = model.predict_proba(df_new)
print(y_pred_new)
print(y_pred_new_probs)

'''
Kun lisätään sukupuoli mukaan opettamiseen ja ennustamiseen, tulokset
paranevat huomattavasti. 
'''
