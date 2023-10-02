import pandas as pd

# Carica il file CSV
df = pd.read_csv('datasets\DB-Output_25000.csv')
instance_name='r101_21_100.txt'
# Seleziona le righe in cui il valore di OFFS è seguito da un valore maggiore
# solo quando il campo "Instance's Name" è "rc101_21_100.txt"
selected_rows = df[(df["Instance's Name"] == instance_name) & (df['OFFS'].shift(-1) > df['OFFS'])] #c101_21_100 r101_21_100 rc101_21_100

# Calcola il numero di elementi con 'Instance Name' uguale a 'rc101_21_100.txt'
total_elements = df[df["Instance's Name"] == instance_name].shape[0]


# Prendi gli ultimi 8 valori di OFFS
last_8_values = selected_rows['OFFS'].tail(8)
#print(last_8_values)
# Calcola la media e la deviazione standard degli ultimi 8 elementi
average = last_8_values.mean()
std_deviation = last_8_values.std()

# Crea un nuovo DataFrame con le colonne desiderate
result_df = pd.DataFrame({"Instance's Name": [instance_name],
                          'mean_OFFS': [average],
                          'std_OFFS': [std_deviation],
                          'num_elements': [total_elements]})

#print(result_df)
# Esporta il DataFrame in un file CSV
result_df.to_csv('EDA2\\results25000\mean_devStd_top10.csv', index=False,mode='a',)
