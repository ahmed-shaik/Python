import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\ahmed\\Downloads\\Social_Network_Ads.csv')

# print(df.head())
# plt.scatter(df['Age'],df['EstimatedSalary'])
# plt.show()

# p_df = df[df['Purchased']==1]
# np_df = df[df['Purchased']==0]
# plt.scatter(p_df['Age'], p_df['EstimatedSalary'], label="Purchased")
# plt.scatter(np_df['Age'], np_df['EstimatedSalary'], label="Not Purchased")
# plt.legend()
# plt.show()

x=df[['Age', 'EstimatedSalary']].values
y=df['Purchased'].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
# print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(random_state=0).fit(x_train, y_train)
print(clf.predict(x_test))