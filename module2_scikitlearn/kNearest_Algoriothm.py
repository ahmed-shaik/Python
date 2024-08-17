# Euclidean Distance
import pandas as pd
df = pd.read_excel("C:\\Users\\ahmed\\Downloads\\Underweight-Normal.xlsx")
# print(df.head())
import matplotlib.pyplot as plt

u_df = df[df['Class']=='Underweight']
# print(u_df)
n_df = df[df['Class']=='Normal']
# print(n_df)
# plt.scatter(u_df['Weight'], u_df['Height'], label='Underweight')
# plt.scatter(n_df['Weight'], n_df['Height'], label='Normal')
# plt.scatter(57, 170, s=80)
# plt.legend()
# plt.show()
x = df.iloc[:, [0,1]].values
y = df.iloc[:, 2].values
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(x, y)
test = (57, 170)
print(neigh.predict([test]))
print(neigh.kneighbors([test]))
