import pygame
import pygame.gfxdraw


x_size = 480
y_size = 320

radius = 50
space = 18

colorGreen = (169, 204, 80)
colorRed = (224,31,73)
colorBlack = (0,0,0)
colorBackground = (180,180,180)
colorYellow = (245,245,73)
colorWhite = (250,250,250)

#circles one and four locations are switched
circley = y_size - (radius + 10)
circleFourx = 1*radius + space-3

circleTwox = 3*radius + 2*space-3

circleThreex = 5*radius + 3*space-3

circleOnex = 7*radius + 4*space-3


lcd = pygame.display.set_mode((480, 320))
background = pygame.Surface(lcd.get_size())
background = background.convert()


def buttonOne(state):
    global speed
    if not state:
        speed = 100
    elif state:
        speed -= 5
        if speed == 0:
            speed = 100
    color = colorBlack
    textcolor = colorBackground
    text = str(speed) + '%'
    textsize = 32

    f = pygame.font.SysFont("freesans", textsize)
    pygame.gfxdraw.filled_circle(background,circleOnex,circley,radius,color)
    pygame.gfxdraw.aacircle(background,circleOnex,circley,radius,color)
    circleOneText = f.render(text,1,textcolor)
    circleOneTextpos = circleOneText.get_rect()
    circleOneTextpos.center = (circleOnex,circley)
    background.blit(circleOneText,circleOneTextpos)


def buttonTwo(state):
    if state:
        color = colorGreen
        textcolor = (5, 5, 5)
        text = 'READY'
        textsize = 27
    if not state:
        color = colorYellow
        textcolor = colorBackground
        text = 'RUNNING'
        textsize = 21

    f = pygame.font.SysFont("freesans", textsize)
    pygame.gfxdraw.filled_circle(background,circleTwox,circley,radius,color)
    pygame.gfxdraw.aacircle(background,circleTwox,circley,radius,color)

    circleTwoText = f.render(text,1,textcolor)
    circleTwoTextpos = circleTwoText.get_rect()
    circleTwoTextpos.center = (circleTwox,circley)
    background.blit(circleTwoText,circleTwoTextpos)


def buttonThree(state):
    if state:
        color = colorGreen
        textcolor = (5, 5, 5)
        text = 'RUN'
        textsize = 32
    if not state:
        color = colorYellow
        textcolor = colorBackground
        text = 'TEST'
        textsize = 32

    f = pygame.font.SysFont("freesans", textsize)
    pygame.gfxdraw.filled_circle(background,circleThreex,circley,radius,color)
    pygame.gfxdraw.aacircle(background,circleThreex,circley,radius,color)
    circleThreeText = f.render(text,1,textcolor)
    circleThreeTextpos = circleThreeText.get_rect()
    circleThreeTextpos.center = (circleThreex,circley)
    background.blit(circleThreeText,circleThreeTextpos)

def buttonFour(state):
    if not state:
        color = colorBlack
        textcolor = colorBackground
        text = 'RESET'
        textsize = 29
    if state:
        color = colorBackground
        textcolor = colorBlack
        text = 'RESET'
        textsize = 29

    f = pygame.font.SysFont("freesans", textsize)
    #text is 'RESET'
    pygame.gfxdraw.filled_circle(background, circleFourx, circley, radius, color)
    pygame.gfxdraw.aacircle(background, circleFourx, circley, radius, color)
    circleFourText = f.render(text, 1, textcolor)
    circleFourTextpos = circleFourText.get_rect()
    circleFourTextpos.center = (circleFourx, circley)
    background.blit(circleFourText, circleFourTextpos)


def drawSensor(location,state):
    x = [75,235,285,380]
    if state:
        color = colorGreen
    elif not state:
        color = colorBackground
    pygame.gfxdraw.filled_circle(background,x[location],105,10,color)
    pygame.gfxdraw.aacircle(background,x[location],105,10,color)

def drawarrow(location, state):
    if location == 1:
        x = 125
        y = 95
    elif location ==2:
        x = 305
        y = 95

    if state:
        color = colorGreen
    elif not state:
        color = colorBackground

    pygame.draw.polygon(background, color, ((0+x,0+y),(0+x,20+y),(40+x,20+y),(40+x,30+y),(60+x,10+y),(40+x,-10+y),(40+x,0+y)))


def insidecircle(x,y):
    radiussquared = radius**2
    insidecircleone = (x-circleOnex)**2 + (y-circley)**2
    insidecircletwo = (x-circleTwox)**2 + (y-circley)**2
    insidecirclethree = (x-circleThreex)**2 + (y-circley)**2
    insidecirclefour = (x-circleFourx)**2 + (y-circley)**2


    if insidecircleone <= radiussquared:
        print x
        print y
        return 1
    elif insidecircletwo <= radiussquared:
        return 2
    elif insidecirclethree <= radiussquared:
        return 3
    elif insidecirclefour <= radiussquared:
        return 4
    else:
        return False


def drawlaunchwheel(state):
    if state:
        #toplaunchwheel
        pygame.gfxdraw.filled_circle(background,410,105-31,30,colorGreen)
        pygame.gfxdraw.aacircle(background,410,105-31,30,colorGreen)
        #bottomlaunchwheel
        pygame.gfxdraw.filled_circle(background,410,105+31,30,colorGreen)
        pygame.gfxdraw.aacircle(background,410,105+31,30,colorGreen)

    elif not state:
        #toplaunchwheel
        pygame.gfxdraw.filled_circle(background,410,105-31,30,colorWhite)
        pygame.gfxdraw.aacircle(background,410,105-31,30,colorWhite)
        #bottomlaunchwheel
        pygame.gfxdraw.filled_circle(background,410,105+31,30,colorWhite)
        pygame.gfxdraw.aacircle(background,410,105+31,30,colorWhite)

def drawLaunchUI():

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
