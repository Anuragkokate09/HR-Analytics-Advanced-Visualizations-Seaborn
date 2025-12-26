import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./IT_Employees_Info_2000.csv")

plt.figure(figsize=(15, 20))

# Histogram - Age
plt.subplot(3, 2, 1)
sns.histplot(df['Age'], bins=10, kde=False, color='skyblue')
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Count')

# KDE Plot - Annual Salary
plt.subplot(3, 2, 2)
sns.kdeplot(df['AnnualSalary'], fill=True, color='green', linewidth=2, alpha=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.title('KDE Plot of Salary')
plt.xlabel('Annual Salary')
plt.ylabel('Density')

# 3. Histogram - Experience (From the Image)
plt.subplot(3, 2, 3)
sns.histplot(df['Experience(Years)'], kde=True, color='orange')
plt.title('Distribution of Experience (Years)')
plt.xlabel('Experience (Years)')
plt.ylabel('Count / Density')

# 5. ViolinPlot - AnnualSalary
plt.subplot(3, 2, 5)
sns.violinplot(x=df['AnnualSalary'], color='red')
plt.title('Violin Plot of AnnualSalary')
plt.xlabel('AnnualSalary')

# 6. countplot Graph - Department
plt.subplot(3, 2, 6)
sns.countplot(x='Department', data=df)
plt.title('Bar Graph of Department')
plt.xlabel('Department')
plt.ylabel('Count')
plt.xticks(rotation=45)




plt.tight_layout()

plt.show()



