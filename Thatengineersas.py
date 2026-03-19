
#WIP not finished product

import pygame
import random
import math

#for debugging purposes I have added these
speed = 0.5
distance = 10
tryagain = "Y"
shiphealth = 10
loops = 1
money = 0

#speed = 0
#distance = 0

while shiphealth > 0 and (tryagain == "Y" or "y" or "YES" or "yes" or "Yes"):
    

    def timecalc():
        randomtime = random.random()
        #howlong = round(randomtime * 100 + 25)
        #Another Debugging tool to help with testing
        howlong = 1
        return howlong



    #this is a placeholder until I can be bothered to render the actual animation in blender 
    print ("About time")


    print (f"You have been tasked by the Right On Time delivery service to deliver packages throughout time.")

    if loops == 1:
        print ("For your first assignment ")


    while speed >= 1 or speed <= 0 :
        speed = float(input("How fast do you want to go? (0.1-0.9):"))

    while distance <= 0 or distance >= 100 :
        distance = int(input("How far do you want to go? (1-99):"))



    #Use these for debugging
    #print (distance)
    #print (speed)

    timeinside = round(distance/speed)
    timeoutside = round(timeinside/math.sqrt(1-speed*speed))







    print (f"You spent {timeinside} years inside the ship")
    print (f"And arrived in {timeoutside} years in the future")


    def endingcalc():
        if abs(timeinside) > 50 :
            return "You went too far and died"
        elif abs(timecalc()-timeoutside) <= 5 :
            return "You arrived on time"
        elif abs(timecalc()-timeoutside) > 5 :
            return "Not even close"
    
            
    output = endingcalc()
    print (output)




    def midending():
            midending = output == ("Not even close")
            return midending
    if midending() == True:
        shiphealth -= 2
        with open("Achievements.txt", "a") as achsave:
            achsave.write(f"Mediocre ending. Off by: {score} years\n")       
            #print ("Achievement Unlocked: Mediocre results")


    def badending():
            badending = output == ("You went too far and died")
            return badending
    if badending() == True:
        shiphealth -= 10
        with open("Achievements.txt", "a") as achsave:
            achsave.write(f"The worst ending. Off by: {score} years\n")      
            #print ("Achievement Unlocked: The worst ending")


    def goodending():
            goodending = output == ("You arrived on time")
            return goodending
    if goodending() == True:
        with open("Achievements.txt", "a") as achsave:
            achsave.write(f"You won. Off by: {score} years\n")      
            #print ("Achievement Unlocked: The worst ending")

    print (f"your ship health is {shiphealth}")
    
    tryagain = input(str("do you want to go again? Y/N"))
    if tryagain == "Y":
         loops += 1
    
    
    if tryagain == "N" or "n" or "no" or "No" or "NO":
         with open("Scores.txt", "a") as achsave:
            achsave.write(f"You made {score} deliveries and got ${money}")  



            
            
    
            
