import pandas as pd

df = pd.read_csv("diabetes.csv")

nans = df.isna().sum() #Create a new dataframe of the columns now containing if they have NaN or not

nan_columns = nans[nans > 0] #Every column that has NaNs

if not nan_columns.empty:
    print("Columns with NaN and their counts")
    print(nan_columns)
else:
    print("No NaNs in the set")
