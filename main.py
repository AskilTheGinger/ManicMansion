
import pygame as pg

from constants import *
from classes import *

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

player = Menneske()
spøkelse1 = Spokelse()

hindringer:list[Hindring] = []

for _ in range(3):
    hindringer.append(Hindring())

def tegne_brett():
    fri_rect_venstre = pg.Rect(0,0,FRI_BREDDE,VINDU_HOYDE)
    fri_rect_hoyre = pg.Rect(FRI_HOYRE,0,FRI_BREDDE,VINDU_HOYDE)

    pg.draw.rect(vindu, GREY, fri_rect_venstre)
    pg.draw.rect(vindu, GREY, fri_rect_hoyre)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_w:
            player.vy=-10
        

    vindu.fill(WHITE)
    for hindring in hindringer:
        hindring.draw(vindu)
    
    tegne_brett()
    player.move()
    player.draw(vindu)
    spøkelse1.oppdater()
    spøkelse1.draw(vindu)

    

    pg.display.flip()
    clock.tick(FPS)


pg.quit()
