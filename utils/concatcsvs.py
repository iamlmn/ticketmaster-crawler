import pandas as pd
import glob

fin=pd.DataFrame()
for file in glob.glob('*.csv'):
    df=pd.read_csv(file)
    df['sheet']=str(file)
    print(len(df),file)
    if len(fin)<2:
        fin=df
    else:
        fin=fin.append(df)
#fin.to_csv('finalconcatenated.txt',sep='\t')
fin.to_csv('ticketmaster_2019.csv',index=False)

