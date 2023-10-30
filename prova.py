import pandas as pd
import matplotlib.pyplot as plt
import os

# Leggi il file CSV
csv_file = 'DB-Output12000_S5000_S1000_hybrid.csv'
df = pd.read_csv(csv_file)

# Crea la cartella per salvare le immagini, se non esiste
output_folder = 'results12000_S5000_S1000_hybrid\\trendsOFFS_prova'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Raggruppa i dati in base al "Instance's Name"
grouped = df.groupby("Instance's Name")

# Valori di Iteration per cui si vuole colorare il punto in rosso
highlight_iterations = [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]

# Create a set to keep track of seen seeds
seen_seeds = set()

# Crea un grafico per ogni "Instance Name"
for name, group in grouped:
    # Conta il numero di righe per ogni "Instance Name"
    x_data = range(1, len(group) + 1)
    
    # Estrai il valore di OFFS
    y_data = group['OFFS']

    # Estrai il valore di Iteration
    iteration_data = group['Iteration']

    # Estrai il valore di Seed
    seed_data = group['Seed']

    # Crea il grafico con dimensioni personalizzate (larghezza, altezza)
    plt.figure()  # Modifica le dimensioni come preferisci

    plt.plot(x_data, y_data, color='#077169', label='Trend')
    plt.xlabel('Iterazione')
    plt.ylabel('OFFS')
    plt.title(f'{name}')

    # Colora i punti in rosso se l'Iteration è nell'elenco specificato
    for i in range(len(iteration_data)):
        if iteration_data.iloc[i] in highlight_iterations:
            plt.scatter(x_data[i], y_data.iloc[i], color='red', marker='.', s=30, label=f'Iteration {iteration_data.iloc[i]}')

    # Aggiungi etichette sopra i punti Seed solo per la prima occorrenza di ciascun Seed
    for i in range(len(seed_data)):
        if seed_data.iloc[i] not in seen_seeds:
            # Modifica il valore -10 nel parametro xytext per abbassare l'etichetta
            plt.annotate(f'{seed_data.iloc[i]}', (x_data[i], y_data.iloc[i]), textcoords="offset points", xytext=(0, -0.1), ha='center')
            seen_seeds.add(seed_data.iloc[i])

    # Opzionale: per evitare che la legenda mostri molte volte "Iteration xxxx"
    handles, labels = plt.gca().get_legend_handles_labels()
    new_labels, new_handles = [], []
    for handle, label in zip(handles, labels):
        if label not in new_labels:
            new_labels.append(label)
            new_handles.append(handle)

    # Salva il grafico nella cartella 'grafici' con il nome dell'istanza come titolo del file
    name_without_txt = os.path.splitext(name)[0]
    plt.savefig(os.path.join(output_folder, f'{name_without_txt}.png'), dpi=300)
    plt.close()
