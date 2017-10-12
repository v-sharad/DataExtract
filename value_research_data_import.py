import pandas as pd
from os import listdir

def import_mutual_funds_data(path):
    files = listdir(path)
    mutual_funds_data = {}
    for file in files:
        file_path = path + "\\" + file
        file_data = pd.read_csv(file_path,skiprows=[0,1])
        file_contents = file.split('-')[1]
        mutual_funds_data[file_contents] = file_data
    return mutual_funds_data

path = r"C:\Users\venkats4\Documents\Investments\Multi Cap"
funds_data = import_mutual_funds_data(path)

test = reduce(lambda left,right:pd.merge(left,right,on="Fund"),funds_data.values())
