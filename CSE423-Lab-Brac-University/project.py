from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

#Note: Some of the lines are not showing up on the screen.
# Mostly the vertical lines, debug this if you can

SCREEN_HEIGHT = 900
SCREEN_WIDTH = 800
RADIUS = 50
MAX_MISSES = 3

ball_x = SCREEN_WIDTH // 2
ball_y = RADIUS
score = 0
game_over = False
pause = False
exit = False
moving_balls = []

def zone_conv(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1

#Determining the Zones and Converting to Zone 0

    abs_dx = abs(dx)
    abs_dy = abs(dy)
    if(dx > 0 and dy > 0) and (abs_dx >= abs_dy):
        zone = 0
        return x1, y1, x2, y2, zone
    elif(dx > 0 and dy > 0) and (abs_dx < abs_dy):
        zone = 1
        return x1, y1, x2, y2, zone
    elif(dx < 0 and dy > 0) and (abs_dx < abs_dy):
        zone = 2
        return y1, -x1, y2, -x2, zone
    elif (dx < 0 and dy > 0) and (abs_dx >= abs_dy):
        zone = 3
        return -x1, y1, -x2, y2, zone
    elif (dx < 0 and dy < 0) and (abs_dx >= abs_dy):
        zone = 4
        return -x1, -y1, -x2, -y2, zone
    elif (dx < 0 and dy < 0) and (abs_dx < abs_dy):
        zone = 5
        return -y1, -x1, -y2, -x2, zone
    elif (dx > 0 and dy < 0) and (abs_dx < abs_dy):
        zone = 6
        return -y1, x1, -y2, x2, zone
    else:
        zone = 7
        return x1, -y1, x2, -y2, zone 

#Mid Point Line Algorithm

def mpl(x1, y1, x2, y2 , color = (1, 1, 1)):
    x1 , y1 , x2, y2, zone = zone_conv(x1, y1, x2, y2)
    dx = x2 - x1
    dy = y2 - y1
    d = 2*dy - dx
    E = 2*dy
    NE = 2*(dy-dx)
    y = y1
    x = x1
    draw_points(x, y, color, 2)
    while (x<=x2):
        if (d>0):
            d += NE
            x += 1
            y += 1
        else:
            d += E
            x += 1
        x_t , y_t = init_zone(x , y , zone)
        draw_points(x_t, y_t, color, 2)

#Converting to the initial Zone

def init_zone(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y , x
    elif zone == 2:
        return -y , x
    elif zone == 3:
        return -x , y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y , -x
    elif zone == 6:
        return y , -x
    elif zone == 7:
        return x , -y
    else:
        print("Error")
        return x , y

def draw_points(x, y, color, size):
    glColor3fv(color)
    glPointSize(size) 
    glBegin(GL_POINTS)
    glVertex2f(x, y) 
    glEnd()

def mpc_algorithm(r, c_x, c_y, color):
    d = 1 - r
    x = 0
    y = r

    while x < y:
        for i in range(8):
            x1, y1 = convert_zone(x, y, i)
            draw_points(x1 + c_x, y1 + c_y, color, 2)
        
        if d < 0:  # E pixel
            d += 2 * x + 3
            x += 1
        else:      # SE pixel
            d += 2 * x - 2 * y + 5
            x += 1
            y -= 1

def convert_zone(x, y, z):
    if z == 0: return x, y
    if z == 1: return y, x
    if z == 2: return -y, x
    if z == 3: return -x, y
    if z == 4: return -x, -y
    if z == 5: return -y, -x
    if z == 6: return y, -x
    if z == 7: return x, -y

# Drawing Game Buttons

def draw_play(x, y):
    color = (0.0, 1.0, 0.0)
    mpl(x - 10, y + 10, x - 10, y - 10, color)
    mpl(x - 10, y - 10, x + 10, y, color)
    mpl(x + 10, y, x - 10, y + 10, color)

def draw_pause(x, y):
    color = (1.0, 1.0, 0.0)
    x1 = x+10
    x2 = x-10
    y1 = y+20
    y2 = y-20
    mpl(x1, y1, x1, y2, color)
    mpl(x2, y1, x2, y2, color)

def draw_reset(x, y):
    color = (0.0, 0.5, 1.0)
    mpl(x, y, x+40, y, color)
    mpl(x, y, x+20, y+20, color)
    mpl(x, y, x+20, y-20, color)

def draw_close(x, y):
    color = (1.0, 0.0, 0.0)
    mpl(x - 10, y + 10, x + 10, y - 10, color)
    mpl(x - 10, y - 10, x + 10, y + 10, color)

def draw_text(x, y, text, color):
    glColor3fv(color)
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))

