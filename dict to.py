import numpy as np
import pandas as pd

d = {'col1':[1,11], 'col2':[2,22], 'col3':[3,33]}
df_dict = pd.DataFrame(d) # dict DataFrame 변환
print(df_dict)

array3 = df_dict.values # DataFrame to numpy array
print(array3, type(array3))

to_list = df_dict.values.tolist() # DataFrame to list
print(to_list, type(to_list))

to_dict = df_dict.to_dict() # DataFrame to dict
print(to_dict, type(to_dict))