import pygame
import os
import sys
from pygame.locals import *
from random import*

from Level_Path import*

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
Black = (0,0,0)
White = (255,255,255)
pink = (153,0,153)
red = (255,0,0)
dark_green = (0,51,0)
grey = (160,160,160)
verylightpink = (255,192,203)
lightpink = (255,105,180)
darkpink = (199,21,133)
somewhatdarkpink = (255,20,147)

# IMAGE SIZE
twoXtwo = 300
threeXthree = 200

blockWidth = twoXtwo
blockHeight = twoXtwo

blockWidth3 = threeXthree
blockHeight3 = threeXthree

#---------Map-For-2x2-------------------------------------------
                     
# Block 1 2x2 
path = os.path.join("Map2x2/B1.png")
Bim1 = pygame.image.load( path )
Bim1 = pygame.transform.scale(Bim1, (twoXtwo,twoXtwo))

# Block 2 2x2 
path = os.path.join("Map2x2/B2.png")
Bim2 = pygame.image.load( path )
Bim2 = pygame.transform.scale(Bim2, (twoXtwo,twoXtwo))

# Block 3 2x2 
path = os.path.join("Map2x2/B3.png")
Bim3 = pygame.image.load( path )
Bim3 = pygame.transform.scale(Bim3, (twoXtwo,twoXtwo))

# ARROW/PLAYER 
path = os.path.join("Map2x2/arrow.png")
Aim1 = pygame.image.load( path )
Aim1 = pygame.transform.scale(Aim1, (twoXtwo,twoXtwo))
#---------Map-Level-2 For-3x3-----------------------------------------
                                                                     #                     
# Block 1 3x3                                                        #
path = os.path.join("Map3x3/Level#2/B1.png")                                 
Bim1x = pygame.image.load( path )                                    #
Bim1x = pygame.transform.scale(Bim1x, (threeXthree,threeXthree))     #
                                                                     #                                                             
# Block 2 3x3                                                        #  
path = os.path.join("Map3x3/Level#2/B2.png")                                 
Bim2x = pygame.image.load( path )                                    #
Bim2x = pygame.transform.scale(Bim2x, (threeXthree,threeXthree))     #
                                                                     #
# Block 3 3x3                                                        # 
path = os.path.join("Map3x3/Level#2/B3.png")                                 
Bim3x = pygame.image.load( path )                                    #
Bim3x = pygame.transform.scale(Bim3x, (threeXthree,threeXthree))              
                                                                     #
# Block 4 3x3                                                        # 
path = os.path.join("Map3x3/Level#2/B4.png")                                 
Bim4x = pygame.image.load( path )                                    #
Bim4x = pygame.transform.scale(Bim4x, (threeXthree,threeXthree))              
                                                                     #
# Block 5 3x3                                                        # 
path = os.path.join("Map3x3/Level#2/B5.png")                                 
Bim5x = pygame.image.load( path )                                    #
Bim5x = pygame.transform.scale(Bim5x, (threeXthree,threeXthree))              
                                                                     #
# Block 6 3x3                                                        # 
path = os.path.join("Map3x3/Level#2/B6.png")                                 
Bim6x = pygame.image.load( path )                                    #
Bim6x = pygame.transform.scale(Bim6x, (threeXthree,threeXthree))              
                                                                     #
# Block 8 3x3                                                        # 
path = os.path.join("Map3x3/Level#2/B8.png")                                 
Bim8x = pygame.image.load( path )                                    #
Bim8x = pygame.transform.scale(Bim8x, (threeXthree,threeXthree))              
                                                                     #
# Block 9 3x3                                                        # 
path = os.path.join("Map3x3/Level#2/B9.png")                                 
Bim9x = pygame.image.load( path )                                    #
Bim9x = pygame.transform.scale(Bim9x, (threeXthree,threeXthree))              
                                                                     #                                                                     #                                                                     #                                                                     #                                                                     #
# ARROW/PLAYER 3x3                                                   # 
path = os.path.join("Map3x3/Level#2/arrow.png")                              
Aim1x = pygame.image.load( path )                                    #
Aim1x = pygame.transform.scale(Aim1x, (threeXthree,threeXthree))              
#---------------------------------------------------------------------
#---------Map-Level-3---For---3x3-------------------------------------
                                                                     #                     
# Block 1 3x3                                                        #
path = os.path.join("Map3x3/Level#3/B1.png")                         #
Bim1x1 = pygame.image.load( path )                                   #
Bim1x1 = pygame.transform.scale(Bim1x1, (threeXthree,threeXthree))   #
                                                                     #                                                             
# Block 2 3x3                                                        #  
path = os.path.join("Map3x3/Level#3/B2.png")                         #
Bim2x1 = pygame.image.load( path )                                   #
Bim2x1 = pygame.transform.scale(Bim2x1, (threeXthree,threeXthree))   #
                                                                     #
# Block 3 3x3                                                        # 
path = os.path.join("Map3x3/Level#3/B3.png")                         #
Bim3x1 = pygame.image.load( path )                                   #
Bim3x1 = pygame.transform.scale(Bim3x1, (threeXthree,threeXthree))   #
                                                                     #
# Block 4 3x3                                                        # 
path = os.path.join("Map3x3/Level#3/B4.png")                         #
Bim4x1 = pygame.image.load( path )                                   #
Bim4x1 = pygame.transform.scale(Bim4x1, (threeXthree,threeXthree))   #
                                                                     #
# Block 5 3x3                                                        # 
path = os.path.join("Map3x3/Level#3/B5.png")                         #
Bim5x1 = pygame.image.load( path )                                   #
Bim5x1 = pygame.transform.scale(Bim5x1, (threeXthree,threeXthree))   #
                                                                     #
# Block 6 3x3                                                        # 
path = os.path.join("Map3x3/Level#3/B6.png")                         #
Bim6x1 = pygame.image.load( path )                                   #
Bim6x1 = pygame.transform.scale(Bim6x1, (threeXthree,threeXthree))   #
                                                                     #
# Block 9 3x3                                                        # 
path = os.path.join("Map3x3/Level#3/B9.png")                         #
Bim9x1 = pygame.image.load( path )                                   #
Bim9x1 = pygame.transform.scale(Bim9x1, (threeXthree,threeXthree))   #
                                                                     #
