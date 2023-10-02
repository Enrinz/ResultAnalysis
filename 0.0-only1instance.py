import csv

#filtraggio del csv per una sola istanza, per effettuare un confronto tra innestamento e non

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def get_column_index(data, column_name):
    header_row = data[0]
    try:
        column_index = header_row.index(column_name)
        return column_index
    except ValueError:
        print(f"Column '{column_name}' not found in the CSV.")
        return -1

def filter_data(data, column_index, desired_prefix):
    filtered_data = [data[0]]  # Include the header row in the filtered data
    for row in data[1:]:
        if row[column_index].startswith(desired_prefix):
            filtered_data.append(row)
    return filtered_data


def write_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("Filtered data written to CSV successfully.")

# Example usage
#csv_in = "C:\\Users\\enrin\\Desktop\\Ricerca\\Fase2\\1-Dataset\\12000\\DB-Output12000_FULL.csv"
csv_in="C:\\Users\\enrin\\Desktop\\Ricerca\\Fase2\\1-Dataset\\12000\\DB-Output12000_FULL.csv"
csv_out='DB-12000-TestInstances_c107_original.csv'
desired_column = 'Instance\'s Name'
desired_prefix = 'c107_21_'

data = read_csv(csv_in)
column_index = get_column_index(data, desired_column)

if column_index != -1:
    filtered_data = filter_data(data, column_index, desired_prefix)
    write_csv(csv_out, filtered_data)
