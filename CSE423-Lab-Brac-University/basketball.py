from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

#Global variables
difficulty = int(input("Please select difficulty (0 for easy mode, 1 for medium, and, 2 for hard): "))
gamePaused = False
score = 0
cx = 5000
cy = 800
r = 400
hoop_x_up_left = 4500
hoop_x_up_right = 5500
thrown = False
goUp = True
gameOver= False
speed = 100
lives = 3
goingRight = True

if difficulty == 0:
    x = random.randint(-4000, 4000)
    y = 0
elif difficulty == 1:
    x = random.randint(-4000, 4000)
    y = random.randint(-4000, 2000)
elif difficulty == 2: 
    x = random.randint(-4000, 4000)
    y = random.randint(-4000, 2000)

if difficulty < 0 or difficulty > 2:
    print("No game available for you!")
else:
    if difficulty == 0:
        print("Easy Mode Selected!")
    elif difficulty == 1:
        print("Medium Mode Selected!")
    elif difficulty == 2:
        print("Hard Mode Selected!")

'''MPL Code from Lab 2:'''
#Start of MPL
def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def draw_using_mpl(x0, y0, x1, y1):
    zone = findZone(x0, y0, x1, y1)
    x0, y0 = convert_to_zone_0(zone, x0, y0)
    x1, y1 = convert_to_zone_0(zone, x1, y1)
    dx = x1 - x0
    dy = y1 - y0
    d = 2 * dy - dx
    dne = 2 * dy - 2 * dx
    de = 2 * dy
    for i in range(x0, x1):
        a, b = convert_back_to_original(zone, x0, y0)
        if d >= 0:
            d = d + dne
            draw_points(a, b)
            x0 += 1
            y0 += 1
        else:
            d = d + de
            draw_points(a, b)
            x0 += 1

def findZone(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dx) > abs(dy): #For Zone 0, 3, 4 & 7
        if dx > 0 and dy > 0:
            return 0
        elif dx < 0 and dy > 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7
    else: #For zone 1, 2, 5 & 6
        if dx > 0 and dy > 0:
            return 1
        elif dx < 0 and dy > 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        else:
            return 6

def convert_to_zone_0(zone, x0, y0):
    if zone == 0:
        return x0, y0
    elif zone == 1:
        return y0, x0
    elif zone == 2:
        return -y0, x0
    elif zone == 3:
        return -x0, y0
    elif zone == 4:
        return -x0, -y0
    elif zone == 5:
        return -y0, -x0
    elif zone == 6:
        return -y0, x0
    elif zone == 7:
        return x0, -y0
   
def convert_back_to_original(zone, x0, y0):
    if zone == 0:
        return x0, y0
    if zone == 1:
        return y0, x0
    if zone == 2:
        return -y0, -x0
    if zone == 3:
        return -x0, y0
    if zone == 4:
        return -x0, -y0
    if zone == 5:
        return -y0, -x0
    if zone == 6:
        return y0, -x0
    if zone == 7:
        return x0, -y0
    #End of MPL
    
def draw_arrow():
    glColor3f(0.0, 1.0, 1.0)
    draw_using_mpl(500, 9000, 1000, 9000)
    draw_using_mpl(500, 9000, 750, 9250)
    draw_using_mpl(500, 9000, 750, 8750)

def draw_cross():
    glColor3f(1.0, 0.0, 0.0)
    draw_using_mpl(9000, 9250, 9500, 8750)
    draw_using_mpl(9000, 8750, 9500, 9250)

def draw_pause_button():   
    glColor3f(1.0, 1.0, 0.0)
    draw_using_mpl(4900, 9250, 4900, 8750)
    draw_using_mpl(5100, 9250, 5100, 8750)

def draw_play_button():
    glColor3f(1.0, 1.0, 0.0)
    draw_using_mpl(4800, 9250, 5200, 9000)
    draw_using_mpl(4800, 9250, 4800, 8750)
    draw_using_mpl(4800, 8750, 5200, 9000)