# Block 8 3x3                                                        # 
path = os.path.join("Map3x3/Level#3/B8.png")                         #
Bim8x1 = pygame.image.load( path )                                   #
Bim8x1 = pygame.transform.scale(Bim8x1, (threeXthree,threeXthree))   #
                                                                     #                                                                     #                                                                     #                                                                     #                                                                     #
# ARROW/PLAYER 3x3                                                   # 
path = os.path.join("Map3x3/Level#3/arrow.png")                      #
Aim1x1 = pygame.image.load( path )                                   #
Aim1x1 = pygame.transform.scale(Aim1x1, (threeXthree,threeXthree))   #
#---------------------------------------------------------------------
# Row And Column
blueAtRow = 0
blueAtColumn = 0

arrowAtRow = -1
arrowAtColumn = -1

# Level Data
currentLevel = 0
LevelData = LevelDataList [currentLevel]

LevelRightData = LevelDataRight[currentLevel]

NextLevel = False
#----------------------UI/Backgrounds-----------------------------------

#backgroundmenu
path = os.path.join("picture","menu.png")
menupic = pygame.image.load(path)
menupic = pygame.transform.scale(menupic,(1024,768))

#gamebackground
bpath = os.path.join("picture", "brains.png")
brainpic = pygame.image.load(bpath)
brainpic = pygame.transform.scale(brainpic, (1024,768))

#countdown3
count3path = os.path.join("picture", "3.png")
count3pic = pygame.image.load(count3path)
count3pic = pygame.transform.scale(count3pic, (1024,768))

#countdown2
count2path = os.path.join("picture", "2.png")
count2pic = pygame.image.load(count2path)
count2pic = pygame.transform.scale(count2pic, (1024,768))

#countdown1
count1path = os.path.join("picture", "1.png")
count1pic = pygame.image.load(count1path)
count1pic = pygame.transform.scale(count1pic, (1024,768))

#go
gopath = os.path.join("picture", "go.png")
gopic = pygame.image.load(gopath)
gopic = pygame.transform.scale(gopic, (1024,768))

#gameover
overpath = os.path.join("picture", "gameover.png")
overpic = pygame.image.load(overpath)
overpic = pygame.transform.scale(overpic, (1024,768))
#victory
vicpath = os.path.join("picture", "Victory.png")
vicpic = pygame.image.load(vicpath)
vicpic = pygame.transform.scale(vicpic, (1024,768))
#--------------------------Animation Pictures---------------------------
#1
ani1path = os.path.join("map1", "1.png")
ani1pic = pygame.image.load(ani1path)
ani1pic = pygame.transform.scale(ani1pic, (600,600))
#2
ani2path = os.path.join("map1", "2.png")
ani2pic = pygame.image.load(ani2path)
ani2pic = pygame.transform.scale(ani2pic, (600,600))
#3
ani3path = os.path.join("map1", "3.png")
ani3pic = pygame.image.load(ani3path)
ani3pic = pygame.transform.scale(ani3pic, (600,600))
#4
ani4path = os.path.join("map1", "4.png")
ani4pic = pygame.image.load(ani4path)
ani4pic = pygame.transform.scale(ani4pic, (600,600))
#5
ani5path = os.path.join("map1", "5.png")
ani5pic = pygame.image.load(ani5path)
ani5pic = pygame.transform.scale(ani5pic, (600,600))
#6
ani6path = os.path.join("map1", "6.png")
ani6pic = pygame.image.load(ani6path)
ani6pic = pygame.transform.scale(ani6pic, (600,600))
#7
ani7path = os.path.join("map1", "7.png")
ani7pic = pygame.image.load(ani7path)
ani7pic = pygame.transform.scale(ani7pic, (600,600))
#8
ani8path = os.path.join("map1", "8.png")
ani8pic = pygame.image.load(ani8path)
ani8pic = pygame.transform.scale(ani8pic, (600,600))
#9
ani9path = os.path.join("map1", "9.png")
ani9pic = pygame.image.load(ani9path)
ani9pic = pygame.transform.scale(ani9pic, (600,600))
#--------------------------------------------------------------------
#1
ani21path = os.path.join("map2", "1.png")
ani21pic = pygame.image.load(ani21path)
ani21pic = pygame.transform.scale(ani21pic, (600,600))
#2
ani22path = os.path.join("map2", "2.png")
ani22pic = pygame.image.load(ani22path)
ani22pic = pygame.transform.scale(ani22pic, (600,600))
#3
ani23path = os.path.join("map2", "3.png")
ani23pic = pygame.image.load(ani23path)
ani23pic = pygame.transform.scale(ani23pic, (600,600))
#4
ani24path = os.path.join("map2", "4.png")
ani24pic = pygame.image.load(ani24path)
ani24pic = pygame.transform.scale(ani24pic, (600,600))
#5
ani25path = os.path.join("map2", "5.png")
ani25pic = pygame.image.load(ani25path)
ani25pic = pygame.transform.scale(ani25pic, (600,600))
#6
ani26path = os.path.join("map2", "6.png")
ani26pic = pygame.image.load(ani26path)
ani26pic = pygame.transform.scale(ani26pic, (600,600))
#7
ani27path = os.path.join("map2", "7.png")
ani27pic = pygame.image.load(ani27path)
ani27pic = pygame.transform.scale(ani27pic, (600,600))
#8
ani28path = os.path.join("map2", "8.png")
ani28pic = pygame.image.load(ani28path)
ani28pic = pygame.transform.scale(ani28pic, (600,600))
#9
ani29path = os.path.join("map2", "9.png")
ani29pic = pygame.image.load(ani29path)
ani29pic = pygame.transform.scale(ani29pic, (600,600))
#--------------------------------------------------------------------
#1
ani31path = os.path.join("map3", "1.png")
ani31pic = pygame.image.load(ani31path)
ani31pic = pygame.transform.scale(ani31pic, (600,600))
#2
ani32path = os.path.join("map3", "2.png")
ani32pic = pygame.image.load(ani32path)
ani32pic = pygame.transform.scale(ani32pic, (600,600))
#3
ani33path = os.path.join("map3", "3.png")
ani33pic = pygame.image.load(ani33path)
ani33pic = pygame.transform.scale(ani33pic, (600,600))
#4
ani34path = os.path.join("map3", "4.png")
ani34pic = pygame.image.load(ani34path)
ani34pic = pygame.transform.scale(ani34pic, (600,600))
#5
ani35path = os.path.join("map3", "5.png")
ani35pic = pygame.image.load(ani35path)
ani35pic = pygame.transform.scale(ani35pic, (600,600))
#6
ani36path = os.path.join("map3", "6.png")
ani36pic = pygame.image.load(ani36path)
ani36pic = pygame.transform.scale(ani36pic, (600,600))
#7
ani37path = os.path.join("map3", "7.png")
ani37pic = pygame.image.load(ani37path)
ani37pic = pygame.transform.scale(ani37pic, (600,600))
#8
ani38path = os.path.join("map3", "8.png")
ani38pic = pygame.image.load(ani38path)
ani38pic = pygame.transform.scale(ani38pic, (600,600))
#9
ani39path = os.path.join("map3", "9.png")
ani39pic = pygame.image.load(ani39path)
ani39pic = pygame.transform.scale(ani39pic, (600,600))
#------------------------UI/Texts--------------------------------------

