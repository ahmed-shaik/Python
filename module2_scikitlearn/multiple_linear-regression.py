# Multiple Features
# 1 Output

# Best Fit Line Equation for Multi Linear Regression
# y = m1x1+m2x2+m3x3+.....+mnxn+c
# ml,m2,m3,...mn = Slopes
# c = Y Intercept

# 1. Ingest the csv file in Python memory using Pandas library
# 2. Consider the input features and output target
# Consider Temperature, Rainfall and Flyers as Input Features
# Sales will be the output target
# 3. Split your data into training(67%) and testing(33%)
# 4. Apply Linear Regression algorithm on training data
# 5. Predict for Testing data
# 6. Evaluate the test data with predicted data using MSE ( Mean Squared Error )


import pandas as pd
reg = pd.read_csv("C:\\Users\\ahmed\\Downloads\\Lemonade.csv")