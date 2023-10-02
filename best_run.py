import csv

def find_iterations_with_zero_of_diff(csv_file):
    data = {}
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            instance_name = row["Instance's Name"]
            iteration = int(row["Iteration"])
            of_diff = float(row["OF_Diff"])
            
            if instance_name not in data:
                data[instance_name] = {"iterations": [], "last_non_zero_iteration": -1}
                
            if of_diff != 0:
                data[instance_name]["last_non_zero_iteration"] = iteration
            elif data[instance_name]["last_non_zero_iteration"] != -1:
                data[instance_name]["iterations"].append(iteration)
    
    return data

# Esempio di utilizzo
csv_file_path = 'datasets\DB-Output_25000_3.csv'
result = find_iterations_with_zero_of_diff(csv_file_path)

# Calcola la media dei risultati
averages = {}
for instance_name, values in result.items():
    if len(values["iterations"]) > 0:
        average_iteration = sum(values["iterations"]) / len(values["iterations"])
        averages[instance_name] = average_iteration

# Stampa le medie
print("Media degli Iteration dopo i quali OF_Diff è sempre zero:")
for instance_name, average_iteration in averages.items():
    print(f"Instance's Name: {instance_name}")
    print(f"Media delle Iteration: {average_iteration}")
    print()
