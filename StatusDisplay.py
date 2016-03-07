from functions import *
import sys
import time

def exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN:
            pygame.quit()
            sys.exit()


#if these are changed, change in reset button push also
arrowstate = [False,False]
buttonstate = [False,True,True,False]
sensorstate = [False,False,False,False]
wheelstate = False
servostate = [False,False,False,False]



pygame.init()

drawLaunchUI()


buttonOne(False)

lcd.blit(background, (0,0))
pygame.display.flip()

while True:

    for i in range(0,4):
        drawSensor(i, sensorstate[i])
        drawServo(i,servostate[i])
    drawarrow(1,arrowstate[0]); drawarrow(2,arrowstate[1])
    buttonTwo(buttonstate[1]); buttonThree(buttonstate[2]); buttonFour(buttonstate[3])
    drawlaunchwheel(wheelstate)

    if buttonstate[0]:
        buttonOne(True)
        buttonstate[0] = False

    lcd.blit(background, (0,0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            print x
            print y
            if insidecircle(x, y) == 3:
                print "inside 3"
                buttonstate[2] = not buttonstate[2]
            elif insidecircle(x, y) == 4:
                print "inside 4"
                buttonFour(True)
                lcd.blit(background, (0,0))
                pygame.display.flip()
                time.sleep(.05)
                buttonOne(False)
                arrowstate = [False,False]
                buttonstate = [False,True,True,False]
                sensorstate = [False,False,False,False]
                wheelstate = False
                servostate = [False,False,False,False]
            if not buttonstate[2]:
                if insidecircle(x,y) == 1:
                    print "inside 1"
                    buttonstate[0] = not buttonstate[0]
                elif insidecircle(x, y) == 2:
                    print "inside 2"
                elif insidecircle(x, y) == 's1':
                    servostate[0] = not servostate[0]
                elif insidecircle(x, y) == 's2':
                    servostate[1] = not servostate[1]
                elif insidecircle(x, y) == 's3':
                    servostate[2] = not servostate[2]
                elif insidecircle(x, y) == 's4':
                    servostate[3] = not servostate[3]
                elif insidecircle(x, y) == 'l1':
                    wheelstate = not wheelstate
                elif insidecircle(x, y) == 'l2':
                    wheelstate = not wheelstate
                elif insidecircle(x, y) == 'a1':
                    arrowstate[0] = not arrowstate[0]
                elif insidecircle(x, y) == 'a2':
                    arrowstate[1] = not arrowstate[1]
            elif not insidecircle(x, y):
                    print "missed"
