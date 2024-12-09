import pandas as pd
import pandas as py
#data reading
df = pd.read_csv("superior university\AI\TASK9AILAB\ecommerce_dataset_updated.csv")
print (df)
#data explore
print(f"Number of Rows: {df.shape[0]} \nNumber of Columns: {df.shape[1]}")
df . count()
df.isnull().sum()
df.info()
df.describe()
df.head()
df.nunique()
df.dtypes()
df.duplicated()
df.drop_duplicates()




