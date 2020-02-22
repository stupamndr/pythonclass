    #exercise 1#
hall=11.25
kitchen=18.0
living_room=20.0
bedroom=10.75
bathroom=9.50
areax=[11.25,18.0,20.0,10.75,9.50]
print(areax)
    #exercise 2#
areas=['hallway',hall,'kitchen',kitchen,'living_room',living_room,'bedroom',bedroom,'bathroom',bathroom]
#the printout becomes more informative#
print(areas)
    #exercise 3#
#we can put lists within lists-#
house=[['hallway',hall],['kitchen',kitchen],['living_room',living_room],['bedroom',bedroom],['bathroom',bathroom]]
print(house)
print(type(house))#this prints out the type of the list
    #exercise 4
print(areas[3])#subsettting lists |prints out 2nd element of list
print(areas[1])
print(areas[-1])#using negative index we can print out the last element easily
    #exercise 5
eat_sleep_area=areas[3]+areas[7] #using subsetting we can add specific elements of the list
print(eat_sleep_area)
    #exercise 6
downstairs=areas[0:6]#slicing to take specific contents from a list
print(downstairs)
upstairs=areas[-4:]#to take last four elements we can use negative indexing
print(upstairs)
    #exercise 7
downstairs=areas[1:7]#the first index is included while the last one is excluded
print(downstairs)
upstairs=areas[-4:0]
print(upstairs)
#print(house[-1][1])

    #exercise 8
areas[-1]=10.50#updating lists
areas[4]='chill zone'
areas[0]="hall"
print(areas)
    #exercise 9
area_ext=areas+['room',1.88] #using "+" opertor to add data to list 
print(area_ext)
#del(area_ext[3]) #we use del(list_name[index]) functin to delete a componenet of a list
#print(area_ext)
print(areas)
    #exercise 10
area=[11.25,18.0,20.0,10.75,9.50]
#area_copy=area #copying list to another variable
area_copy=area[:]#we can also use this method to copy list to another variable
print(area_copy)
area_copy[0]=11.89#updating a component of a list
print(area_copy)
print(area)
