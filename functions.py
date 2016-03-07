import pygame
import pygame.gfxdraw


x_size = 480
y_size = 320

radius = 50
space = 18

colorGreen = (47, 232, 11)
colorBlack = (0,0,0)
colorBackground = (180,180,180)
colorYellow = (255,220,42)
colorWhite = (250,250,250)

#circles one and four locations are switched
circley = y_size - (radius + 10)
circleFourx = 1*radius + space-3
circleTwox = 3*radius + 2*space-3
circleThreex = 5*radius + 3*space-3
circleOnex = 7*radius + 4*space-3

servox = [251,251,175,175]
servoy = [40,167,40,167]

launchwheelx = 410
launchwheely = [105+31,105-31]

arrowcenterx = [155,335]
arrowcentery = 95

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
    servoradiussquared = 10**2
    launchradiussquared = 30 **2
    insidecircleone = (x-circleOnex)**2 + (y-circley)**2
    insidecircletwo = (x-circleTwox)**2 + (y-circley)**2
    insidecirclethree = (x-circleThreex)**2 + (y-circley)**2
    insidecirclefour = (x-circleFourx)**2 + (y-circley)**2

    insideservo1 = (x-servox[0])**2 + (y-servoy[0])**2
    insideservo2 = (x-servox[1])**2 + (y-servoy[1])**2
    insideservo3 = (x-servox[2])**2 + (y-servoy[2])**2
    insideservo4 = (x-servox[3])**2 + (y-servoy[3])**2

    insidelaunch1 = (x-launchwheelx)**2 + (y-launchwheely[0])**2
    insidelaunch2 = (x-launchwheelx)**2 + (y-launchwheely[1])**2

    insidearrow1 = (x-arrowcenterx[0])**2 + (y-arrowcentery)**2
    insidearrow2 = (x-arrowcenterx[1])**2 + (y-arrowcentery)**2

    if insidecircleone <= radiussquared:
        return 1
    elif insidecircletwo <= radiussquared:
        return 2
    elif insidecirclethree <= radiussquared:
        return 3
    elif insidecirclefour <= radiussquared:
        return 4
    elif insideservo1 <= servoradiussquared:
        return 's1'
    elif insideservo2 <= servoradiussquared:
        return 's2'
    elif insideservo3 <= servoradiussquared:
        return 's3'
    elif insideservo4 <= servoradiussquared:
        return 's4'
    elif insidelaunch1 <= launchradiussquared:
        return 'l1'
    elif insidelaunch2 <= launchradiussquared:
        return 'l2'
    elif insidearrow1 <= launchradiussquared:
        return 'a1'
    elif insidearrow2 <= launchradiussquared:
        return 'a2'
    else:
        return False


def drawlaunchwheel(state):
    if state:
        #toplaunchwheel
        pygame.gfxdraw.filled_circle(background,launchwheelx,launchwheely[1],30,colorGreen)
        pygame.gfxdraw.aacircle(background,launchwheelx,launchwheely[1],30,colorGreen)
        #bottomlaunchwheel
        pygame.gfxdraw.filled_circle(background,launchwheelx,launchwheely[0],30,colorGreen)
        pygame.gfxdraw.aacircle(background,launchwheelx,launchwheely[0],30,colorGreen)

    elif not state:
        #toplaunchwheel
        pygame.gfxdraw.filled_circle(background,launchwheelx,launchwheely[1],30,colorWhite)
        pygame.gfxdraw.aacircle(background,launchwheelx,launchwheely[1],30,colorWhite)
        #bottomlaunchwheel
        pygame.gfxdraw.filled_circle(background,launchwheelx,launchwheely[0],30,colorWhite)
        pygame.gfxdraw.aacircle(background,launchwheelx,launchwheely[0],30,colorWhite)

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

def drawServo(pos,state):
    if state:
        color = colorGreen
        textcolor = (5, 5, 5)
    if not state:
        color = colorWhite
        textcolor = colorBackground

    f = pygame.font.SysFont("freesans", 18)
    pygame.gfxdraw.filled_circle(background,servox[pos],servoy[pos],10,color)
    pygame.gfxdraw.aacircle(background,servox[pos],servoy[pos],10,color)
