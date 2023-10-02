import csv

moves_dict = {}

with open('datasets\DB-Output_25000.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader) # skip header row
    for row in csvreader:
        moves = row[4] # get the value of the 'Moves' column
        for move in eval(moves): # iterate over the list of moves
            if move in moves_dict:
                moves_dict[move] += 1
            else:
                moves_dict[move] = 1

with open('EDA2\\results25000\moves_count.csv', 'w', newline='') as csvfile:
    fieldnames = ['Moves', 'Count']
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    csvwriter.writeheader()
    for move, count in moves_dict.items():
        csvwriter.writerow({'Moves': move, 'Count': count})