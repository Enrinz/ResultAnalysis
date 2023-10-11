import pandas as pd

# Definisci i valori target delle Iteration
target_iterations = [1999,2000, 3000, 4000, 5000, 6000,7000,8000, 9000,10000,11000, 12000]

# Leggi il file CSV
df = pd.read_csv('DB-Output12000_hybrid_R101_21_100.csv')

# Seleziona solo le righe con le prime Iteration corrispondenti ai valori target
df_selected = df[df['Iteration'].isin(target_iterations)]

# Esegui il raggruppamento per "Instance's Name" e salva solo i campi desiderati su un file
groups = df_selected.groupby("Instance's Name")
with open('results12000_OFFS_hybrid_R101_21_100\\steps.txt', 'w') as file:
    for name, group in groups:
        file.write("Instance's Name: {}\n".format(name))
        for index, row in group.iterrows():
            file.write("Iteration: {}\tOFFS: {}\n".format(row['Iteration'], row['OFFS']))
        file.write('\n')
