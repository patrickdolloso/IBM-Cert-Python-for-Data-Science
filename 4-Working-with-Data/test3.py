# Video: Loading Data with Pandas


'''
# Importing Pandas library
import pandas

# load csv file
csv_path='file1.csv'

df=pandas.read_csv(csv_path)
'''

# shorter version

# import pandas library into function pd
import pandas as pd

'''
# open file & store into variable csv_path
csv_path='file1.csv'

# load into dataframe df
df=pd.read_csv(csv_path)
'''

# open xlsx file
csv_path='file1.xlsx'
df=pd.read_excel(csv_path)

# examine first 5 rows
df.head()