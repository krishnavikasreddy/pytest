#BInary Search Program
#These are part of my learning exercises

#Data that is used
#random data is created using seed 
import random
from time import time

searchArray=[]

initValue=0
for x in range(0,50):
	searchArray.append(initValue+random.randint(1,5))
	initValue=searchArray[-1]

#searchable number 
#should be made a dynamic input

searchVariable=searchArray[random.randint(0,len(searchArray)-1)]


t0=time()
#min and max value of the array
#this is used to divide the array for search

min=0
max=len(searchArray)-1

randomSearch=random.randint(min,max)

while searchArray[randomSearch]!=searchVariable:
	if searchArray[randomSearch]<searchVariable:
		min=randomSearch
	else:
		max=randomSearch
	randomSearch=random.randint(min,max)


print("{} is present at position {} in array {}; Time taken={}".format(searchVariable,randomSearch+1,searchArray,t0-time()))
		
		
