import seaborn as sns

titanic = sns.load_dataset("titanic")

print(titanic.head())

objective = "Classification: Survived (Yes/No)"
success_criteria = "Accuracy > 80%"
constraints = "Limited features, missing values, imbalanced classes"
print("Objective: ",objective)
print("Success criteria: ",success_criteria)
print("constraints: ",constraints)

