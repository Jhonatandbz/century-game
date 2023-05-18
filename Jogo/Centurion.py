from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import pygame 
import random as rd

#----------------Parametros Globais----------------#
display = (1280, 720)
vel = 0.008
screen_limit_x = display[0]/80
screen_limit_y = display[1]/90
ini_position = -screen_limit_x + 6
depth = -80
life = 3
count = screen_limit_x
count_score = 0
score = 0
acc = 1
level = 1
random_list = [-6.5, -3.8, -1.1, 1.6, 4.3, 6]
#-------------------COORDENADAS--------------------#
main_block_position = [ini_position,0,0]
enemy_block_position_2 = [0,rd.choice(random_list),0]
enemy_block_position_3 = [0,rd.choice(random_list),0]
enemy_block_position_4 = [0,rd.choice(random_list),0]
enemy_block_position_5 = [0,rd.choice(random_list),0]
enemy_block_position_6 = [0,rd.choice(random_list),0]
estrela_1 = [0,0,depth]
estrela_2 = [0,0,depth]
estrela_3 = [0,0,depth]
estrela_4 = [0,0,depth]
estrela_5 = [0,0,depth]
estrela_6 = [0,0,depth]
estrela_7 = [0,0,depth]
estrela_8 = [0,0,depth]
key = True
#--------------------------------------------------#

def randomizer(enemy_pos: list):
    global key, random_list
    breaker = True
    while breaker:
        step = rd.choice(random_list)
        if step == enemy_pos[1]:
            pass
        else:
            if step == random_list[2] or step == random_list[3]:
                if key:
                    breaker = False
                    key = False
                else:
                    key = True
            else: 
                breaker = False
    return step

def Text_plot(text: str, position: list):
    
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()

    gluOrtho2D(0, display[0], 0, display[1])
    
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    text = list(text)
    glColor(0, 1, 0, 0)
    glRasterPos2f(position[0], position[1])

    for c in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))

    glMatrixMode(GL_PROJECTION)
    glPopMatrix()

    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

def background():   
    glColor3f(1.0,1.0,1.0)
    glPushMatrix()
    glPointSize(5)
    glBegin(GL_POINTS)

    
    for i in range(10):
        glVertex2f(rd.randint(-screen_limit_x, screen_limit_x), rd.randint(-screen_limit_y, screen_limit_y))

    
    glEnd()
    glFlush()
    glPopMatrix()

def star_block(star_pos: list, cor: int, velocity: float, index: int):
    global count, screen_limit_x
    glPushMatrix()
    star_pos[1] = index
    star_pos[0] = count*velocity
    glTranslatef(star_pos[0], star_pos[1], star_pos[2])      
    cube(cor)
    glPopMatrix()
    
def enemy_block(enemy_pos: list, cor: int, velocity: float):
    global count, screen_limit_x, random_list, key
    glPushMatrix()
    if count <= -screen_limit_x:
        count = screen_limit_x 
        if count == screen_limit_x:
            enemy_pos[1] = randomizer(enemy_pos)
    enemy_pos[0] = count*velocity
    glTranslatef(enemy_pos[0], enemy_pos[1], enemy_pos[2])      
    cube(cor)
    glPopMatrix()

def collision(main: list, enemy_pos: list):
    global life, ini_position, screen_limit_x, count
    step = 0
    if round(enemy_pos[0],0)-2 < main[0] < round(enemy_pos[0],0)+2  and round(enemy_pos[1],0)-2 < main[1] < round(enemy_pos[1],0)+2:
        count = screen_limit_x
        if count == screen_limit_x:
            enemy_pos[1] = randomizer(enemy_pos)
        main[0] = ini_position
        main[1] = 0
        enemy_pos[0] = count
        life -= 1
        if life == 0:
            return False
        return True
    return True

