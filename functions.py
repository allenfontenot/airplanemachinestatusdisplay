import pygame
import pygame.gfxdraw


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
        f = pygame.font.SysFont("freesans", 27)
        #text is 'READY'
        #color is green
        pygame.gfxdraw.filled_circle(background,circleTwox,circley,radius,colorGreen)
        circleTwoText = f.render('READY',1,(5,5,5))
        circleTwoTextpos = circleTwoText.get_rect()
        circleTwoTextpos.center = (circleTwox,circley)
        background.blit(circleTwoText,circleTwoTextpos)
    elif state is False:
        f = pygame.font.SysFont("freesans", 21)
        #text is 'IN PROGRESS'
        #color is YELLOW
        pygame.gfxdraw.filled_circle(background,circleTwox,circley,radius,colorYellow)
        circleTwoText = f.render('RUNNING',1,colorBackground)
        circleTwoTextpos = circleTwoText.get_rect()
        circleTwoTextpos.center = (circleTwox,circley)
        background.blit(circleTwoText,circleTwoTextpos)

def buttonThree(state):
    if state is True:
        f = pygame.font.SysFont("freesans", 32)
        #text is 'RUN'
        #color is green
        pygame.gfxdraw.filled_circle(background,circleThreex,circley,radius,colorGreen)
        circleThreeText = f.render('RUN',1,(5,5,5))
        circleThreeTextpos = circleThreeText.get_rect()
        circleThreeTextpos.center = (circleThreex,circley)
        background.blit(circleThreeText,circleThreeTextpos)
    elif state is False:
        f = pygame.font.SysFont("freesans", 32)
        #text is 'TEST'
        #color is YELLOW
        pygame.gfxdraw.filled_circle(background,circleThreex,circley,radius,colorYellow)
        circleThreeText = f.render('TEST',1,colorBackground)
        circleThreeTextpos = circleThreeText.get_rect()
        circleThreeTextpos.center = (circleThreex,circley)
        background.blit(circleThreeText,circleThreeTextpos)

def buttonFour(state):
    if state is True:
        f = pygame.font.SysFont("freesans", 30)
        #text is 'RESET'
        pygame.gfxdraw.filled_circle(background,circleFourx,circley,radius,colorBlack)
        circleFourText = f.render('RESET',1,colorBackground)
        circleFourTextpos = circleFourText.get_rect()
        circleFourTextpos.center = (circleFourx,circley)
        background.blit(circleFourText,circleFourTextpos)
    elif state is False:
        f = pygame.font.SysFont("freesans", 30)
        #text is 'RESET'
        pygame.gfxdraw.filled_circle(background,circleFourx,circley,radius,colorBlack)
        circleFourText = f.render('RESET',1,colorBackground)
        circleFourTextpos = circleFourText.get_rect()
        circleFourTextpos.center = (circleFourx,circley)
        background.blit(circleFourText,circleFourTextpos)
