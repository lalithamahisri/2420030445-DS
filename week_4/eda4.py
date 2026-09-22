import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset("titanic")
#histogram
sns.histplot(df['age'],bins=20,kde=True)
plt.title("Age Distribution")
plt.show()
df = sns.load_dataset("tips")
#Histogram
sns.histplot(df['size'],bins=10,kde=True)
plt.title("Age Distribution")
plt.show()
