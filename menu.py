import pygame
import os
import sys
from pygame.locals import *

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Brain Path")

#colors
lime = (50,205,50)
seagreen = (46,139,87)
black = (0,0,0)
white = (255,255,255)
pink = (153,0,153)

#backgroundmenu
path = os.path.join("picture","menu.png")
menupic = pygame.image.load(path)
menupic = pygame.transform.scale(menupic,(1024,768))


#title
fontObj = pygame.font.Font("zombiecontrol.ttf",150)
gameTitle = fontObj.render("BrainPath",True, white)
titleRect = gameTitle.get_rect()
titleRect.center = (512, 200)

#titleshading
fontObj = pygame.font.Font("zombiecontrol.ttf",150)
gameTitleshade = fontObj.render("BrainPath",True, pink)
titleRectshade = gameTitleshade.get_rect()
titleRectshade.center = (512, 210)

#start button
fontObj = pygame.font.Font("zombiecontrol.ttf",64)
startText = fontObj.render("Start",True, white)
startRect = startText.get_rect()
startRect.center = (512, 420)

#start button shade
fontObj = pygame.font.Font("zombiecontrol.ttf",64)
startTextshade = fontObj.render("Start",True, pink)
startRectshade = startTextshade.get_rect()
startRectshade.center = (512, 430)

#exit button
fontObj = pygame.font.Font("zombiecontrol.ttf",64)
exitText = fontObj.render("Exit",True, white)
exitRect = exitText.get_rect()
exitRect.center = (512, 570)
#exit button shade
fontObj = pygame.font.Font("zombiecontrol.ttf",64)
exitTextshade = fontObj.render("Exit",True, white)
exitRectshade = exitTextshade.get_rect()
exitRectshade.center = (512, 580) 
sceneNumber = 0
#Hunger
fontObj2 = pygame.font.Font("zombiecontrol.ttf", 32)
hungerText = fontObj2.render("Hunger", True, white)
hungerRect = hungerText.get_rect()
hungerRect.center = (135,46)

#bool
isholdstartbutton = False

#var
hunger1 = 600
timecounter = 0
#main loop
while True:

    if sceneNumber == 0:
        gameDisplay.blit(menupic,(0,0))
        gameDisplay.blit(gameTitleshade, titleRectshade)
        gameDisplay.blit(gameTitle, titleRect)
        gameDisplay.blit(startTextshade, startRectshade)
        startButton = pygame.Rect(426,392,158,57)
        gameDisplay.blit(startText, startRect)
        gameDisplay.blit(exitTextshade, exitRectshade)
        gameDisplay.blit(exitText, exitRect)
        exitButton = pygame.Rect(453,543,158,57)
        pygame.display.update()

        mousePos = pygame.mouse.get_pos()
        if startButton.collidepoint(mousePos) == True:
            startText = fontObj.render("Start",True, pink)
            startTextshade = fontObj.render("Start",True, white)
        elif exitButton.collidepoint(mousePos) == True:
            exitText = fontObj.render("Exit",True, pink)
            exitTextshade = fontObj.render("Exit",True, white)
        else:
            startText = fontObj.render("Start",True, white)
            startTextshade = fontObj.render("Start",True, pink)
            exitText = fontObj.render("Exit",True, white)
            exitTextshade = fontObj.render("Exit",True, pink)
            
        #events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mousePos = pygame.mouse.get_pos()
                    if exitButton.collidepoint(mousePos) == True:
                        exitText = fontObj.render("Exit",True, pink)
                        exitTextshade = fontObj.render("Exit",True, seagreen)
                    if startButton.collidepoint(mousePos) == True:
                        startText = fontObj.render("Start",True, pink)
                        startTextshade = fontObj.render("Start",True, white)
            if event.type == MOUSEBUTTONUP:
                exitText = fontObj.render("Exit",True, white)
                startText = fontObj.render("Start",True, white)
                if event.button == 1:
                    mousePos = pygame.mouse.get_pos()
                    print(mousePos)
                    if startButton.collidepoint(mousePos) == True:
                        print("start")
                        sceneNumber +=1
                    if exitButton.collidepoint(mousePos) == True:
                        pygame.quit()
                        sys.exit()

    if sceneNumber == 1:
        timecounter +=1
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,black,(0,0,212,768))
        pygame.draw.rect(gameDisplay,black,(812,0,212,768))
        pygame.draw.rect(gameDisplay,black,(0,0,1024,84))
        pygame.draw.rect(gameDisplay,black,(0,684,1024,84))

        if timecounter >= 1:
            if hunger1 > 0:
                hunger1 -= (600.0/(50.0*60))
                timecounter = 0
        positionxh = 210
        if hunger1 <= 0:
            positionxh = 2000
        pygame.draw.rect(gameDisplay, lime, (positionxh,30,hunger1,30))
        hungerText = fontObj2.render("Hunger", True, lime)
        gameDisplay.blit(hungerText, hungerRect)
        
            
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                print(mousePos)

    fpsClock.tick(fps)
          
