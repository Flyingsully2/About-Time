
#WIP not finished product

import pygame
import random
import math
import time
import sys 
import os

#for debugging purposes I have added these
#speed = 0.5
#distance = 10
pygame.init()

tryagain = "Y"
class player:
    def __init__(self):
        self.fuelcells = 10
        self.deliveries = 0
        self.money = 0
    def payment(self, amount):
        self.money += amount
    def lose_fuel(self,amount):
        self.fuelcells -= amount
    def gain_fuel(self, amount):
        self.fuelcells += amount
player = player()

from pygame import font
gamestarted = False


#Titleactive = True 

#while Titleactive :


def splash():
    
    pygame.time.Clock
    WINDOW_WIDTH = 1600
    WINDOW_HEIGHT = 1200
    TEXTCOLOUR = (255, 255, 255)
    Titlefont = pygame.font.SysFont('freesans', 64 )
    Startfont = pygame.font.Font('Nerd.ttf', 32)
    font = pygame.font.SysFont('freesans', 32 )
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    text = font.render('All characters and their appearances in time are not factual and should NOT be fact checked.', True, TEXTCOLOUR) 
    text2 = Titlefont.render('About Time.', True, TEXTCOLOUR) 
    Starttext = Startfont.render('PRESS ENTER TO CLOCK IN', True, TEXTCOLOUR)
    Starttextpos = ((620, 1002))
    flashpos = pygame.Rect((620, 1002, 340, 36))
    unflashpos = pygame.Rect((620, 1002, 340, 36))
    logo = pygame.image.load(os.path.join('stupid.png'))

    textRect = text.get_rect()
    textRect.center = (WINDOW_WIDTH //2, WINDOW_HEIGHT //2)


    
   
    

    titleactive = True
    notstarted = True
    loop = True
    while titleactive:

        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(text, textRect)
        pygame.display.update()
        pygame.time.delay(1000)
        screen.fill((0, 0, 0))
        screen.blit(logo, (550,300))
        pygame.time.delay(1000)
 
        while loop == True :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.quit()
                        return ('Introfinish') 

            pygame.event.wait()
            screen.blit(logo, (550,300))
            pygame.draw.rect(screen, (0, 0, 0), (unflashpos))
            screen.blit(Starttext,Starttextpos)
            pygame.time.delay(1000)
            pygame.display.update()
            pygame.time.delay(1000) 
            pygame.draw.rect(screen, (255, 255, 255), (flashpos))
            pygame.time.delay(1000)
            pygame.display.update()
            
            #checkpress = input('Type login to start: ')
            #if checkpress == 'login':
                #notstarted = False
                
            



    
                

                
            




if splash() == 'Introfinish':
        while player.fuelcells > 0 and (tryagain == "Y" or "y" or "YES" or "yes" or "Yes"):
            speed = 0
            player.deliveries += 1
            distance = 0 
            
            def years():
                randomtime = random.random()
                howlong = round(randomtime * 100 + 25)
                #Another Debugging tool to help with testing
                #howlong = 1
                return howlong



            #this is a placeholder until I can be bothered to render the actual animation in blender 


            

            if player.deliveries == 1:
                print (f"You have been tasked by the Right On Time delivery service (R.O.T) to deliver packages throughout time.")
                print (f"For your first assignment you are tasked to deliver a package to the year {years()}")
            else:
                print (f"Your next delivery is at {years()}")


            while speed >= 1 or speed <= 0 :
                speed = float(input("How fast do you want to go? (0.1-0.9):"))

            while distance <= 0 or distance >= 100 :
                distance = int(input("How far do you want to go? (1-99):"))



            #Use these for debugging
            #print (distance)
            #print (speed)

            timeinside = round(distance/speed)
            timeoutside = round(timeinside/math.sqrt(1-speed*speed))
            moneybase = round(years()-timeoutside)
            paycheck = abs(moneybase*years())
            

            print (f"You spent {timeinside} years inside the ship")
            print (f"And arrived in {timeoutside} years in the future")


            def endingcalc():
                if abs(timeinside) > 50 :
                    return "Too far"
                elif abs(years()-timeoutside) <= 5 :
                    return "On time"
                elif abs(years()-timeoutside) > 5 :
                    return "Not even close"
            
                    
            deliveryresult = endingcalc()
            
            print (deliveryresult)

            if deliveryresult == ("Not even close"):
                print ("You didnt make it in time and lost 2 fuel cells")
                player.lose_fuel(2)
                player.payment(paycheck)
            if deliveryresult == ("On time"):
                if fuelcells < 10:
                    print ("The R.O.T rewards your perfect landing with 2 fuel cells")
                    print ("You gained +2 fuel cells")
                    fuelcells += 2
                player.payment(paycheck)
            if deliveryresult == ("Too far"):
                print ("You went too far and missed the date, the R.O.T is dissapointed in your efforts")
                print ("You lost 4 fuel cells") 
                player.lose_fuel(4)
                player.payment(paycheck)
            print (f"You have {player.fuelcells} fuel cells remaining")
            print (player.money)
            print (f'paycheck:{paycheck}')
                
            tryagain = input(str("Continue? Y/N: ")).strip().upper()
            
            if tryagain == "Y":
                player.deliveries += 1
            #player.money(paycheck)
            
            if tryagain == "N":
                with open("Scores.txt", "a") as achsave:
                    achsave.write(f"You made {player.deliveries} deliveries and got ${player.money} \n")
                    quit()
                    
