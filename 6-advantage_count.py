import os
import pandas as pd
import numpy as np


num="12000_c107_grafting" #

improvements = {} 
neutrals={}
dir = "splitted_dataset"+str(num)    
files = os.listdir(dir)
for file in files:

    df = pd.read_csv(dir+"\\"+file) 

    df_pos=df[df['OFIS'] - df['OFFS']>0]
    df_neu=df[df['OFIS'] - df['OFFS']==0]


    improvements[file.replace(".csv","")] = len(df_pos)*100/(len(df)) #len(df_pos)
    neutrals[file.replace(".csv","")]=len(df_neu)*100/(len(df))  #len(df_neu)


sorted_improvemets = dict(sorted(improvements.items(), key=lambda x: x[1], reverse=True))
sorted_neutrals = dict(sorted(neutrals.items(), key=lambda x: x[1], reverse=True))
df_improvements = pd.DataFrame(list(sorted_improvemets.items()), columns=['Move', 'Improves Count'])
df_neutrals = pd.DataFrame(list(sorted_neutrals.items()), columns=['Move', 'Neutral Count'])

with open('results12000_OFFS_c107_grafting\\advantage_count.txt', 'a') as f:
    print("Classifica migliorative:\n",df_improvements,file=f)
    print("Classifica neutrali:\n",df_neutrals,file=f)