def draw_basketball():
    global cx, cy, r
    glColor3f(1.0, 0.5, 0.0)
    MidpointCircle(r, cx, cy)
    draw_using_mpl(cx, cy+r, cx, cy-r)
    draw_using_mpl(cx-r, cy, cx+r, cy)

def draw_hoop():
    global x, y, hoop_x_up_left, hoop_x_up_right
    glColor3f(1.0, 1.0, 1.0)
    draw_using_mpl(hoop_x_up_left-x, 6000-y, hoop_x_up_right-x, 6000-y)
    draw_using_mpl(hoop_x_up_left-x, 6000-y, hoop_x_up_left+200-x, 5000-y)
    draw_using_mpl(hoop_x_up_left+600-x, 6000-y, hoop_x_up_right-200-x, 5000-y)
    draw_using_mpl(hoop_x_up_left+400-x, 6000-y, hoop_x_up_right-400-x, 5000-y)
    draw_using_mpl(hoop_x_up_left+200-x, 6000-y, hoop_x_up_left+400-x, 5000-y)
    draw_using_mpl(hoop_x_up_left+200-x, 5000-y, hoop_x_up_right-200-x, 5000-y)
    draw_using_mpl(hoop_x_up_right-200-x, 5000-y, hoop_x_up_right-x, 6000-y)
    draw_using_mpl(hoop_x_up_right-400-x, 5000-y, hoop_x_up_right-200-x, 6000-y)
    draw_using_mpl(hoop_x_up_left+400-x, 5000-y, hoop_x_up_right-400-x, 6000-y)
    draw_using_mpl(hoop_x_up_left+200-x, 5000-y, hoop_x_up_left+400-x, 6000-y)

def game_over():
    global score, gameOver
    print("Game Over!")
    print("Lives remaining: 0")
    print("Score:", score)
    print("Thanks for playing!")
    gameOver = True
    #glutLeaveMainLoop()

def draw_points_circle(x, y, cx, cy):
    glColor3f(1.0, 0.5, 0.0)
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x + cx, y + cy) 
    glEnd()

def MidpointCircle(r, cx, cy):
    d = 1 - r
    x = 0
    y = r
    Circlepoints(x, y, cx, cy)
    while x < y:
        if d < 0:
            d = d + 2 * x + 3
            x += 1
        else:
            d = d + 2 * x - 2 * y + 5
            x += 1
            y -= 1
        Circlepoints(x, y, cx, cy)

def Circlepoints(x, y, cx, cy):
    draw_points_circle(x, y, cx, cy)
    draw_points_circle(y, x, cx, cy)
    draw_points_circle(y, -x, cx, cy)
    draw_points_circle(x, -y, cx, cy)
    draw_points_circle(-x, -y, cx, cy)
    draw_points_circle(-y, -x, cx, cy)
    draw_points_circle(-y, x, cx, cy)
    draw_points_circle(-x, y, cx, cy)

def keyboardListener(key, x, y):
    global thrown, gamePaused, gameOver
    if not gamePaused and not gameOver:
        if key==b' ':
            thrown = True
    glutPostRedisplay()

def specialKeyListener(key, left, right):
    global cx, gamePaused, gameOver, thrown, difficulty
    if difficulty == 2:
        if not gamePaused and not gameOver:
            if key == GLUT_KEY_LEFT:
                if cx >= 700:
                    cx-=250
            if key == GLUT_KEY_RIGHT:
                if cx <= 9300:
                    cx+=250  
    else:  
        if not gamePaused and not gameOver and not thrown:
            if key == GLUT_KEY_LEFT:
                if cx >= 700:
                    cx-=250
            if key == GLUT_KEY_RIGHT:
                if cx <= 9300:
                    cx+=250
    glutPostRedisplay()

def restartGame():
    global score, cx, cy, r, thrown, goUp, lives, goingRight, hoop_x_up_left, hoop_x_up_right
    score = 0
    cx = 5000
    cy = 800
    r = 400
    lives = 3
    thrown = False
    goUp = True
    goingRight = True
    hoop_x_up_left = 4500
    hoop_x_up_right = 5500
    print("Starting over!")
    glutPostRedisplay()