#title
fontObj = pygame.font.Font("zombiecontrol.ttf",150)
gameTitle = fontObj.render("BrainPath",True, lightpink)
titleRect = gameTitle.get_rect()
titleRect.center = (512, 200)

#titleshading
fontObj = pygame.font.Font("zombiecontrol.ttf",150)
gameTitleshade = fontObj.render("BrainPath",True, pink)
titleRectshade = gameTitleshade.get_rect()
titleRectshade.center = (517, 205)

#start button
fontObj = pygame.font.Font("zombiecontrol.ttf",64)
startText = fontObj.render("Start",True, white)
startRect = startText.get_rect()
startRect.center = (512, 420)

#start button shade
fontObj = pygame.font.Font("zombiecontrol.ttf",64)
startTextshade = fontObj.render("Start",True, somewhatdarkpink)
startRectshade = startTextshade.get_rect()
startRectshade.center = (517, 425)

#exit button
fontObj = pygame.font.Font("zombiecontrol.ttf",64)
exitText = fontObj.render("Exit",True, white)
exitRect = exitText.get_rect()
exitRect.center = (512, 570)
#exit button shade
fontObj = pygame.font.Font("zombiecontrol.ttf",64)
exitTextshade = fontObj.render("Exit",True, white)
exitRectshade = exitTextshade.get_rect()
exitRectshade.center = (517, 575) 
sceneNumber = 0
#Hunger
fontObj2 = pygame.font.Font("zombiecontrol.ttf", 32)
hungerText = fontObj2.render("Hunger", True, white)
hungerRect = hungerText.get_rect()
hungerRect.center = (135,46)
#P
wayObj = pygame.font.Font("zombiecontrol.ttf", 100)
wayText = wayObj.render("P", True, white)
wayRect = wayText.get_rect()
wayRect.center = (106,230)
#Z
zombObj = pygame.font.Font("zombiecontrol.ttf", 100)
zombText = zombObj.render("Z", True, white)
zombRect = zombText.get_rect()
zombRect.center = (106,508)
#tutorialorno
tutObj = pygame.font.Font("zombiecontrol.ttf", 55)
tutText = tutObj.render("Do you want to play the tutorial?", True, lightpink)
tutRect = tutText.get_rect()
tutRect.center = (512,300)
#tutorialornoshade
tutshadeObj = pygame.font.Font("zombiecontrol.ttf", 55)
tutshadeText = tutshadeObj.render("Do you want to play the tutorial?", True, pink)
tutshadeRect = tutshadeText.get_rect()
tutshadeRect.center = (517,305)
#yes
yesObj = pygame.font.Font("zombiecontrol.ttf", 50)
yesText = yesObj.render("Yes", True, white)
yesRect = yesText.get_rect()
yesRect.center = (270,420)
#yesshade
yesshadeObj = pygame.font.Font("zombiecontrol.ttf", 50)
yesshadeText = yesshadeObj.render("Yes", True,somewhatdarkpink)
yesshadeRect = yesshadeText.get_rect()
yesshadeRect.center = (275,425)
#noshade
noshadeObj = pygame.font.Font("zombiecontrol.ttf", 50)
noshadeText = noshadeObj.render("No", True, somewhatdarkpink)
noshadeRect = noshadeText.get_rect()
noshadeRect.center = (735,425)
#no
noObj = pygame.font.Font("zombiecontrol.ttf", 50)
noText = noObj.render("No", True, white)
noRect = noText.get_rect()
noRect.center = (730,420)
#pmode1
p1Obj = pygame.font.Font("zombiecontrol.ttf", 70)
p1Text = p1Obj.render('"P" is path mode', True, lightpink)
p1Rect = p1Text.get_rect()
p1Rect.center = (492,360)
#pmode1shade
p1shadeObj = pygame.font.Font("zombiecontrol.ttf", 70)
p1shadeText = p1shadeObj.render('"P" is path mode', True, pink)
p1shadeRect = p1shadeText.get_rect()
p1shadeRect.center = (492,360)
#pmode2
p2Obj = pygame.font.Font("zombiecontrol.ttf", 30)
p2Text = p2Obj.render("you will move the path using this mode", True, lightpink)
p2Rect = p2Text.get_rect()
p2Rect.center = (492,360)
#zmode
zObj = pygame.font.Font("zombiecontrol.ttf", 70)
zText = zObj.render('"Z" is zombie mode', True, lightpink)
zRect = zText.get_rect()
zRect.center = (492,360)
#zmodeshade
zshadeObj = pygame.font.Font("zombiecontrol.ttf", 70)
zshadeText = zshadeObj.render('"Z" is zombie mode', True, pink)
zshadeRect = zshadeText.get_rect()
zshadeRect.center = (492,360)
#zmode2
z2Obj = pygame.font.Font("zombiecontrol.ttf", 25)
z2Text = z2Obj.render("you will control the zombie body using this mode", True, lightpink)
z2Rect = z2Text.get_rect()
z2Rect.center = (492,360)
#wtxt
wObj = pygame.font.Font("zombiecontrol.ttf", 25)
wText = wObj.render("W - Up", True, lightpink)
wRect = wText.get_rect()
#atxt
aObj = pygame.font.Font("zombiecontrol.ttf", 25)
aText = aObj.render("A - Left", True, lightpink)
aRect = aText.get_rect()
#stxt
sObj = pygame.font.Font("zombiecontrol.ttf", 25)
sText = sObj.render("S - Down", True, lightpink)
sRect = sText.get_rect()
#dtxt
dObj = pygame.font.Font("zombiecontrol.ttf", 25)
dText = dObj.render("D - Right", True, lightpink)
dRect = dText.get_rect()
#qtxt
qObj = pygame.font.Font("zombiecontrol.ttf", 25)
qText = qObj.render("Q - switch between modes", True, lightpink)
qRect = qText.get_rect()
#KEYS
kObj = pygame.font.Font("zombiecontrol.ttf", 150)
kText = kObj.render("Controls", True, lightpink)
kRect = kText.get_rect()
#keysshade
kshadeObj = pygame.font.Font("zombiecontrol.ttf", 150)
kshadeText = kshadeObj.render("Controls", True, pink)
kshadeRect = kshadeText.get_rect()
#objective
oObj = pygame.font.Font("zombiecontrol.ttf", 30)
oText = oObj.render("Your objective is to led the zombie before he hungers to death", True, lightpink)
oRect = oText.get_rect()
#ready
readyObj = pygame.font.Font("zombiecontrol.ttf",80)
readyText = readyObj.render("Are you ready?", True, lightpink)
readyRect = readyText.get_rect()
#readyshade
readyshadeObj = pygame.font.Font("zombiecontrol.ttf",80)
readyshadeText = readyshadeObj.render("Are you ready?", True, pink)
readyshadeRect = readyshadeText.get_rect()
#play
playObj = pygame.font.Font("zombiecontrol.ttf",70)
playText = playObj.render("Yes", True, white)
playRect = playText.get_rect()
#playshade
playshadeObj = pygame.font.Font("zombiecontrol.ttf",70)
playshadeText = playshadeObj.render("Yes", True, somewhatdarkpink)
playshadeRect = playshadeText.get_rect()
#3
_3Obj = pygame.font.Font("zombiecontrol.ttf",128)
_3Text = _3Obj.render("3", True, white)
_3Rect = _3Text.get_rect()
#tutorial controls note
noteObj = pygame.font.Font("zombiecontrol.ttf", 20)
noteText = noteObj.render("***The path must be completed before switching to zombie mode***", True, lightpink)
noteRect = noteText.get_rect()
#restart button
restObj = pygame.font.Font("zombiecontrol.ttf",64)
restText = restObj.render("Restart",True, white)
restRect = restText.get_rect()
restRect.center = (512, 420)
#exit button shade
restshadeObj = pygame.font.Font("zombiecontrol.ttf",64)
restTextshade = restshadeObj.render("Restart",True, somewhatdarkpink)
restRectshade = restTextshade.get_rect()
restRectshade.center = (517, 425) 
#------------------------------UI/Var-----------------------------------------
gamestart = False
isholdstartbutton = False
tutorialstep = 1
positionxh = 210
path = True
zombie = False
hunger1 = 600
timecounter = 0
finTutorial = False
px = 106
py = 230
ptx = 512
p1ty = 300
p2ty = 400
zx = 106
zy = 508
ztx = 512
z1ty = 300
z2ty = 400
controlx = 512
controly = 350
objectivex = 512
objectivey = 384
playx = 512
playy = 300
gameEnd = False
numx = 512
numy = 384
timer = 0
count3x = 0
count2x = 0
count1x = 0
countgo = 0
playButton = 0
timer2x2 = 0

