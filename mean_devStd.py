import pandas as pd

df = pd.read_csv('datasets\DB-Output_25000.csv',keep_default_na=False)

# Raggruppa il DataFrame in base alla colonna "Instance's Name" e calcola la media e la deviazione standard della colonna "OFFS"
grouped = df.groupby("Instance's Name")["OFFS"].agg(["mean", "std"])

# Rinomina le colonne del DataFrame
grouped = grouped.rename(columns={"mean": "mean_OFFS", "std": "std_OFFS"})

# Aggiungi la colonna "value_counts" al DataFrame
grouped["row_counts"] = df["Instance's Name"].value_counts(sort=False).values

# Aggiungi l'header
grouped = grouped.reset_index().rename(columns={"Instance's Name": "Instance Name"})

# Imposta le opzioni di visualizzazione per visualizzare l'intero DataFrame
pd.set_option('display.max_rows', None)

grouped[['Instance Name', 'mean_OFFS', 'std_OFFS', 'row_counts']].to_csv("EDA2\\results25000\mean_devStd.csv", index=False)
print(grouped)