import pandas as pd

# Definisci i valori target delle Iteration

#1999,2000,2999, 3000, 3999,4000,
target_iterations = [4999, 5000, 5999,6000,6999,7000,7999,8000,8999, 9000,9999,10000,10999,11000,11999, 12000]

# Leggi il file CSV
df = pd.read_csv('DB-Output12000_S5000_S1000_hybrid.csv')

# Seleziona solo le righe con le prime Iteration corrispondenti ai valori target
df_selected = df[df['Iteration'].isin(target_iterations)]

# Esegui il raggruppamento per "Instance's Name" e salva solo i campi desiderati su un file
groups = df_selected.groupby("Instance's Name")
with open('results12000_S5000_S1000_hybrid\\steps.txt', 'w') as file:
    for name, group in groups:
        file.write("Instance's Name: {}\n".format(name))
        for index, row in group.iterrows():
            file.write("Iteration: {}\tOFFS: {}\n".format(row['Iteration'], row['OFFS']))
        file.write('\n')
