import numpy as np
import pandas as pd
#dataset 
df = pd.DataFrame({ 'Age': [25,20,np.nan,34,60],
                   'Department':['HR','Finance','Finance',np.nan,'IT']})
print(df)
print("\n")

#mean value for numeric
df['Age'] = df['Age'].fillna(df['Age'].mean())
# mode for the categorical data
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])
print(df)