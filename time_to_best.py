import pandas as pd

df = pd.read_csv('datasets\DB-Output_25000.csv')
instance_name='rc101_21_100.txt'
selected_rows = df[(df["Instance's Name"] == instance_name) & (df['OFFS'].shift(-1) > df['OFFS'])]
selected_rows = selected_rows.append(df[(df["Instance's Name"] == instance_name)].iloc[-1])

offs=selected_rows['OFFS']
time=selected_rows['Exe_Time_d-r']

#time.to_csv('EDA2\\results25000\\time_to_best.csv', index=True, header=True)
with open("EDA2\\results25000\\time.txt", "a") as f:
    print("Istanza: ",instance_name,"\n",time,"\n Media:",int(time.mean()),"\n",file=f)


print("Istanza: ",instance_name,time,"\n Media:",int(time.mean()))