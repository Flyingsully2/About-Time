
#WIP not finished product

import pygame
import random
import math
import dataclasses

#for debugging purposes I have added these
#speed = 0.5
#distance = 10

speed = 0
distance = 0

def timecalc():
    randomtime = random.random()
    howlong = round(randomtime * 100 + 25)
    return howlong

#this is a placeholder until I can be bothered to render the actual animation in blender 
print ("Trip to the future")


print (f"you must travel {timecalc()} years into the future")

while speed >= 1 or speed <= 0 :
    speed = float(input("How fast do you want to go? (0-1):"))

#debugging 
distance = int(input("How far do you want to go?:"))



#Use these for debugging
#print (distance)
#print (speed)

timeinside = round(distance/speed)
timeoutside = round(timeinside/math.sqrt(1-speed*speed))

print (f"You took {timeinside} years")
print (f"And arrived in {timeoutside} years in the future")


def p3(endingmerchant):   
    shitending = (timecalc()-timeoutside) >5
    badending = (timecalc()-timeoutside) <=5 
    goodending = timeinside>50
    if timeinside>50:
        print ("You went too far and died :(")
        return badending
    elif (timecalc()-timeoutside) <=5 :
        #Make an animation of the ship landing safely
        print ("You arrived on time")
        return goodending
    elif (timecalc()-timeoutside) >5:
        print ("Not even close")
 
        
output = p3('')






    
