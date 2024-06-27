import pandas as pd

df = pd.DataFrame({'Yes':[1,2,3,4],
                   'No':[2,4,6,8]}, 
                   index=['A','B','C','D'])
print(df)