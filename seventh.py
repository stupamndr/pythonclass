#dictionary# var_name={list1_var:list2_var}
colleges=['KEC','HCOE','ACOE','IOE']
location=['kalimati','chyasal','kupondole','pulchowk']
ind_advance=colleges.index('ACOE')
print(location[ind_advance])
engineering={'KEC':'kalimati','HCOE':'chyasal','ACOE':'kupondole','IOE':'pulchowk'}
print(engineering['ACOE'])
print(engineering.get('KEC'))

#accessing values from dictionary#
print(engineering.keys())# engineering.values() also work 
world={"Afghanistan":30.55,"Albania":2.77,"Algeria":39.22}
world["Nepal"]=29.3
print(world)
del[world["Nepal"]]
print("Nepal" in world)

#exercise
engineering['kec2']='dhapasi'
print("kec2" in engineering)
engineering['nec']='duwakot'
print("nec" in engineering)
engineering['kec2']='dhapakhel'
del[engineering["nec"]]
engineering['kathford']='balkumari'
print(engineering)

# #dictionaryception
engineeringx={'KEC':{'location':'kalimati','students':400},
            'HCOE':{'location':'chyasal','students':350},
            'ACOE':{'location':'kupondole','students':380},
            'IOE':{'location':'pulchowk','students':300},
            'kec2':{'location':'dhapakhel','students':420}}
data={'location':'kupondole','students':509}
engineeringx['janakpur']=data
print(engineeringx)

# pandas
# dataframe
names=['United States','Australia','Japan','India','Russia','Morocco','Egypt']
dr=[True,False,False,False,True,True,True]
cpc=[809,731,588,18,200,70,45]
import pandas as pd
my_dict={'country':names,
         'drives_right':dr,
         'cars_per_cap':cpc}
cars=pd.DataFrame(my_dict)
# print(cars)
row_label=['us','aus','jp','ind','rus','mor','egy']
cars.index=row_label
# print(cars)
cars=pd.read_csv("D:/cars.csv",index_col=0)
# print(cars)
credit_records=pd.read_csv("D:/credit_records.csv")
brics=pd.read_csv("D:/brics.csv")
print(credit_records)
print(credit_records.head())
print(credit_records.info())
#selecting a with a dot
credit=credit_records['item']
print(credit)
print(type(credit_records['item']))#<class 'pandas.core.series.Series'>
print(credit_records[['date']])
print(type(credit_records[['date']]))#<class 'pandas.core.frame.DataFrame'>
print(credit_records.price)
print(type(credit_records.price))#<class 'pandas.core.series.Series'>
great=credit_records[credit_records.price>str(20.0)]
print(great)
suspect=credit_records[credit_records.suspect=="Gertrude Cox"]
print(suspect)
print(cars.loc[[0,1,2]])
y=cars.loc[['mor','drive_right']]
print(y)