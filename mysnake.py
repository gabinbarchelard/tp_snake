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

x, y = 100, 200
width, height = 20, 20
color = (255, 0, 0)         #du rouge

running = True
while running:
    clock.tick(1)

    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_q) :
            running = False

    color_choisie = (0, 0, 0)               #(0, 0, 0) correspond à du noir
    screen.fill(color_choisie)

    rect = pg.Rect(x, y, width, height)
    pg.draw.rect(screen, color, rect)               #on remplit le rectangle de rouge (color est rouge)

    pg.display.update()

pg.quit()

