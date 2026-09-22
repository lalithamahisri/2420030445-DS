# pearson correlation
import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/lalit/Documents/DataScience Lab/week_3.py/Iris.csv")
print(df.corr(method = 'pearson',numeric_only = 'float'))
# spearman
# pearson correlation
df = pd.read_csv("C:/Users/lalit/Documents/DataScience Lab/week_3.py/Iris.csv")
print(df.corr(method='spearman',numeric_only = 'float'))
