import pandas as pd
df = pd.DataFrame({
    'Name':['Alice','Bob','charles','DAVID']
})

#to lowercase
df['Name_lower'] = df['Name'].str.lower()
df['Name_upper'] = df['Name'].str.upper()
print(df)