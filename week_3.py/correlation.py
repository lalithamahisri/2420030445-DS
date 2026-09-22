# Pearson Correlation
import pandas as pd
# Example dataset
df = pd.DataFrame({
   'X': [10, 20, 30, 40, 50], 
  'Y': [12, 24, 33, 45, 60]   }) 


 #Pearson correlation matrixc
corr_matrix = df.corr(method='pearson')
print("Pearson CorrelationMatrix:\n", corr_matrix)

#Spearman Correlation
import pandas as pd
from scipy.stats import spearmanr

 # Example datase
tdf = pd.DataFrame(
{   'X': [10, 20, 30, 40, 50],
   'Y': [12, 18, 33, 47, 55]}
) 

# Spearman correlation coefficient andp-valuec
corr_value, p_value = spearmanr(df['X'],df['Y'])
print(f"Spearman CorrelationCoefficient: {corr_value}")
print(f"P-value: {p_value}")