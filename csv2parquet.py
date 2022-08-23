import pandas as pd

input_file = 'GOSTAR_DATA.csv'
output_file = 'GOSTAR_DATA.parquet'
dtype = {'YEAR': 'int', 'COMPOUND_NAME': 'string', 'COMMON_NAME': 'string'} # Add column headers and their data types to handle null values in each row

# encoding cp1252 is used since this script is executed from Windows machine. For Linux, we can skip it or mention 'utf-8'
df = pd.read_csv(input_file, encoding='cp1252', dtype=dtype)
df.to_parquet(output_file)
