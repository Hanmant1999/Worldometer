import pandas as  pd
import numpy as np


my_csv=pd.read_csv('data.csv')

my_file=pd.ExcelWriter('corona.xlsx')
my_csv.to_excel(my_file,index=False)
my_file.save()