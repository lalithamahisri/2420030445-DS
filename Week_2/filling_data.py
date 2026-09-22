# Forward fill 
import numpy as np
import pandas as pd
#dataset 
df = pd.DataFrame({ 'Age': [25,20,np.nan,34,60],
                   'Department':['HR','Finance','Finance',np.nan,'IT']})
#display original dataset with missing values
print(df)

df_ffill = df.copy()
df_ffill.ffill(inplace=True)
print(df_ffill)

# backward fill
df_bfill = df.copy()
df_bfill.bfill(inplace=True)
print(df_bfill)



