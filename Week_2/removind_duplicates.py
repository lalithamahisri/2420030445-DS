#removing duplicates
import pandas as pd
import numpy as np
df = pd.DataFrame({
    'ID': [1,2,2,3,4,4],
    'Name':['Alice','Bob','Bob','Charles','David','David'],
    'Age':[25,30,30,35,40,40]
})

print("Original Data:\n",df)

#Remove exact duplicates
df_exact = df.drop_duplicates()
print("\nAfter Exact Match removal:\n",df_exact)

#remove duplicated based on ids
df_subset_id = df.drop_duplicates(subset=['ID'])
print("\nAfter subset-based removal(ID):",df_subset_id)
#removal deupllicates based on name
df_subset_name = df.drop_duplicates(subset=['Name'])
print("\nafter subset based removal(name):",df_subset_name)

