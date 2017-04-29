import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib import style
style.use('ggplot')

web_data = {'days': [1,2,3],
			'visitors': [43,53,77]
			'bouncerate': [10,33,47]}

df = pd.DataFrame(web_data)
print(df)