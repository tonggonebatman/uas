import pandas as pd
import numpy as np
import sys  

spam_data = pd.read_csv('/resources/data/dataokta.csv')
spam_data['label'] = np.where(spam_data['label']=='positif',1,0)
print(spam_data.shape)
spam_data.head(20)
