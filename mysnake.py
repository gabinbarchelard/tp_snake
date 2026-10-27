from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

running=True                #on initialise le running pour que la boucle commence
while running:              #tant qu'on n'a pas modifié, le running est True et ça tourne
    clock.tick(1)

    for event in pg.event.get():
        if event.type == pg.QUIT:       #si on a demandé de fermer
            running=False               #on change l'état de runningv pour qu'à la prochaine évaluation, on ne rentre pas dans la boucle

    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.fill(random_color)
    pg.display.update()