def while_scope_controller():
    global main_block_position, enemy_block_position_2, vel, screen_limit_x, life, count, count_score, score, acc, level
    start = True
    velocity = 5

    while start:
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False

        background()

        star_block(estrela_1, 0, velocity*2.5,-50)
        star_block(estrela_2, 0, velocity*2.0,-35)
        star_block(estrela_3, 0, velocity*1.6,-20)
        star_block(estrela_4, 0, velocity*2.7,-10)
        star_block(estrela_5, 0, velocity*1.3, 10)
        star_block(estrela_6, 0, velocity*2.2, 20)
        star_block(estrela_7, 0, velocity*1.5, 35)
        star_block(estrela_8, 0, velocity*1.8, 50)


        glPushMatrix()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                main_block_position[0] -= vel
                if main_block_position[0] <= -screen_limit_x+1:
                    main_block_position[0] = -screen_limit_x+1
                glTranslatef(main_block_position[0], main_block_position[1], main_block_position[2])

            if event.key == pygame.K_RIGHT:
                main_block_position[0] += vel
                if main_block_position[0] >= screen_limit_x-1:
                    main_block_position[0] = screen_limit_x-1
                glTranslatef(main_block_position[0], main_block_position[1], main_block_position[2])
            
            if event.key == pygame.K_UP:
                main_block_position[1] += vel
                if main_block_position[1] >= screen_limit_y:
                    main_block_position[1] = screen_limit_y
                glTranslatef(main_block_position[0], main_block_position[1], main_block_position[2])

            if event.key == pygame.K_DOWN:
                main_block_position[1] -= vel
                if main_block_position[1] <= -screen_limit_y:
                    main_block_position[1] = -screen_limit_y
                glTranslatef(main_block_position[0], main_block_position[1], main_block_position[2])
        else:
            glTranslatef(main_block_position[0], main_block_position[1], main_block_position[2])
       
        cube(1)
        glPopMatrix()
        
        if count_score == 1000:
            count_score = 0
            score += 1
            
        #Inimigos e dificuldade
        enemy_block(enemy_block_position_2, 0, 1*acc)
        if score > screen_limit_x*1+2:
            if score == screen_limit_x*1+3: 
                acc = 1.5
                level = 2
            enemy_block(enemy_block_position_3, 0, 1.3*acc)
            if score > screen_limit_x*2+2:
                if score == screen_limit_x*2+3: 
                    acc = 1.7
                    level = 3
                enemy_block(enemy_block_position_4, 0, 1.6*acc)
                if score > screen_limit_x*3+2:
                    if score == screen_limit_x*3+3: 
                        acc = 2
                        level = 4
                    enemy_block(enemy_block_position_5, 0, 1.9*acc)
                    if score > screen_limit_x*4+2:
                        if score == screen_limit_x*4+3: 
                            acc = 2.4
                            level = 5   
                        enemy_block(enemy_block_position_6, 0, 2.1*acc)
                        if score == 80: 
                            acc = 2.8
                            level = 6
                        if score == 100: 
                            acc = 3.3
                            level = 7
                        if score == 110: 
                            acc = 5
                            level = 8
                        if score == 120: 
                            acc = 8
                            level = 9
                        if score == 130: 
                            acc = 11
                            level = 10
                        if score == 140: 
                            acc = 14
                            level = 11
                        if score == 150: 
                            acc = 17
                            level = 12
        
        #colisões
        start = collision(main_block_position, enemy_block_position_2)
        if start == False: break
        start = collision(main_block_position, enemy_block_position_3)
        if start == False: break
        start = collision(main_block_position, enemy_block_position_4)
        if start == False: break
        start = collision(main_block_position, enemy_block_position_5)
        if start == False: break
        start = collision(main_block_position, enemy_block_position_6)
        if start == False: break

        #textos
        coordenada = [display[0]-350,display[1]-50]
        Text_plot('Lifes: {}'.format(life), coordenada)
        coordenada = [display[0]-200,display[1]-50]
        Text_plot('Score: {}'.format(score), coordenada)
        coordenada = [display[0]-500,display[1]-50]
        Text_plot('Level: {}'.format(level), coordenada)
        
        pygame.display.flip()
        count -= vel
        count_score += 1
      
def cube(cor: int):
    #print(cor)
    glBegin(GL_QUADS)
    if cor == 0:
        glColor(0.5,0.5,0.5,0)
    elif cor == 1:
        glColor(1,0,0,0)
    else:
        glColor(1,1,1,0)

    #Quad 1
    #glColor(1,0,0,0)
    glVertex3f( 1., 1., 1.)  
    glVertex3f( 1.,-1., 1.)  
    glVertex3f( 1.,-1.,-1.)   
    glVertex3f( 1., 1.,-1.)  
    #Quad 2
    #glColor(0,1,0,0)
    glVertex3f( 1., 1.,-1.)   
    glVertex3f( 1.,-1.,-1.)  
    glVertex3f(-1.,-1.,-1.)   
    glVertex3f(-1., 1.,-1.)  
    #Quad 3
    #glColor(0,0,1,0)
    glVertex3f(-1., 1.,-1.)  
    glVertex3f(-1.,-1.,-1.)   
    glVertex3f(-1.,-1., 1.)   
    glVertex3f(-1., 1., 1.)   
    #Quad 4
    #glColor(1,1,1,0)
    glVertex3f(-1., 1., 1.)   
    glVertex3f(-1.,-1., 1.)  
    glVertex3f( 1.,-1., 1.)   
    glVertex3f( 1., 1., 1.)   
    #Quad 5
    #glColor(1,1,0,0)
    glVertex3f(-1., 1.,-1.)   
    glVertex3f(-1., 1., 1.)   
    glVertex3f( 1., 1., 1.)   
    glVertex3f( 1., 1.,-1.)   
    #Quad 6
    #glColor(0,1,1,0)
    glVertex3f(-1.,-1., 1.)   
    glVertex3f(-1.,-1.,-1.)   
    glVertex3f( 1.,-1.,-1.)   
    glVertex3f( 1.,-1., 1.)  
    glEnd()        

def InitPyGame():
    global display
    glutInit()
    pygame.init()
    pygame.display.set_mode(display, pygame.DOUBLEBUF|pygame.OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 100)
    glTranslatef(0,0,-20)
    pygame.display.set_caption('Cinturão de Asteroides')
    pygame.mixer.music.load('angel.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    while_scope_controller()

InitPyGame()