#main loop
while True:
    LevelData = LevelDataList [currentLevel]
    LevelRightData = LevelDataRight[currentLevel]
    
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
            startText = fontObj.render("Start",True, verylightpink)
            startTextshade = fontObj.render("Start",True, somewhatdarkpink)
        elif exitButton.collidepoint(mousePos) == True:
            exitText = fontObj.render("Exit",True, verylightpink)
            exitTextshade = fontObj.render("Exit",True, somewhatdarkpink)
        else:
            startText = fontObj.render("Start",True, white)
            startTextshade = fontObj.render("Start",True, somewhatdarkpink)
            exitText = fontObj.render("Exit",True, white)
            exitTextshade = fontObj.render("Exit",True, somewhatdarkpink)
            
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
    #tutorial game
    if sceneNumber == 1:
        gameDisplay.blit(brainpic,(0,0))
        pygame.draw.rect(gameDisplay, white, (212,84,600,600))
        if finTutorial == True:
            timecounter +=1            
            if timecounter >= 1:
                if hunger1 > 0:
                    hunger1 -= (600.0/(120.0*60))
                    timecounter = 0
                    positionxh = 210
        if hunger1 <= 0:
            positionxh = 2000
        if hunger1 >= 150:    
            pygame.draw.rect(gameDisplay, lime, (positionxh,30,hunger1,30))
            hungerText = fontObj2.render("Hunger", True, lime)
            gameDisplay.blit(hungerText, hungerRect)
        else:
            pygame.draw.rect(gameDisplay, red, (positionxh,30,hunger1,30))
            hungerText = fontObj2.render("Hunger", True, red)
            gameDisplay.blit(hungerText, hungerRect)
        if (path == True) and (zombie == False):
            pygame.draw.circle(gameDisplay, lightpink, (106,239), 80,0)
            wayText = wayObj.render("P", True, white)
            gameDisplay.blit(wayText, wayRect)
            pygame.draw.circle(gameDisplay, darkpink, (106,508), 80,0)
            gameDisplay.blit(zombText, zombRect)
            zombText = zombObj.render("Z", True, grey)
        elif (path == False) and (zombie == True):
            pygame.draw.circle(gameDisplay, darkpink, (106,239), 80,0)
            wayText = wayObj.render("P", True, grey)
            gameDisplay.blit(wayText, wayRect)
            pygame.draw.circle(gameDisplay, lightpink, (106,508), 80,0)
            gameDisplay.blit(zombText, zombRect)
            zombText = zombObj.render("Z", True, white)
        overlay = pygame.Surface((1024,768), pygame.SRCALPHA)
        overlay.fill((0,0,0,220))
        gameDisplay.blit(overlay, (0,0))
        gameDisplay.blit(tutshadeText,tutshadeRect)        
        gameDisplay.blit(tutText,tutRect)
        gameDisplay.blit(yesshadeText,yesshadeRect)
        gameDisplay.blit(yesText,yesRect)
        #yesbutton
        yesButton = pygame.Rect(225,390,90,55)
        #nobutton
        noButton = pygame.Rect(700,395,58,45)
        gameDisplay.blit(noshadeText,noshadeRect)
        gameDisplay.blit(noText,noRect)
        mousePos = pygame.mouse.get_pos()
        if yesButton.collidepoint(mousePos) == True:
            yesText = yesObj.render("Yes",True, verylightpink)
            yesshadeText = yesObj.render("Yes",True, somewhatdarkpink)
        elif noButton.collidepoint(mousePos) == True:
            noText = noObj.render("no",True, verylightpink)
            noshadeText = noObj.render("no",True, somewhatdarkpink)    
        else:
            yesText = yesObj.render("Yes",True,white)
            yesshadeText = yesObj.render("Yes",True,somewhatdarkpink)
            noText = noObj.render("no",True,white)
            noshadeText = noObj.render("no",True,somewhatdarkpink)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if finTutorial == False:
                if event.type == MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    print(mousePos)
                    if yesButton.collidepoint(mousePos) == True:
                        print("Start Tutorial")
                        sceneNumber += 1
                    elif noButton.collidepoint(mousePos) == True:
                        print("Start game right away")
                        sceneNumber += 2
            if finTutorial == True:
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        if (path == True) and (zombie == False):
                            path = False
                            zombie = True
                        elif (path == False) and (zombie == True):
                            path = True
                            zombie = False
                elif event.type == MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    print(mousePos)
    #tutorial                
    if sceneNumber == 2:
        gameDisplay.blit(brainpic,(0,0))
        pygame.draw.rect(gameDisplay, white, (212,84,600,600))
        timecounter +=1            
        if timecounter >= 1:
            if hunger1 > 0:
                hunger1 -= (600.0/(50.0*60))
                timecounter = 0
            positionxh = 210
            if hunger1 <= 0:
                positionxh = 2000
            if hunger1 >= 150:    
                pygame.draw.rect(gameDisplay, lime, (positionxh,30,hunger1,30))
                hungerText = fontObj2.render("Hunger", True, lime)
                gameDisplay.blit(hungerText, hungerRect)
            else:
                pygame.draw.rect(gameDisplay, red, (positionxh,30,hunger1,30))
                hungerText = fontObj2.render("Hunger", True, red)
                gameDisplay.blit(hungerText, hungerRect)
        if path == True:
            pygame.draw.circle(gameDisplay, lime, (106,230), 80,0)
            wayText = wayObj.render("P", True, white)
            gameDisplay.blit(wayText, wayRect)
            pygame.draw.circle(gameDisplay, dark_green, (106,508), 80,0)
            gameDisplay.blit(zombText, zombRect)
            zombText = zombObj.render("Z", True, grey)
        if zombie == True:
            pygame.draw.circle(gameDisplay, lime, (106,230), 80,0)
            wayText = wayObj.render("P", True, grey)
            gameDisplay.blit(wayText, wayRect)
            pygame.draw.circle(gameDisplay, dark_green, (106,508), 80,0)
            gameDisplay.blit(zombText, zombRect)
            zombText = zombObj.render("Z", True, white)
        #Overlay    
        overlay = pygame.Surface((1024,768), pygame.SRCALPHA)
        overlay.fill((0,0,0,220))
        gameDisplay.blit(overlay, (0,0))
        if tutorialstep == 1:
            pygame.draw.circle(gameDisplay, lime, (px,py), 80,0)
            wayText = wayObj.render("P", True, white)
            gameDisplay.blit(wayText, wayRect)
            p1Rect.center = (ptx,p1ty)
            p1shadeRect.center = (ptx+5,p1ty+5)
            gameDisplay.blit(p1shadeText,p1shadeRect)
            gameDisplay.blit(p1Text, p1Rect)
            p2Rect.center = (ptx,p2ty)
            gameDisplay.blit(p2Text, p2Rect)
        if tutorialstep == 2:
            px = 2000
            py = 2000
            ptx = 2000
            pygame.draw.circle(gameDisplay, lime, (zx,zy), 80,0)
            zombText = zombObj.render("Z", True, white)
            gameDisplay.blit(zombText, zombRect)
            zshadeRect.center = (ztx+5,z1ty+5)
            gameDisplay.blit(zshadeText,zshadeRect)
            zRect.center = (ztx,z1ty)
            gameDisplay.blit(zText,zRect)
            z2Rect.center = (ztx,z2ty)
            gameDisplay.blit(z2Text,z2Rect)
        if tutorialstep == 3:
            zx = 2000
            zy = 2000
            ztx = 2000
            kshadeRect.center = (controlx + 5, controly -120)
            kRect.center = (controlx,controly-125)
            gameDisplay.blit(kshadeText, kshadeRect)
            gameDisplay.blit(kText,kRect)
            wRect.center = (controlx,controly+25)
            gameDisplay.blit(wText,wRect)
            aRect.center = (controlx,controly+75)
            gameDisplay.blit(aText,aRect)
            sRect.center = (controlx,controly+125)
            gameDisplay.blit(sText,sRect)
            dRect.center = (controlx,controly+175)
            gameDisplay.blit(dText,dRect)
            qRect.center = (controlx,controly+225)
            gameDisplay.blit(qText,qRect)
            noteRect.center = (controlx,controly + 250)
            gameDisplay.blit(noteText,noteRect)
        if tutorialstep == 4:
            controlx = 2000
            oRect.center = (objectivex,objectivey)
            gameDisplay.blit(oText,oRect)
        if tutorialstep == 5:
            objectivex = 2000
            gameDisplay.blit(readyshadeText,readyshadeRect)
            gameDisplay.blit(readyText,readyRect)
            readyshadeRect.center = (playx+5,playy+5)
            readyRect.center = (playx,playy)
            playshadeRect.center = (playx+5, playy +155)
            gameDisplay.blit(playshadeText,playshadeRect)
            playRect.center = (playx, playy +150)
            gameDisplay.blit(playText,playRect)
            mousePos = pygame.mouse.get_pos()
            playButton = pygame.Rect(449,416,123,74)
            if playButton.collidepoint(mousePos) == True:
                playText = playObj.render("Yes",True, verylightpink)
                playTextshade = playshadeObj.render("Yes",True, somewhatdarkpink)
            else:
                playText = playObj.render("Yes", True, white)
                playshadeText = playshadeObj.render("Yes", True, somewhatdarkpink)     
        pygame.display.update()    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_q:
                    if (path == True) and (zombie == False):
                        path = False
                        zombie = True
                    elif (path == False) and (zombie == True):
                        path = True
                        zombie = False
                tutorialstep += 1         
            if event.type == MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                print(mousePos)
                if event.button != 4 and event.button != 5:
                    if tutorialstep < 5:
                        tutorialstep += 1
                        print("Click")
                    elif tutorialstep == 5 and playButton.collidepoint(mousePos) == True:
                        print("Next Game")
                        sceneNumber += 1    
    #first game, template
    if sceneNumber == 3:
        gameDisplay.blit(brainpic,(0,0))
        pygame.draw.rect(gameDisplay, white, (212,84,600,600))
        pygame.draw.circle(gameDisplay, lightpink, (106,230), 80,0)
        wayText = wayObj.render("P", True, white)
        gameDisplay.blit(wayText, wayRect)
        pygame.draw.circle(gameDisplay, pink, (106,508), 80,0)
        gameDisplay.blit(zombText, zombRect)
        zombText = zombObj.render("Z", True, grey)
        timer += 3 
        if gamestart == False:
            if (timer >= 0) and (timer < 60):
                print("3")
                gameDisplay.blit(count3pic, (count3x,0))
            if (timer >= 60) and (timer < 120):
                count3x = 2000
                print("2")
                gameDisplay.blit(count2pic, (count2x,0))
            if (timer >= 120) and (timer < 180):
                count2x = 2000
                print("1")
                gameDisplay.blit(count1pic, (count1x,0))
            if (timer >= 180) and (timer <240):
                count1x = 2000
                print("Go")
                gameDisplay.blit(gopic, (countgo,0))
            if timer == 240:
                countgo = 2000
                gamestart = True  
        if gamestart == True:
