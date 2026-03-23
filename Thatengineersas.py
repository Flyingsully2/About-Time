import pygame
import random
import math
import sys 
import os
from datetime import datetime



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
gamestarted = False




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

            
            screen.blit(logo, (550,300))
            pygame.draw.rect(screen, (0, 0, 0), (unflashpos))
            screen.blit(Starttext,Starttextpos)
            pygame.time.delay(1000)
            pygame.display.update()
            pygame.time.delay(1000) 
            pygame.draw.rect(screen, (255, 255, 255), (flashpos))
            pygame.time.delay(1000)
            pygame.display.update()
        
            




if splash() == 'Introfinish':
        while player.fuelcells > 0 and (tryagain == "Y" or "y" or "YES" or "yes" or "Yes"):
            speed = 0
            player.deliveries += 1
            distance = 0 
            
            def years():
                randomtime = random.random()
                howlong = round(randomtime * 100 + 25)
                return howlong


            

            if player.deliveries == 1:
                print (f"You have been tasked by the Right On Time delivery service (R.O.T) to deliver packages throughout time.")
                print (f"For your first assignment you are tasked to deliver a package to the year {years()}")
            else:
                print (f"Your next delivery is at {years()}")


            while speed >= 1 or speed <= 0 :
                speed = float(input("How fast do you want to go? (0.1-0.9):"))

            while distance <= 0 or distance >= 100 :
                distance = int(input("How far do you want to go? (1-99):"))

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
            

            if deliveryresult == ("Not even close"):
                print ("You didnt make it in time and lost 2 fuel cells.")
                player.lose_fuel(2)
                player.payment(paycheck)
            if deliveryresult == ("On time"):
                if player.fuelcells < 10:
                    print ("The R.O.T rewards your perfect landing with 2 fuel cells.")
                    print ("You gained +2 fuel cells")
                    player.fuelcells += 2
                player.payment(paycheck)
            if deliveryresult == ("Too far"):
                print ("You went too far and missed the date, the R.O.T is dissapointed in your efforts.")
                print ("You lost 4 fuel cells") 
                player.lose_fuel(4)
                player.payment(paycheck)
            print (f"You have {player.fuelcells} fuel cells remaining/")
            print (f"You have ${player.money} in total.")
            print (f'paycheck:{paycheck}')
            if player.fuelcells <= 0:
                print ('You have failed the R.O.T. You lost all of your fuel and became stranded.')
                exit()









            
            def whosthis():
                WINDOW_WIDTH = 1600
                WINDOW_HEIGHT = 1200
                WHITE = (255, 255, 255)
                BLACK = (0, 0, 0)
                pygame.init()
                pygame.font.init()
                screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
                textbubble = pygame.Rect((150, 200, 1250, 100))
                speakfont = pygame.font.Font('Nerd.ttf', 32)
                speakpos = ((150, 200))
                interacting = True
                
           
                while interacting == True:
                    
                    if timeoutside >= 100 and timeoutside < 200:
                        text = speakfont.render(f'Thank you for delivering me this toothbrush Here is ${paycheck}', True, BLACK)
                        image = pygame.image.load(os.path.join('larson.png'))
                        pygame.draw.rect(screen, (WHITE), (textbubble))
                        screen.blit(image, (200,300))
                        screen.blit(text, speakpos)
                        pygame.display.update()
                        pygame.time.delay(7500)
                        interacting = False
                        pygame.quit()
                    elif timeoutside >= 200 and timeoutside < 300: 
                        text = speakfont.render(f'Thank you for delivering me this calculator Here is ${paycheck}', True, BLACK)
                        image = pygame.image.load(os.path.join('ein.png'))
                        pygame.draw.rect(screen, (WHITE), (textbubble))
                        screen.blit(image, (200,300))
                        screen.blit(text, speakpos)
                        pygame.display.update()
                        pygame.time.delay(7500)
                        interacting = False
                        pygame.quit()
                    elif timeoutside >= 300:
                        text = speakfont.render(f'ugg ugg (The strange caveman puts some sort of shell necklace in your hands) ${paycheck}???', True, BLACK)
                        image = pygame.image.load(os.path.join('ugg.png'))
                        pygame.draw.rect(screen, (WHITE), (textbubble))
                        screen.blit(image, (200,300))
                        screen.blit(text, speakpos)
                        pygame.display.update()
                        pygame.time.delay(7500)
                        interacting = False
                        pygame.quit()

            

                    
                


            whosthis()





                
            tryagain = input(str("Do you want to make another delivery? Y/N: ")).strip().upper()
        

            if tryagain == "Y":
                player.deliveries += 1
            

            if tryagain == "N":
                print (f'Good work today. You made {player.money} and made {player.deliveries} deliveries. The R.O.T congratulates you for your hard work')
                now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                with open("Scores.txt", "a") as achsave:
                    achsave.write(f"[{now}] You made {player.deliveries} deliveries and got ${player.money}\n")
                    quit()
                    
