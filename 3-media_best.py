import pandas as pd

# Lettura del dataframe
df = pd.read_csv('DB-12000-hybrid-25.csv')

# Trova gli indici dei valori "1" nel campo "Iteration"
indices = df[df['Iteration'] == 1].index

# Inizializza una lista vuota per i dataframe divisi
df_list = []

# Itera attraverso gli indici trovati
for i in range(len(indices)-1):
    start_index = indices[i]
    end_index = indices[i+1]
    
    # Estrai il dataframe per ogni sezione
    section_df = df[start_index:end_index]
    
    # Aggiungi il dataframe alla lista
    df_list.append(section_df)

# Estrai l'ultimo dataframe dalla fine dell'ultimo "1" fino alla fine del dataframe
last_section_df = df[indices[-1]:]

# Aggiungi l'ultimo dataframe alla lista
df_list.append(last_section_df)

# Dizionario per i valori minimi di ogni "Instance's Name"
min_values_dict = {}

# Apri il file di testo in modalità scrittura
with open("results12000_OFFS_hybrid\media_OFFS_best_hybrid.txt", "w") as file:
    # Itera attraverso i dataframe divisi
    for section_df in df_list:
        # Effettua il groupby sul campo "Instance's Name" e calcola il valore minimo di "OFFS" per ogni gruppo
        min_offs = section_df.groupby("Instance's Name")['OFFS'].min()

        # Aggiorna il dizionario dei valori minimi e scrivi gli elementi minimi sul file di testo
        for instance_name, min_value in min_offs.iteritems():
            if instance_name not in min_values_dict:
                min_values_dict[instance_name] = []
            min_values_dict[instance_name].append(min_value)
            file.write(f"Minimo {instance_name}: {min_value}\n")

    # Calcola la media dei valori minimi per ogni "Instance's Name"
    mean_values_dict = {}
    for instance_name, min_values in min_values_dict.items():
        mean_values_dict[instance_name] = sum(min_values) / len(min_values)

    # Scrivi i risultati finali con la media dei valori minimi per ogni "Instance's Name" sul file di testo
    for instance_name, mean_value in mean_values_dict.items():
        file.write(f"Media {instance_name}: {mean_value}\n")
