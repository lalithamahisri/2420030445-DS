import pandas as pd
df = pd.DataFrame({
    'sname' : ['a','b','c','d','e'],
    'QC' : [12,24,33,45,60],
    'CD' : [22,33,44,55,66],
    'TOC' : [77,88,99,22,33]
})
print(df.corr(method='spearman',numeric_only = float))