import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\ahmed\\Downloads\\Social_Network_Ads.csv')

# print(df.head())
# plt.scatter(df['Age'],df['EstimatedSalary'])
# plt.show()

p_df = df[df['Purchased']==1]
np_df = df[df['Purchased']==0]
plt.scatter(p_df['Age'], p_df['EstimatedSalary'])
plt.scatter(np_df['Age'], np_df['EstimatedSalary'])
plt.show()
