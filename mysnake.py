from random import randint
import pygame as pg


pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

### 1.1 Code de démarrage 

#running=True                #on initialise le running pour que la boucle commence
#while running:              #tant qu'on n'a pas modifié, le running est True et ça tourne
#    clock.tick(1)
#
#    for event in pg.event.get():
#        if event.type == pg.QUIT:       #si on a demandé de fermer
#            running=False               #on change l'état de running pour qu'à la prochaine évaluation, on ne rentre pas dans la boucle
#
#    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
#    screen.fill(random_color)
#    pg.display.update()




### 1.2 Quitter proprement

# running=True                #on initialise le running pour que la boucle commence
# while running:              #tant qu'on n'a pas modifié, le running est True et ça tourne
#    clock.tick(1)

#    for event in pg.event.get():
#        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_q) :       #si on a demandé de fermer d'une manière ou de l'autre
#            running=False               #on change l'état de running pour qu'à la prochaine évaluation, on ne rentre pas dans la boucle

#    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
#    screen.fill(random_color)
#    pg.display.update()



### 2.1 Dessiner un rectangle

# x, y = 100, 200
# width, height = 20, 20
# color = (255, 0, 0)         #du rouge

# running = True
# while running:
#     clock.tick(1)

#     for event in pg.event.get():
#         if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_q) :
#             running = False

#     color_choisie = (0, 0, 0)               #(0, 0, 0) correspond à du noir
#     screen.fill(color_choisie)

#     rect = pg.Rect(x, y, width, height)
#     pg.draw.rect(screen, color, rect)               #on remplit le rectangle de rouge (color est rouge)

#     pg.display.update()

# pg.quit()



### 2.2. Le damier

def draw_board():
    color_choisie = (0, 0, 0)               #(0, 0, 0) correspond à du noir
    color_blanc = (255, 255, 255)
    screen.fill(color_choisie)
    i=0
    J=0
    width, height = 20, 20
    for i in range(30) : 
        for j in range(30) : 
            if (i+j)%2==0 :                             #on colorie un carré sur 2 horizontalement et verticalement
                rect = pg.Rect(20*i, 20*j, width, height)
                pg.draw.rect(screen, color_blanc, rect)   
    pg.display.flip()          

# running = True
# while running:
#     draw_board()                        #on appelle la fonction créée
#     for event in pg.event.get():
#         if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_q):
#             running = False
# pg.quit()


### 3.1 Dessiner le serpent
SNAKE = [
   (10, 15),
   (11, 15),
   (12, 15),
]


def draw_snake(SNAKE) : 
    color_rouge = (255, 0, 0)
    width, height = 20, 20
    for l in SNAKE : 
        (x,y)=l
        rect = pg.Rect(20*x, 20*y, width, height)
        pg.draw.rect(screen, color_rouge, rect)   
    pg.display.flip() 

# running = True
# while running:
#     draw_board()                   
#     draw_snake(SNAKE)     #on appelle la fonction créée
#     for event in pg.event.get():
#         if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_q):
#             running = False
# pg.quit()


### 3.2 Déplacer le serpent

def move_snake(SNAKE, direction):
    head_x, head_y = SNAKE[-1]
    dx, dy = direction
    SNAKE.pop(0)                                 #retire la queue
    SNAKE.append((head_x + dx, head_y + dy))    #ajoute la nouvelle tête
    return SNAKE

### 3.3. Intégrer le déplacement
### 4. Contrôler le déplacement

direction = (1, 0)

# running = True
# while running:
#     clock.tick(2)

#     for event in pg.event.get():
#         if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_q):     #on garde les 2 manières de quitter
#             running = False
#         elif event.type == pg.KEYDOWN:
#             if event.key == pg.K_UP and direction != (0, 1):            #on doit l'empêcher d'aller à l'envers pour ne pas qu'il se rentre dedans
#                 direction = (0, -1)
#             elif event.key == pg.K_DOWN and direction != (0, -1):           #idem...
#                 direction = (0, 1)
#             elif event.key == pg.K_LEFT and direction != (1, 0):
#                 direction = (-1, 0)
#             elif event.key == pg.K_RIGHT and direction != (-1, 0):
#                 direction = (1, 0)

#     move_snake(SNAKE, direction)

#     screen.fill((0, 0, 0))   # noir
#     draw_board()
#     draw_snake(SNAKE) 
#     pg.display.update()

# pg.quit()


### 5.1 Dessiner le fruit

FRUIT = (randint(0, 29), randint(0, 29))

def draw_fruit(FRUIT) : 
    color_vert = (0, 255, 0)
    x,y=FRUIT
    pg.draw.rect(screen, color_vert, pg.Rect(20*x, 20*y, 1, 1))
    pg.display.flip() 



running = True
while running:
    draw_board()                   
    draw_fruit(FRUIT)   #on appelle la fonction créée
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_q):
            running = False
pg.quit()

