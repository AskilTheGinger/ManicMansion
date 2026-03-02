import pygame as pg

from constants import *
from classes import *

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()
font = pg.font.SysFont(None, 48)

player = Menneske()
spøkelse1 = Spokelse()
poeng = 0

hindringer:list[Hindring] = []
sauer:list[Sau] = []

for _ in range(3):
    hindringer.append(Hindring())

for _ in range(3):
    sauer.append(Sau())

def tegne_brett(poeng:int):
    poengtekst = font.render(f"Poeng: {poeng}", True, BLACK)
    fri_rect_venstre = pg.Rect(0,0,FRI_BREDDE,VINDU_HOYDE)
    fri_rect_hoyre = pg.Rect(FRI_HOYRE,0,FRI_BREDDE,VINDU_HOYDE)

    pg.draw.rect(vindu, GREY, fri_rect_venstre)
    pg.draw.rect(vindu, GREY, fri_rect_hoyre)
    poengtekst_rect = poengtekst.get_rect()
    poengtekst_rect.topleft = (50, 50) 
    vindu.blit(poengtekst, poengtekst_rect)

def game_loop(x1:int, y1:int):
    tegne_brett(poeng)

    for hindring in hindringer:
        hindring.draw(vindu)
    
    for sau in sauer:
        sau.draw(vindu)
        
    player.move()

    for hindring in hindringer:
        if player.rect.colliderect(hindring.rect):
            player.collide(x1, y1)
    
    spøkelse1.oppdater()
    if spøkelse1.rect.colliderect(player.rect):
        return False

    player.draw(vindu)
    spøkelse1.draw(vindu)
    return True

running = True
game_active = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
    
    x1, y1 = player.rect.x, player.rect.y

    vindu.fill(WHITE)
    
    if game_active:
        game_active = game_loop(x1, y1)
    else:
        poengtekst = font.render(f"Du fikk: {poeng} poeng", True, BLACK)
        poengtekst_rect = poengtekst.get_rect()
        poengtekst_rect.center = (VINDU_BREDDE//2, VINDU_HOYDE//2) 
        vindu.blit(poengtekst, poengtekst_rect)

    pg.display.flip()
    clock.tick(FPS)


pg.quit()
