#logic control low and filtering
#exercise1
print(True==False)
print(-5*15==75)
print('pyscript'=='Pyscript')
print(True==1)

#exercise 2
x=-3*6
print(x>=10)
y='test'
print('test'<=y)
print(True>False)

#exercise 3
import numpy as np
my_house=np.array([18.0,20.0,10.75,9.50])
your_house=np.array([14.0,24.0,14.75,9.0])
large=my_house>=18
print(large)
small=my_house<your_house
print(small)

# boolean operators
my_kitchen=18.0
your_kitchen=14.0
print(my_kitchen>10 and my_kitchen<18)
print(my_kitchen<14 or my_kitchen>17)
print(my_kitchen*2<your_kitchen*3)

#assignment
my_house=np.array([18.0,20.0,10.75,9.50])
your_house=np.array([14.0,24.0,14.75,9.0])
print(np.logical_or(my_house>18.5,my_house<10))
print(np.logical_or(my_house<11,your_house<11))


#conditional 
#exercise
room='kit'
area=14.0
if(room=='kit'):
    print('Looking around in the kitchen')
if(area>15):
    print('big place')
elif(area==14):
    print("mhmm... just average i guess")
else:
    print('looking around elsewhere')

#filtering pandas and dataframe
import pandas as pd
cars=pd.read_csv("D:/cars.csv",index_col=0)
#extracts drives right column as series 
# dr=cars['drives_right']
# print(dr)
# sel=cars[dr]
# print(sel)

# code converted to one liner code in accordance to aove code
sel_oneliner=cars[cars.loc[:,'drives_right']]
# or sel_oneliner=cars[cars['drives_right]]
print(sel_oneliner)

# import cars data and compare it to value
cpc=cars['cars_per_cap']
many_cars=cpc>500
print(many_cars)
car_maniac=cars[cpc]
print(car_maniac)


import numpy as np
between=np.logical_and(cpc>10,cpc<80)
medium=cars[between]
print(medium)