# Button Coordinates
resest_button = (20, SCREEN_HEIGHT - 50)
pause_play_button = (SCREEN_WIDTH/2, SCREEN_HEIGHT-50)
close_button = (SCREEN_WIDTH-50, SCREEN_HEIGHT-50)

#Drawing Game Objects
h_x = SCREEN_WIDTH/2
h_y = SCREEN_HEIGHT*0.9
net_x = h_x
net_y = h_y - SCREEN_HEIGHT//4
net_z = 90
def draw_hoop():
    dx = SCREEN_WIDTH*0.35
    dy = SCREEN_HEIGHT*0.3
    color = (1, 1, 1)
    #large rect
    mpl(h_x - dx, h_y, h_x + dx, h_y, color)
    mpl(h_x - dx, h_y, h_x - dx, h_y - dy, color)
    mpl(h_x - dx, h_y - dy, h_x + dx, h_y - dy, color)
    mpl(h_x + dx, h_y - dy, h_x + dx, h_y, color)

    #small rect
    py = h_y - 0.25*dy
    cx = dx/2
    cy = 1.5
    mpl(h_x - cx, py, h_x + cx, py, color)
    mpl(h_x - cx, py, h_x - cx, py - cy, color)
    mpl(h_x - cx, py - cy, h_x + cx, py - cy, color)
    mpl(h_x + cx, py - cy, h_x + cx, py, color)

def draw_net():
    color = (1, 1, 0)
    mpl(net_x - net_z, net_y, net_x + net_z, net_y, color)

def draw_ball():
    mpc_algorithm(RADIUS, ball_x, ball_y, (0.86, 0.36, 0.0)) 

def draw_moving_balls():
    for i in moving_balls:
        mpc_algorithm(40, i[0], i[1], (0.86, 0.36, 0.0)) 

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_ball()  
    draw_hoop()
    draw_net() 
    draw_moving_balls() 
    draw_reset(resest_button[0],resest_button[1])
    draw_close(close_button[0],close_button[1])
    if not pause:
        draw_pause(pause_play_button[0], pause_play_button[1])
    else:
        draw_play(pause_play_button[0], pause_play_button[1])
    
    draw_text(10, 10, f"Score: {score}", (1.0, 1.0, 1.0))
    draw_text(10, 50, f"Lives: {MAX_MISSES}", (1.0, 1.0, 1.0))
    if game_over:
        draw_text(300, 300, "Game Over!", (1.0, 1.0, 1.0))
    glutSwapBuffers()

def key_pressed(key, x, y):
    global ball_x
    if key == b"a" and ball_x - RADIUS > 0: 
        ball_x -= 20
    elif key == b"d" and ball_x + RADIUS < SCREEN_WIDTH: 
        ball_x += 20
    elif key == b" " and not game_over:  
        throw()

def mouseListener(key, state, x, y):
    global pause, exit
    if key == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        y = SCREEN_HEIGHT-y
        if (x >= resest_button[0] and x <= resest_button[0]+40):
            if (y >= resest_button[1]-20 and y <= resest_button[1]+20):
                restart()

        elif (x >= pause_play_button[0]-10 and x <= pause_play_button[0]+10):
            if(y >= pause_play_button[1]-20 and y <= pause_play_button[1]+20):
                pause = not pause
        
        elif (x >= close_button[0]-10 and x <= close_button+10):
            if(y >= close_button[1]-10 and y<= close_button[1]+10):
                exit = True
def restart():
    global pause, game_over, score, MAX_MISSES, exit, moving_balls

    MAX_MISSES = 3
    score = 0
    game_over = False
    pause = False
    exit = False
    moving_balls = []


def throw():
    global moving_balls
    moving_balls.append([ball_x, ball_y])

def update_ball():
    for balls in moving_balls:
        balls[1] += 150

def animate():
    if not game_over and not pause:
        #update_basket_position()
        #handle_collisions()  / Scores will be updated here
        update_ball()
    if exit:
        glutLeaveMainLoop()
    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
glutCreateWindow(b"Basket Ball Loop")
glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)
glutDisplayFunc(draw)
glutIdleFunc(animate)
glutKeyboardFunc(key_pressed)
glutMouseFunc(mouseListener)
glutMainLoop()