#--------------------------LEVEL-ONE--------------------------------------------------------------------------
            if currentLevel == 0:
                for row in range( 0 , 2 , 1 ) :
                    for column in range( 0 , 2 , 1 ) :
                        # Draw the game level
                        if LevelData[ row ][ column ] == "B1" :
                            gameDisplay.blit( Bim1, ( (blockWidth * column)+ 212, (blockHeight * row)+84))
                        if LevelData [ row ] [ column ] == "B2":
                            gameDisplay.blit( Bim2, (( blockWidth * column)+ 212, (blockHeight * row)+84))
                        if LevelData[ row ] [ column ] == "B3":
                            gameDisplay.blit(Bim3, ((blockWidth * column) + 212, (blockHeight * row)+84))

                        elif LevelData[ row ][ column ] == "A1" :
                            if arrowAtRow == -1 and arrowAtColumn == -1:
                                arrowAtRow = row
                                arrowAtColumn = column 
                    
                gameDisplay.blit( Aim1, ( (blockWidth * arrowAtColumn)+212, (blockHeight * arrowAtRow)+84))
#--------------------------------LEVEL-TWO-------------------------------------------------------------------------------
            if currentLevel == 1:
                for row in range( 0 , 3 , 1 ) :
                    for column in range( 0 , 3 , 1 ) :
                        # Draw the game level
                        if LevelData[ row ][ column ] == "B1" :
                            gameDisplay.blit( Bim1x, ( (blockWidth3 * column) + 212, (blockHeight3 * row) + 84))
                        if LevelData [ row ] [ column ] == "B2":
                            gameDisplay.blit( Bim2x, ( (blockWidth3 * column) + 212 , (blockHeight3 * row) + 84))
                        if LevelData[ row ] [ column ] == "B3":
                            gameDisplay.blit(Bim3x, ((blockWidth3 * column) + 212 , (blockHeight3 * row) + 84))
                        if LevelData[ row ] [ column ] == "B4":
                            gameDisplay.blit(Bim4x, ((blockWidth3 * column) + 212 , (blockHeight3 * row) + 84))
                        if LevelData[ row ] [ column ] == "B5":
                            gameDisplay.blit(Bim5x, ((blockWidth3 * column) + 212 , (blockHeight3 * row) +84))
                        if LevelData[ row ] [ column ] == "B6":
                            gameDisplay.blit(Bim6x, ((blockWidth3 * column) + 212 , (blockHeight3 * row) + 84))
                        if LevelData[ row ] [ column ] == "B8":
                            gameDisplay.blit(Bim8x, ((blockWidth3 * column) + 212 , (blockHeight3 * row) + 84))
                        if LevelData[ row ] [ column ] == "B9":
                            gameDisplay.blit(Bim9x, ((blockWidth3 * column) + 212 , (blockHeight3 * row) + 84))

                        elif LevelData[ row ][ column ] == "A1" :
                            if arrowAtRow == -1 and arrowAtColumn == -1:
                                arrowAtRow = row
                                arrowAtColumn = column 
                                print(arrowAtColumn, arrowAtRow)
                gameDisplay.blit( Aim1x, ( ((blockWidth3 * arrowAtColumn)+212), ((blockHeight3 * arrowAtRow)+84)))
