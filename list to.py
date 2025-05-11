import numpy as np
import pandas as pd

col_name1 = ['col1']
list = [1,2,3]
array = np.array(list) # list np.array 변환
print(array.shape)

df_list = pd.DataFrame(list, columns=col_name1) # list DataFrame 변환
print(df_list)

col_name2 = ['col1', 'col2', 'col3']
list2 = [[1,2,3], [11,12,13]]
df_list2 = pd.DataFrame(list2, columns=col_name2) # list of lists DataFrame 변환
print(df_list2)