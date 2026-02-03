# Importing necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"

column_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
heart_df = pd.read_csv(url, names=column_names)


print("First few rows of the Heart Disease UCI dataset:")
print(heart_df.head())

print("\nSummary of the Heart Disease UCI dataset:")
print(heart_df.info()) 


print("\nMissing values in the dataset:")
print(heart_df.isnull().sum())


print("\nSummary statistics of numerical features:")
print(heart_df.describe())


sns.pairplot(heart_df)
plt.show()


sns.countplot(x='target', data=heart_df)
plt.title('Heart Disease Presence Count (0 = No, 1 = Yes)')
plt.show()
sns.histplot(heart_df['age'], bins=20, kde=True)
plt.title('Distribution of Age')
plt.show()


sns.histplot(x='age', hue='target', data=heart_df, bins=20, kde=True)
plt.title('Presence of Heart Disease by Age')
plt.show()
