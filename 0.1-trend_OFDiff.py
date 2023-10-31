import pandas as pd
import matplotlib.pyplot as plt
import os

starts = [2000, 5000]
steps = [1000]
tecnicals = ["original", "hybrid"]

# Leggi il file CSV
for start in starts:
    for step in steps:
        for tecnical in tecnicals:
            csv_file = 'DB-Output12000_S' + str(start) + '_S' + str(step) + '_' + tecnical + '.csv'
            df = pd.read_csv(csv_file)

            # Crea la cartella per salvare le immagini, se non esiste
            output_folder = 'results12000_S' + str(start) + '_S' + str(step) + '_' + tecnical + '\\trendsOFDIFF'
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Raggruppa i dati in base al "Instance's Name" e "Seed"
            grouped = df.groupby(["Instance's Name", "Seed"])

            # Valori di Iteration per cui si vuole colorare il punto in rosso
            highlight_iterations = [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]

            index_of_5000 = highlight_iterations.index(starts[1])
            elements_from_5000 = highlight_iterations[index_of_5000:]

            # Crea un grafico per ogni "Instance Name" e "Seed"
            for (name, seed), group in grouped:
                # Conta il numero di righe per ogni "Instance Name" e "Seed"
                x_data = range(1, len(group) + 1)

                # Estrai il valore di OF_Diff
                y_data = group['OF_Diff']

                # Estrai il valore di Iteration
                iteration_data = group['Iteration']

                # Crea il grafico con dimensioni personalizzate (larghezza, altezza)
                plt.figure()  # Modifica le dimensioni come preferisci

                plt.plot(x_data, y_data, color='#077169', label='Trend')
                plt.xlabel('Iterazione')
                plt.ylabel('OF_Diff')
                plt.title(f'{name.replace(".txt", "")}, Start: {start}, Step: {step}, Tech: {tecnical}, Seed: {seed}')

                if tecnical == "original":
                    pass
                else:
                    if start==2000:
                        # Colora i punti in rosso se l'Iteration è nell'elenco specificato
                        for i in range(len(iteration_data)):
                            if iteration_data.iloc[i] in highlight_iterations:
                                plt.scatter(x_data[i], y_data.iloc[i], color='red', marker='.', s=30, label=f'Iteration {iteration_data.iloc[i]}')
                    else:
                        for i in range(len(iteration_data)):
                            if iteration_data.iloc[i] in elements_from_5000:
                                plt.scatter(x_data[i], y_data.iloc[i], color='red', marker='.', s=30, label=f'Iteration {iteration_data.iloc[i]}')
    

                # Salva il grafico nella cartella 'grafici' con il nome dell'istanza e del seed come titolo del file
                name_without_txt = os.path.splitext(name)[0]
                plt.savefig(os.path.join(output_folder, f'{name_without_txt}_Seed{seed}.png'), dpi=300)
                plt.close()
