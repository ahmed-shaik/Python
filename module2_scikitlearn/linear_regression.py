# Linear Models - Regressors in Scikit-Learn
# For linear models, there are many estimator classes which are very close to each other. Let us have a look at
# • LinearRegression, no penalty
# • Ridge, L2 penalty
# • Lasso, LI penalty (sparse models)
# • ElasticNet, L1 + L2 penalty (less sparse models)
# • SGDRegressor With loss='squared_loss'

import pandas as pd
df = pd.read_csv('C:\\Users\\ahmed\\Downloads\\Salary_dataset.csv')
print(df.head())

import matplotlib.pyplot as plt
plt.scatter(df['YearsExperience'] , df['Salary'])
plt.title("iScatter Plo")
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt. show()
x = df.iloc[:,0].values()
y = df.iloc[:,1].values()
reg=LinearRegression().fit(x, y)
print(reg)