#--------------------------------LEVEL-THREE-------------------------------------------------------------------
            if currentLevel == 2:
                for row in range( 0 , 3 , 1 ) :
                    for column in range( 0 , 3 , 1 ) :
                        # Draw the game level
                        if LevelData[ row ][ column ] == "B1" :
                            gameDisplay.blit( Bim1x1, ( (blockWidth3 * column) + 212, (blockHeight3 * row) + 84))
                        if LevelData [ row ] [ column ] == "B2":
                            gameDisplay.blit( Bim2x1, ( (blockWidth3 * column) + 212, (blockHeight3 * row) + 84))
                        if LevelData[ row ] [ column ] == "B3":
                            gameDisplay.blit(Bim3x1, ((blockWidth3 * column) +212, (blockHeight3 * row) + 84))
                        if LevelData[ row ] [ column ] == "B4":
                            gameDisplay.blit(Bim4x1, ((blockWidth3 * column) + 212 , (blockHeight3 * row) + 84))
                        if LevelData[ row ] [ column ] == "B5":
                            gameDisplay.blit(Bim5x1, ((blockWidth3 * column) + 212, (blockHeight3 * row)+84))
                        if LevelData[ row ] [ column ] == "B6":
                            gameDisplay.blit(Bim6x1, ((blockWidth3 * column) +212, (blockHeight3 * row) +84))
                        if LevelData[ row ] [ column ] == "B8":
                            gameDisplay.blit(Bim8x1, ((blockWidth3 * column) +212, (blockHeight3 * row) +84))
                        if LevelData[ row ] [ column ] == "B9":
                            gameDisplay.blit(Bim9x1, ((blockWidth3 * column) +212, (blockHeight3 * row) +84))

                        elif LevelData[ row ][ column ] == "A1" :
                            if arrowAtRow == -1 and arrowAtColumn == -1:
                                arrowAtRow = row
                                arrowAtColumn = column 
                    
                    gameDisplay.blit( Aim1x1, (( blockWidth3 * arrowAtColumn)+212, (blockHeight3 * arrowAtRow) +84))

