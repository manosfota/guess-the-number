import pandas as pd
import numpy as np

c_sal=pd.read_csv(r'C:\Users\fotam\Downloads\Car_Sales 12.csv')
print(c_sal,"\n")
#print(car_sales[car_sales['Doors']<4])
sp_country=['Japan','Germany']
#c_sal[c_sal['Country_Prod'].isin(sp_country)]
#c_sal[c_sal['Country_Prod'].str.contains('U')]
#c_sal.set_index('Country_Prod')
print(c_sal.filter(like= 'Fuel',axis=1))#SOS
#print(c_sal.loc[3] )
#print(c_sal[c_sal['Country_Prod'] == 'USA'])
#print([c_sal.sort_values(by='Odometer')])

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
        index=['cobra', 'viper', 'sidewinder'],
        columns=['max_speed', 'shield'])
#print(df)
print(df.loc['viper'])
print(pd.__version__)









