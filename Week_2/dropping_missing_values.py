import numpy as np
import pandas as pd
#dataset 
df = pd.DataFrame({ 'Age': [25,20,np.nan,34,60],
                   'Department':['HR','Finance','Finance',np.nan,'IT']})
#display original dataset with missing values
print(df)

df_drop_rows = df.dropna()
print("After dropping rows:\n",df_drop_rows)


df_drop_cols = df.dropna(axis=1)
print("After dropping columns:\n",df_drop_cols)