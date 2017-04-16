import pandas as pdata

web_data = {'Day':[1,2,3,4,5,6],
             'Visitors':[10,500,657,778,2009,1299],
             'Bounce Rate':[9,268,403,667,700,1102]}

df = pdata.DataFrame(web_data)
print(df.head())
