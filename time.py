import pandas as pd

df = pd.read_csv('EDA2\DB-12000-TestInstances_c106_original.csv')

print(df["Exe_Time_d-r"].head)