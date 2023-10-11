import pandas as pd

df = pd.read_csv('DB-Output12000_hybrid_R101_21_100.csv')
grouped = df.groupby("Instance's Name")

for name, group in grouped:
    index_min = group['OFFS'].idxmin()

    print(group.loc[index_min])
    with open("results12000_OFFS_hybrid_R101_21_100/DB-Output12000_hybrid_R101_21_100.txt", "a") as f:
        print(group.loc[index_min],file=f)

#4806

#print(df.loc[df['OFFS'].idxmin()].head(1))