import pandas as pd

# Carica il file CSV
csv_file = 'DB-Output12000_S5000_S1000_hybrid.csv'
df = pd.read_csv(csv_file)

# Filtra il dataframe per l'iterazione 12000
df_12000 = df[df['Iteration'] == 12000]

# Itera su ciascun valore unico di "Seed" e "Instance's Name"
unique_seeds = df_12000['Seed'].unique()
unique_instances = df_12000["Instance's Name"].unique()

result = []

for seed in unique_seeds:
    for instance in unique_instances:
        # Filtra il dataframe per Seed e Instance's Name
        filtered_df = df_12000[(df_12000['Seed'] == seed) & (df_12000["Instance's Name"] == instance)]
        
        # Estrai il valore di "Exe_Time_d-r"
        exe_time = filtered_df['Exe_Time_d-r'].values[0] if not filtered_df.empty else None
        
        result.append({
            'Seed': seed,
            "Instance's Name": instance,
            'Exe_Time_d-r': exe_time
        })

# Crea un nuovo DataFrame con i risultati
result_df = pd.DataFrame(result)

# Stampa il DataFrame risultante
print(result_df)
