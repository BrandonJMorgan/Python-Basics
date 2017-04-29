import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib import style
style.use('ggplot')

web_data = {'days': [1,2,3,4,5],
			'visitors': [43,53,77,100,90],
			'bouncerate': [10,33,47,20,50]}

df = pd.DataFrame(web_data)
print(df)
#print(df.head(2)) this will print the first 2 same with .tail()the last said numbers
