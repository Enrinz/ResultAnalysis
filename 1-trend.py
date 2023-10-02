import pandas as pd
import matplotlib.pyplot as plt
import os

# Leggi il file CSV
csv_file = 'DB-12000-hybrid-25.csv'
df = pd.read_csv(csv_file)

# Crea la cartella per salvare le immagini, se non esiste
output_folder = 'results12000_OFFS_hybrid_TEST\\trendsOFFS'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Raggruppa i dati in base al "Instance's Name"
grouped = df.groupby("Instance's Name")

# Crea un grafico per ogni "Instance Name"
for name, group in grouped:
    # Conta il numero di righe per ogni "Instance Name"
    x_data = range(1, len(group) + 1)
    
    # Estrai il valore di OFFS
    y_data = group['OFFS']

    # Crea il grafico
    plt.figure()
    plt.plot(x_data, y_data,color='#077169')
    plt.xlabel('Riga')
    plt.ylabel('OFFS')
    plt.title(f'{name}')
    #plt.show()
    name_without_txt = os.path.splitext(name)[0]
    # Salva il grafico nella cartella 'grafici' con il nome dell'istanza come titolo del file
    plt.savefig(os.path.join(output_folder, f'{name_without_txt}.png'),dpi=300)
    plt.close()