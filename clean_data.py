# 4 i. Load Pandas library
import pandas as pd

# 4 ii. Load the data
df_clean = pd.read_csv('raw_data.csv')
print(df_clean)
print("-------------------")

# df_clean = df_clean.drop_duplicates()
# print(df_clean)
# print("-------------------")

# 4 iii. a. Drop Duplicates
df_clean = df_clean.drop_duplicates(subset=["name", "age", "date", "score"])
print(df_clean)
print("-------------------")

# 4 iii. b. Fill missing Values with s default value
df_clean['age'] = df_clean['age'].fillna('No Age Given')
df_clean['date'] = df_clean['date'].fillna('No Date Given')
df_clean['score'] = df_clean['score'].fillna('No Score Given')
print(df_clean)
print("-------------------")

# 4 iii. c. YYYY-MM-DD format
df_clean['date'] = pd.to_datetime(df_clean['date'], format='mixed', errors='coerce')
df_clean['date'] = df_clean['date'].dt.strftime('%Y-%m-%d')
print(df_clean)
print("-------------------")
df_clean['date'] = df_clean['date'].fillna('No Date Given')
print(df_clean)
print("-------------------")

# 4 iV. Export the cleaned data
df_clean.to_csv('cleaned_data.csv', index=False)