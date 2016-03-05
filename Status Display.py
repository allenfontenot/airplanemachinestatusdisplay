import pygame
import pygame.gfxdraw
import sys
import time

x_size = 480
y_size = 320

radius = 50
space = 18

colorGreen = (169, 204, 80)
colorRed = (214,51,87)
colorBlack = (0,0,0)
colorBackground = (180,180,180)
colorYellow = (245,245,73)

circley = y_size - (radius + 10)
circleOnex = 1*radius + space-3

circleTwox = 3*radius + 2*space-3

circleThreex = 5*radius + 3*space-3

circleFourx = 7*radius + 4*space-3

def buttonOne(state):
    if state is True:
        f = pygame.font.SysFont("freesans", 32)
        #color is green
        pygame.gfxdraw.filled_circle(background,circleOnex,circley,radius,colorGreen)
        #text is ON
        circleOneText = f.render('ON',1,(5,5,5))
        circleOneTextpos = circleOneText.get_rect()
        circleOneTextpos.center = (circleOnex,circley)
        background.blit(circleOneText,circleOneTextpos)
    elif state is False:
        f = pygame.font.SysFont("freesans", 32)
        #color is black
        pygame.gfxdraw.filled_circle(background,circleOnex,circley,radius,colorBlack)
        #text is OFF
        circleOneText = f.render('OFF',1,colorBackground)
        circleOneTextpos = circleOneText.get_rect()
        circleOneTextpos.center = (circleOnex,circley)
        background.blit(circleOneText,circleOneTextpos)

def buttonTwo(state):
    if state is True:
        f = pygame.font.SysFont("freesans", 32)
        #color is green
        pygame.gfxdraw.filled_circle(background,circleTwox,circley,radius,colorGreen)
        #text is ON
        circleTwoText = f.render('READY',1,(5,5,5))
        circleTwoTextpos = circleTwoText.get_rect()
        circleTwoTextpos.center = (circleTwox,circley)
        background.blit(circleTwoText,circleTwoTextpos)
    elif state is False:
        f = pygame.font.SysFont("freesans", 24)
        #color is black
        pygame.gfxdraw.filled_circle(background,circleTwox,circley,radius,colorYellow)
        #text is OFF
        circleTwoText = f.render('RUNNING',1,colorBackground)
        circleTwoTextpos = circleTwoText.get_rect()
        circleTwoTextpos.center = (circleTwox,circley)
        background.blit(circleTwoText,circleTwoTextpos)
    #if state is True:
        #text is 'READY'
        #color is green
    #elif state is False:
        #text is 'IN PROGRESS'
        #color is YELLOW



def exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN:
            pygame.quit()
            sys.exit()



pygame.init()
lcd = pygame.display.set_mode((480, 320))
background = pygame.Surface(lcd.get_size())
background = background.convert()

background.fill(colorBackground)

launchSquare = pygame.Surface((50,110))
launchSquare.fill((127,127,127))
background.blit(launchSquare, (50,50))

foldSquare = pygame.Surface((150,110))
foldSquare.fill((127,127,127))
background.blit(foldSquare, (110,50))

channel = pygame.Surface((140,40))
channel.fill((127,127,127))
background.blit(channel, (270,85))

#toplaunchwheel
pygame.gfxdraw.filled_circle(background,410,105-31,30,(250,250,250))

#bottomlaunchwheel
pygame.gfxdraw.filled_circle(background,410,105+31,30,(250,250,250))

#sensor 1
pygame.gfxdraw.filled_circle(background,75,105,10,(224,31,73))
#sensor 2
pygame.gfxdraw.filled_circle(background,235,105,10,(224,31,73))
#sensor 3
pygame.gfxdraw.filled_circle(background,285,105,10,(224,31,73))
#sensor 4
pygame.gfxdraw.filled_circle(background,380,105,10,(224,31,73))


#starting point
sx1 = 125
sy1 = 95

sx = 310
sy = 95

pygame.draw.polygon(background, (170, 224, 31), ((0+sx,0+sy),(0+sx,20+sy),(20+sx,20+sy),(20+sx,30+sy),(40+sx,10+sy),(20+sx,-10+sy),(20+sx,0+sy)))
pygame.draw.polygon(background, (170, 224, 31), ((0+sx1,0+sy1),(0+sx1,20+sy1),(40+sx1,20+sy1),(40+sx1,30+sy1),(60+sx1,10+sy1),(40+sx1,-10+sy1),(40+sx1,0+sy1)))

#buttons


#pygame.gfxdraw.filled_circle(background,circleTwoPos,radius,(127,127,127))
#pygame.gfxdraw.filled_circle(background,circleThreePos,radius,(127,127,127))
#pygame.gfxdraw.filled_circle(background,circleFourPos,radius,(127,127,127))



lcd.blit(background, (0,0))
pygame.display.flip()

while True:
    buttonOne(True)
    buttonTwo(True)
    lcd.blit(background, (0,0))
    pygame.display.flip()

    time.sleep(1)

    buttonOne(False)
    buttonTwo(False)
    lcd.blit(background, (0,0))
    pygame.display.flip()
    
    time.sleep(1)



exit()




#def buttonThree(state):
#    if state is True:
        #text is 'RUN'
        #color is green
#    elif state is False:
        #text is 'TEST'
        #color is YELLOW

#def buttonFour(state):
        #text is 'RESET'
