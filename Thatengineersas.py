
#WIP not finished product

import pygame
import random
import math
import time
import sys 

#for debugging purposes I have added these
#speed = 0.5
#distance = 10
pygame.init()

tryagain = "Y"
fuelcells = 10
loops = 1
money = 0
speed = 0
distance = 0
from pygame import font
gamestarted = False


#Titleactive = True 

#while Titleactive :


def splash():
    
    pygame.time.Clock
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    TEXTCOLOUR = (255, 255, 255)
    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    Titlefont = pygame.font.SysFont('freesans', 32 )
    Startfont = pygame.font.Font('Nerd.ttf', 16)
    font = pygame.font.SysFont('freesans', 16 )
    font = pygame.font.SysFont('freesans', 16 )
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    text = font.render('All characters and their appearances in time are not factual and should NOT be fact checked.', True, TEXTCOLOUR) 
    text2 = Titlefont.render('About Time.', True, TEXTCOLOUR) 
    Starttext = Startfont.render('Clock in.[Press any letter]', True, TEXTCOLOUR)
    Starttextpos = ((350, 500))
    flashpos = pygame.Rect((350, 500, 200, 20))

    
    textRect = text.get_rect()
    textRect.center = (WINDOW_WIDTH //2, WINDOW_HEIGHT //2)
    

    titleactive = True
    enterunpressed = True
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
        screen.blit(text2, textRect)
        pygame.time.delay(1000)
 
        
        while enterunpressed == True: 
            screen.blit(Starttext,Starttextpos)
            pygame.display.update()
            pygame.time.delay(1000)
            pygame.draw.rect(screen, (255, 255, 255), (flashpos))
            pygame.time.delay(250)
            pygame.display.update() 
            checkpress=input(str('Type login to start'))
            if checkpress == 'login':
                return ('Introfinish') 
    pygame.quit()        
    
                

                
            




if splash() == 'Introfinish':
        while fuelcells > 0 and (tryagain == "Y" or "y" or "YES" or "yes" or "Yes"):
            
            
            
            def years():
                randomtime = random.random()
                #howlong = round(randomtime * 100 + 25)
                #Another Debugging tool to help with testing
                howlong = 1
                return howlong



            #this is a placeholder until I can be bothered to render the actual animation in blender 


            print (f"You have been tasked by the Right On Time delivery service (R.O.T) to deliver packages throughout time.")


            if loops == 1:
                print (f"For your first assignment is to deliver a package to {years()}")


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
                    return "Too far"
                elif abs(years()-timeoutside) <= 5 :
                    return "On time"
                elif abs(years()-timeoutside) > 5 :
                    return "Not even close"
            
                    
            deliveryresult = endingcalc()
            
            print (deliveryresult)

            if deliveryresult == ("Not even close"):
                print ("You didnt make it in time and lost 2 fuel cells")
                fuelcells -= 2

            if deliveryresult == ("On time"):
                if fuelcells < 10:
                    print ("The R.O.T rewards your perfect landing with 2 fuel cells")
                    print ("You gained +2 fuel cells")
                    fuelcells += 2
            if deliveryresult == ("Too far"):
                print ("You went too far and missed the date, the R.O.T is dissapointed in your efforts")
                print ("You lost 4 fuel cells") 
                fuelcells -= 4

            print (f"You have {fuelcells} fuel cells remaining")
            
            tryagain = input(str("Continue? Y/N: "))
            
            if tryagain == "Y":
                loops += 1
            
            
            if tryagain == "N" or "n" or "no" or "No" or "NO":
                with open("Scores.txt", "a") as achsave:
                    achsave.write(f"You made {loops} deliveries and got ${money} \n")
            
