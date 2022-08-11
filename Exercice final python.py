import os
import pandas as pd
#import glob

folder_path = 'C:/Users/danie/OneDrive/Bureau/M1 ESA/M1_DANIEL/SEMESTRE 8/Python/bazar/bazar'

liste=list()

for path, dirs, files in os.walk(folder_path):
    for filename in files:
        liste.append(filename)
    

excl_merged = pd.DataFrame()
for i in liste:
    a=pd.read_excel(folder_path+'/'+i)
    b=a.loc[1,["Date","Value"]]
    #utilisation du type de la cellule aurait été plus ingénieux
    #avec is istance(x,datetime)
    #lambda est une fonction locale (comme def) qui demande d'exécuter une opération spécifique
    #df.df[-df[Date].apply(lambda x: isinstance(x,str))]
    excl_merged=excl_merged.append(b,ignore_index=True)
                                  
print(excl_merged)       
      
         
excl_merged.insert(2,"Count",1,allow_duplicates=False)
#ou df["count"]=1

df=excl_merged.groupby(by="Date", dropna=True).agg({"Count":"sum","Value":"mean"})

                     
#combined_excel = pd.concat( [ pd.read_excel(f) for f in liste ] )
#joined_list = glob.glob('folder_path'/*.xlsx)
#print(joined_list)
#liste2=pd
#df = pd.concat(liste)
#webscrapping prochain cours