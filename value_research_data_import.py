import pandas as pd
from functools import reduce 
from os import listdir

def import_mutual_funds_data(path):
    files = listdir(path)
    mutual_funds_data = {}
    for file in files:
        if file.find("ValueResearch") > -1:
            file_path = path + "\\" + file
            file_data = pd.read_csv(file_path,skiprows=[0,1])
            file_contents = file.split('-')[1]
            mutual_funds_data[file_contents] = file_data
    return mutual_funds_data

path = r"C:\Users\Meow\Documents\Investments\Multi Cap"
funds_data = import_mutual_funds_data(path)
nav = funds_data.pop('NavDetails') #NavDetails Dataframe has to be cleaned
nav = nav[nav['Scheme'].str.endswith('-G') ==  True] #Select only the Growth option schemes
nav = nav.reset_index(drop = True) #reset the indexes completely to allow accurate merge 
consolidated_funds_data = reduce(lambda left,right:pd.merge(left,right,on=["Fund","Rating"]),funds_data.values())
consolidated_funds_data = consolidated_funds_data.merge(nav,how = "outer",left_index =True,right_index = True)
consolidated_funds_data.to_csv(path + "\\" + "consolidated.csv")