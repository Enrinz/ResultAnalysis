import pandas as pd

df = pd.read_csv('DB-Output12000_S5000_S1000_hybrid.csv')
grouped = df.groupby("Instance's Name")

for name, group in grouped:
    index_min = group['OFFS'].idxmin()

    print(group.loc[index_min])
    with open("results12000_S5000_S1000_hybrid/min_ass.txt", "a") as f:
        print(group.loc[index_min],file=f)

#4806

#print(df.loc[df['OFFS'].idxmin()].head(1))