#--------------------------------------------------------------------------------------------------------
            if (zombie == False):
                timecounter +=1            
                if timecounter >= 1:
                    if hunger1 > 0:
                        hunger1 -= (600.0/(50.0*60))
                        timecounter = 0
                    positionxh = 210
                    if hunger1 <= 0:
                        positionxh = 2000
                        print("Game End")
                        gameEnd == "True"
                        sceneNumber += 1
                        print(sceneNumber)
                    if hunger1 >= 150:    
                        pygame.draw.rect(gameDisplay, lime, (positionxh,30,hunger1,30))
                        hungerText = fontObj2.render("Hunger", True, lime)
                        gameDisplay.blit(hungerText, hungerRect)
                    if hunger1 < 150:
                        pygame.draw.rect(gameDisplay, red, (positionxh,30,hunger1,30))
                        hungerText = fontObj2.render("Hunger", True, red)
                        gameDisplay.blit(hungerText, hungerRect)
            if (path == True):
                pygame.draw.circle(gameDisplay, lime, (106,230), 80,0)
                wayText = wayObj.render("P", True, white)
                gameDisplay.blit(wayText, wayRect)
                pygame.draw.circle(gameDisplay, dark_green, (106,508), 80,0)
                gameDisplay.blit(zombText, zombRect)
                zombText = zombObj.render("Z", True, grey)
            if (zombie == True):
                pygame.draw.circle(gameDisplay, dark_green, (106,230), 80,0)
                wayText = wayObj.render("P", True, grey)
                gameDisplay.blit(wayText, wayRect)
                pygame.draw.circle(gameDisplay, lime, (106,508), 80,0)
                gameDisplay.blit(zombText, zombRect)
                zombText = zombObj.render("Z", True, white)
                timer2x2 += 1
                if currentLevel == 0:
                    if (timer2x2 >= 0) and (timer2x2 < 21):
                        gameDisplay.blit(ani1pic,(212,84))
                    if (timer2x2 >= 21) and (timer2x2 < 41):
                        gameDisplay.blit(ani2pic, (212,84))
                    if (timer2x2 >= 41) and (timer2x2 < 61):
                        gameDisplay.blit(ani3pic, (212,84))
                    if (timer2x2 >= 61) and (timer2x2 < 81):
                        gameDisplay.blit(ani4pic, (212,84))
                    if (timer2x2 >= 81) and (timer2x2 < 101):
                        gameDisplay.blit(ani5pic, (212,84))
                    if (timer2x2 >= 101) and (timer2x2 < 121):
                        gameDisplay.blit(ani6pic, (212,84))
                    if (timer2x2 >= 121) and (timer2x2 < 141):
                        gameDisplay.blit(ani7pic, (212,84))
                    if (timer2x2 >= 141) and (timer2x2 < 161):
                        gameDisplay.blit(ani8pic, (212,84))
                    if (timer2x2 >= 161) and (timer2x2 < 181):
                        gameDisplay.blit(ani9pic, (212,84))
                    if (timer2x2 >= 181):
                        zombie = False
                        currentLevel += 1
                        arrowAtRow = -1
                        arrowAtColumn = -1
                        timer2x2 = 0
                if currentLevel == 1:
                    if (timer2x2 >= 0) and (timer2x2 < 21):
                        gameDisplay.blit(ani21pic,(212,84))
                    if (timer2x2 >= 21) and (timer2x2 < 41):
                        gameDisplay.blit(ani22pic, (212,84))
                    if (timer2x2 >= 41) and (timer2x2 < 61):
                        gameDisplay.blit(ani23pic, (212,84))
                    if (timer2x2 >= 61) and (timer2x2 < 81):
                        gameDisplay.blit(ani24pic, (212,84))
                    if (timer2x2 >= 81) and (timer2x2 < 101):
                        gameDisplay.blit(ani25pic, (212,84))
                    if (timer2x2 >= 101) and (timer2x2 < 121):
                        gameDisplay.blit(ani26pic, (212,84))
                    if (timer2x2 >= 121) and (timer2x2 < 141):
                        gameDisplay.blit(ani27pic, (212,84))
                    if (timer2x2 >= 141) and (timer2x2 < 161):
                        gameDisplay.blit(ani28pic, (212,84))
                    if (timer2x2 >= 161) and (timer2x2 < 181):
                        gameDisplay.blit(ani29pic, (212,84))
                    if (timer2x2 >= 181):
                        zombie = False
                        currentLevel += 1
                        arrowAtRow = -1
                        arrowAtColumn = -1
                        timer2x2 = 0
                if currentLevel == 2:
                    if (timer2x2 >= 0) and (timer2x2 < 21):
                        gameDisplay.blit(ani31pic,(212,84))
                    if (timer2x2 >= 21) and (timer2x2 < 41):
                        gameDisplay.blit(ani32pic, (212,84))
                    if (timer2x2 >= 41) and (timer2x2 < 61):
                        gameDisplay.blit(ani33pic, (212,84))
                    if (timer2x2 >= 61) and (timer2x2 < 81):
                        gameDisplay.blit(ani34pic, (212,84))
                    if (timer2x2 >= 81) and (timer2x2 < 101):
                        gameDisplay.blit(ani35pic, (212,84))
                    if (timer2x2 >= 101) and (timer2x2 < 121):
                        gameDisplay.blit(ani36pic, (212,84))
                    if (timer2x2 >= 121) and (timer2x2 < 141):
                        gameDisplay.blit(ani37pic, (212,84))
                    if (timer2x2 >= 141) and (timer2x2 < 161):
                        gameDisplay.blit(ani38pic, (212,84))
                    if (timer2x2 >= 161) and (timer2x2 < 181):
                        gameDisplay.blit(ani39pic, (212,84))
                    if (timer2x2 >= 181):
                        zombie = False
                        sceneNumber += 2
                        arrowAtRow = -1
                        arrowAtColumn = -1
                        timer2x2 = 0
                
        pygame.display.update()    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
