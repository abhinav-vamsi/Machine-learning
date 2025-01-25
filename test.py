import pandas as pd
import numpy as np
dataset=pd.read_csv(r'/Users/abhinav/Downloads/bank_transactions_data_2.csv')
print(dataset.head)
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
print(x)
print(y)