def mouseInput(button, state, x, y):
    global gamePaused, gameOver, score
    if button == GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        if x>=20 and x<= 50 and y>= 30 and y<= 60:
            restartGame()
        if x>=245 and x<=265 and y>=25 and y<=65:
            if not gamePaused:
                gamePaused = True
                print("Game Paused")
            else:
                gamePaused = False
                print("Game Resuming")
        if x>=420 and x<= 490 and y>= 20 and y<= 80:
            print("Goodbye")
            print("Score:", score)
            gameOver = True
            glutLeaveMainLoop()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 10000, 0.0, 10000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def go_up():
    global cy, y, goUp, difficulty
    if cy>=6500-y:
        goUp = False
    cy += 300
    if difficulty == 2:
        cy += 200

def go_down():
    global cy, x, y, goUp, thrown, score, lives, gameOver, difficulty, hoop_x_up_left, hoop_x_up_right, goingRight, speed
    if cx > hoop_x_up_left - x - 250 and cx < hoop_x_up_right - x + 250:
        cy -= 150
        if cy >= 5000-y and cy <= 6000-y:
            cy = 800
            thrown = False
            goUp = True
            score += 1
            speed += 50
            hoop_x_up_left = 4500
            hoop_x_up_right = 5500
            goingRight = True
            if difficulty == 0:
                x = random.randint(-4000, 4000)
            elif difficulty == 1:
                x = random.randint(-4000, 4000)
                y = random.randint(-4000, 2000)
            elif difficulty == 2:
                x = random.randint(-4000, 4000)
                y = random.randint(-4000, 2000)
            print("Score:", score)
    else:
        cy -= 300
        if cy <= 500:
            hoop_x_up_left = 4500
            hoop_x_up_right = 5500
            goUp = True
            thrown = False
            goingRight = True
            cy = 800
            if lives>1:
                lives -= 1
                print("Lives Remaining:", lives)
            else:
                lives -= 1
                game_over()

def goRight():
    global hoop_x_up_right, hoop_x_up_left, speed
    hoop_x_up_left += speed
    hoop_x_up_right += speed

def goLeft():
    global hoop_x_up_right, hoop_x_up_left, speed
    hoop_x_up_left -= speed
    hoop_x_up_right -= speed

def animate():
    global gameOver, thrown, gamePaused, goUp, difficulty, hoop_x_up_left, hoop_x_up_right, goingRight
    if not gameOver and not gamePaused:
        glutPostRedisplay()
        if thrown:
            if goUp:
                go_up()
            else:
                go_down()
        if difficulty == 2:
            if goingRight and hoop_x_up_right-x <= 9000:
                goRight()
            else:
                goingRight = False
            if not goingRight and hoop_x_up_left-x >= 1000:
                goLeft()
            else:
                goingRight = True
                
    glutPostRedisplay()

def draw_text(x, y, text, color):
    glColor3fv(color)
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))

def showScreen():
    global gamePaused, cx, difficulty, score, lives, gameOver
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_basketball()
    draw_arrow()
    draw_cross()
    draw_hoop()
    if gamePaused:
        draw_play_button()
    else:
        draw_pause_button()
    draw_text(500, 2000, f"Score: {score}", (1.0, 1.0, 1.0))
    draw_text(500, 1500, f"Lives: {lives}", (1.0, 1.0, 1.0))
    if gameOver:
        draw_text(500, 1000, "Game Over!", (1.0, 1.0, 1.0))
    glColor3f(1.0, 1.0, 0.0)  
    glutSwapBuffers()

if difficulty >= 0 and difficulty <= 2:
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow(b"Final Project")
    glutDisplayFunc(showScreen)
    glutKeyboardFunc(keyboardListener)
    glutIdleFunc(animate)
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseInput)
    glutMainLoop()
