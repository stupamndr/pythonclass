#loops
     # #while loop
offset=-6
while offset!=0:
    print('correcting')
    if offset>0:
        offset=offset-1
    else:
        offset=offset+1

#     #for loop
classmates=[1.73,1.68,1.71,1.89]
for index,height in enumerate(classmates):
    print('index '+str(index)+': '+str(height))
areas=[11.25,18.0,20.0,10.75,9.50]
for index,area in enumerate(areas):
    print('room '+str(index+1)+ ' : '+str(area))
house=[['hallway',11.25],['kitchen',18.0],['bedroom',10.75],['bathroom',9.50]]
for area in house:
    print(area[0]+' is '+str(area[1]))

# # loop data structures
import numpy as np
europe={'spain':'madrid',
        'france':'paris',
        'germany':'bonn',
        'norway':'oslo',
        'italy':'rome',
        'poland':'warsaw',
        'australia':'vienna'}
for key,capital in europe.items():
    print('the capital of '+ str(key)+' is '+str(capital))
#exercise 
np_height=np.round(np.random.normal(1.75,0.20,20),2)
np_weight=np.round(np.random.normal(60.32,15,20),2)
np_baseball=np.array([np_height,np_weight])
for baseball in np.nditer(np_baseball):
    print(baseball)
for height in np_height:
    print(str(height)+' inches')
for weight in np_weight:
    print(str(height)+' kg')

#loop data structures 2 :dataframes
import pandas as pd
# brics=pd.read_csv("D:/brics.csv",index_col=0)#example
# for lab,row in brics.iterrows():
#     print(lab)
#     print(row)
cars=pd.read_csv("D:/cars.csv",index_col=1)
for lab,row in cars.iterrows():
    print(str(lab)+' : '+str(row['cars_per_cap']))
    cars.loc[lab,'COUNTRY']=row['country'].upper()
print(cars)

cars["COUNTRY"]=cars['country'].apply(str.upper)#one liner code that does not need the use of for loop
print(cars)