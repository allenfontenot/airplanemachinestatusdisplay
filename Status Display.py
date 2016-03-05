from functions import *
import sys



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
    buttonThree(True)
    buttonFour(True)

    lcd.blit(background, (0,0))
    pygame.display.flip()

    time.sleep(1)

    buttonOne(False)
    buttonTwo(False)
    buttonThree(False)
    buttonFour(False)
    lcd.blit(background, (0,0))
    pygame.display.flip()
    
    time.sleep(1)



exit()