#--------------------------------------------------2x2------------------------------------------------------
                if currentLevel == 0:
                    if gameEnd == False:     
                        if path == True:
                            if event.key == K_q:
                                Rightcounter = 0
                
                                for row in range( 0 , 2 , 1 ) :
                                    for column in range( 0 , 2 , 1 ) :
                                        if LevelData[ row ][ column ] == LevelRightData [row] [column] :
                                            Rightcounter += 1
                                print(Rightcounter)
                                if Rightcounter >= 4:
                                    zombie = True
                                    arrowAtColumn = -1
                                    arrowAtRow = -1
                                else:
                                    print("The path is not correct!")

                            if event.key == K_w:        
                                if arrowAtRow > 0:
                                    temp = LevelData [arrowAtRow-1][arrowAtColumn]
                                    LevelData [arrowAtRow-1][arrowAtColumn] = LevelData [arrowAtRow][arrowAtColumn]
                                    LevelData [arrowAtRow][arrowAtColumn] = temp
                                    arrowAtRow += -1
                                    
                            if event.key == K_s :
                                if arrowAtRow < 600/blockWidth - 1:
                                    temp = LevelData [arrowAtRow+1][arrowAtColumn]
                                    LevelData [arrowAtRow+1][arrowAtColumn] = LevelData [arrowAtRow][arrowAtColumn]
                                    LevelData [arrowAtRow][arrowAtColumn] = temp
                                    arrowAtRow += 1
                                    
                            if event.key == K_d :
                                if arrowAtColumn < 600/blockWidth - 1:
                                    temp = LevelData [arrowAtRow][arrowAtColumn + 1]
                                    LevelData [arrowAtRow][arrowAtColumn + 1] = LevelData [arrowAtRow][arrowAtColumn]
                                    LevelData [arrowAtRow][arrowAtColumn] = temp
                                    arrowAtColumn += 1
                                
                            if event.key == K_a :
                                if arrowAtColumn > 0 :
                                    temp = LevelData [arrowAtRow][arrowAtColumn - 1]
                                    LevelData [arrowAtRow][arrowAtColumn - 1] = LevelData [arrowAtRow][arrowAtColumn]
                                    LevelData [arrowAtRow][arrowAtColumn] = temp
                                    arrowAtColumn += -1            
#--------------------------------------------------3x3------------------------------------------------------------------ 
                if currentLevel >= 1:
                    if gameEnd == False:     
                        if path == True:
                            if event.key == K_q:
                                print("click q path")
                                Rightcounter = 0
                                for row in range( 0 , 3 , 1 ) :
                                    for column in range( 0 , 3 , 1 ) :
                                        if LevelData[ row ][ column ] == LevelRightData [row] [column] :
                                            Rightcounter += 1
                                print(Rightcounter)
                                if Rightcounter >= 9:
                                    zombie = True
                                    arrowAtColumn = -1
                                    arrowAtRow = -1
                                else:
                                    print("The path is not correct!")
                            if event.key == K_w :
                                if arrowAtRow > 0:
                                    temp = LevelData [arrowAtRow-1][arrowAtColumn]
                                    LevelData [arrowAtRow-1][arrowAtColumn] = LevelData [arrowAtRow][arrowAtColumn]
                                    LevelData [arrowAtRow][arrowAtColumn] = temp
                                    arrowAtRow += -1
                                
                            if event.key == K_s :
                                if arrowAtRow < 600/blockWidth3 - 1:
                                    temp = LevelData [arrowAtRow+1][arrowAtColumn]
                                    LevelData [arrowAtRow+1][arrowAtColumn] = LevelData [arrowAtRow][arrowAtColumn]
                                    LevelData [arrowAtRow][arrowAtColumn] = temp
                                    arrowAtRow += 1
                            
                            if event.key == K_d :
                                if arrowAtColumn < 600/blockWidth3 - 1:
                                    temp = LevelData [arrowAtRow][arrowAtColumn + 1]
                                    LevelData [arrowAtRow][arrowAtColumn + 1] = LevelData [arrowAtRow][arrowAtColumn]
                                    LevelData [arrowAtRow][arrowAtColumn] = temp
                                    arrowAtColumn += 1
                        
                            if event.key == K_a :
                                if arrowAtColumn > 0 :
                                    temp = LevelData [arrowAtRow][arrowAtColumn - 1]
                                    LevelData [arrowAtRow][arrowAtColumn - 1] = LevelData [arrowAtRow][arrowAtColumn]
                                    LevelData [arrowAtRow][arrowAtColumn] = temp
                                    arrowAtColumn += -ACTIVEEVENT
#-------------------------------------------------------------------------------------------------------------------------
            if event.type == MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                print(mousePos)
    if sceneNumber == 4:
        pygame.draw.rect(gameDisplay, black, (0,0,1024,768))
        gameDisplay.blit(overpic, (0,-175))
        gameDisplay.blit(restTextshade, restRectshade)
        gameDisplay.blit(restText, restRect)
        gameDisplay.blit(exitTextshade, exitRectshade)
        gameDisplay.blit(exitText, exitRect)
        restButton = pygame.Rect(400,390,240,71)
        exitButton = pygame.Rect(440,540,140,71)
        mousePos = pygame.mouse.get_pos()
        if restButton.collidepoint(mousePos) == True:
            restText = restObj.render("Restart",True, verylightpink)
            restTextshade = restshadeObj.render("Restart",True, somewhatdarkpink)
        elif exitButton.collidepoint(mousePos) == True:
            exitText = fontObj.render("Exit",True, verylightpink)
            exitTextshade = fontObj.render("Exit",True, somewhatdarkpink)
        else:
            restText = restObj.render("Restart",True, white)
            restTextshade = restshadeObj.render("Restart",True, somewhatdarkpink)
            exitText = fontObj.render("Exit",True, white)
            exitTextshade = fontObj.render("Exit",True, somewhatdarkpink)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                print(mousePos)
                if restButton.collidepoint(mousePos) == True:
                    sceneNumber -= 1
                    hunger1 = 600
                    gamestart = False
                    timer = 0
                    count3x = 0
                    count2x = 0
                    count1x = 0
                    countgo = 0
                if exitButton.collidepoint(mousePos) == True:
                    pygame.quit()
                    sys.exit()
    if sceneNumber >= 5:
        gameDisplay.blit(vicpic, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    fpsClock.tick(fps)
          
