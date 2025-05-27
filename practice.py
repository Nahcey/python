import pandas as pd

a = pd.read_csv("C:\\Users\\data\\countries.csv",index_col = 0)
a.loc[:, 'area']
a.loc[:, ['area']]
a.loc[:, ['area', 'population']]
a.loc[:, a.columns != 'area']