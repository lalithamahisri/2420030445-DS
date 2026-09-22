import pandas as pd
#sample dataset with inconsistent date format
df = pd.DataFrame({
    'Date' : ['2025-01-05','05/06/2025','Jan 5,2025','2025.01.06']

})
print(df)

#convert all dates to the standard iso format yyyy-mm-dd
df['Date'] = pd.to_datetime(df['Date'],errors='coerce').dt.strftime('%Y-%m-%d')
print(df)