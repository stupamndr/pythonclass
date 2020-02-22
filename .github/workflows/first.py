#exercise 1
print(100*1.1**7)

#exercise 2
growth_multiplier=1.1                               #assigning variables
time=7 
principle_amount=100
result=principle_amount*growth_multiplier**time    
print(result)

#exercise 3
desc="compound interest"                            
profitable=True                                     

#exercise 4
savings=100
year1=savings*growth_multiplier
print(year1)
type(year1)                                         # to find out the type of variable

doubledesc=desc+desc                                
print(doubledesc)

#exercise 5
saving=5000
result2=51933.291
print("I started with NRs "+str(saving)+" and now i have NRs "+ str(result2)+". Awesome!")
pi_string="3.1415"
pi_float=float(pi_string)                           #converts string variable to float
print(pi_float)                                     

#assignment 
P=10000                                             #Principal amount
r=3.875                                             #rate of interest per year in decimal: r=R/100
t=5                                                 # time perid involved in months or years
A=P*(1+r*t)                                         #A= total accured amount
print(A)
print(str(A)+" is "+str(type(A)))