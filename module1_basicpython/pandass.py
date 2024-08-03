import pandas as pd
# Pandas is a Open source library for analytics
# Data Ingestion / Data Collection
# Data Manipulation / Data Processing

# 1. DataFrame - 2d objects =>Matrix Array
# 2. Series - single dimensional objects =>Vector Array

# a = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
# print(a)
# print(a[0])
# print(type(a))

# Data Ingestion
# pd.DataFrame( )
# pd.read_csv() - CSV: Comma separated value
# pd.read_excel 
# pd.read_json( ) - Javascript object notation
# pd.table()

# d = {'Name': ['Mr A', 'Mr B', 'Mr C'],
#      'Weight' : [143, 154, 134]}
# df = pd.DataFrame(d)
# print(df)
# print(df.iloc[0]) #accessing rows
# print(df['Name']) #accewssing columns
# print(type(df))

df = pd.read_excel(r'C:\Users\ahmed\Downloads\HotelFinalDataset.xlsx')
# print(df.head()) #prints the first five rows 
# print(df.tail()) # prints the last five rows
# print(df.info()) # prints the information
# print(df.nunique()) # prints the number of unique elements in each column
# print(df['Type'].unique()) # prints the unique in specified column
# print(df['City'].value_counts())

# which place has the highest ReviewsCount
# print(df['ReviewsCount'].max())
# print(df[df['ReviewsCount']==df['ReviewsCount'].max()])

#which place has got highest rating
# print(df['Rating'].max())
# print(df[df['Rating'] == df['Rating'].max()])

#changing data 
# SPIit my data based on space
# Remove comma
# Convert into int
df['Price'] =  df['Price'].apply(lambda x: int(x.split()[1].replace(',','')))
print(df['Price'].head())
print(df['Price'].max())
print(df[df['Price'] == df['Price'] .max()])