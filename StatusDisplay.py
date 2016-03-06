from functions import *
import sys
import time

def exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN:
            pygame.quit()
            sys.exit()

arrowstate = [False,False]
buttonstate = [False,True,True,False]
sensorstate = [False,False,False,False]
wheelstate = False

pygame.init()

drawLaunchUI()

drawlaunchwheel(wheelstate)
buttonOne(False)

lcd.blit(background, (0,0))
pygame.display.flip()

while True:

    for i in range(0,4):
        drawSensor(i, sensorstate[i])
    drawarrow(1,arrowstate[0]); drawarrow(2,arrowstate[1])
    buttonTwo(buttonstate[1]); buttonThree(buttonstate[2]); buttonFour(buttonstate[3])

    if buttonstate[0]:
        buttonOne(True)
        buttonstate[0] = False

    lcd.blit(background, (0,0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if insidecircle(x,y) == 1:
                print "inside 1"
                if not buttonstate[2]:
                    buttonstate[0] = not buttonstate[0]
            elif insidecircle(x, y) == 2:
                print "inside 2"
            elif insidecircle(x, y) == 3:
                print "inside 3"
                buttonstate[2] = not buttonstate[2]
            elif insidecircle(x, y) == 4:
                print "inside 4"
                buttonFour(True)
                lcd.blit(background, (0,0))
                pygame.display.flip()
                time.sleep(.05)
            elif insidecircle(x,y) == False:
                print "missed"
