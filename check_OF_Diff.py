import csv

def leggi_csv(file_path):
    righe_interessanti = []
    with open(file_path, 'r') as file_csv:
        lettore = csv.DictReader(file_csv)
        for riga in lettore:
            OFIS = float(riga['OFIS'])
            OFFS = float(riga['OFFS'])
            OFF_Diff = float(riga['OF_Diff'])
            if OFF_Diff<0:
                righe_interessanti.append(riga)
    return righe_interessanti

# Path del file CSV
file_csv_path = 'datasets\DB-Output18.csv'

# Chiamata alla funzione per ottenere le righe interessanti
righe_interessanti = leggi_csv(file_csv_path)


print(len(righe_interessanti))
'''# Stampa delle righe interessanti
for riga in righe_interessanti:
    print(riga)'''
