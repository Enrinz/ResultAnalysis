import pandas as pd

df = pd.read_csv('datasets/DB-Output_25000.csv')

instance_name = 'rc101_21_100.txt'

df_filtered = df[df["Instance's Name"] == instance_name]

df_filtered['OFFS_improvement'] = df_filtered['OFFS'].diff() <= 0
rows_without_improvement = df_filtered[df_filtered['OFFS_improvement'] == False]

print(rows_without_improvement)
