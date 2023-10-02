import pandas as pd

df = pd.read_csv('DB-12000-hybrid-25.csv')
grouped = df.groupby("Instance's Name")

for name, group in grouped:
    index_min = group['OFFS'].idxmin()

    print(group.loc[index_min])
    with open("DB-12000-hybrid-25.txt", "a") as f:
        print(group.loc[index_min],file=f)


#print(df.loc[df['OFFS'].idxmin()].head(1))