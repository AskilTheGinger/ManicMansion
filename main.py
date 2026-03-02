import pygame as pg

from constants import *
from classes import *

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()
font = pg.font.SysFont(None, 48)

player = Menneske()
spøkelse1 = Spokelse()


hindringer:list[Hindring] = []
sauer:list[Sau] = []
spokelser:list[Spokelse] = []

for _ in range(3):
    hindringer.append(Hindring())

for _ in range(3):
    sauer.append(Sau())

spokelser.append(Spokelse())

def tegne_brett():
    poengtekst = font.render(f"Poeng: {player.poeng}", True, BLACK)
    fri_rect_venstre = pg.Rect(0,0,FRI_BREDDE,VINDU_HOYDE)
    fri_rect_hoyre = pg.Rect(FRI_HOYRE,0,FRI_BREDDE,VINDU_HOYDE)

    pg.draw.rect(vindu, GREY, fri_rect_venstre)
    pg.draw.rect(vindu, GREY, fri_rect_hoyre)
    poengtekst_rect = poengtekst.get_rect()
    poengtekst_rect.topleft = (50, 50) 
    vindu.blit(poengtekst, poengtekst_rect)

def game_loop(x:int, y:int):
    tegne_brett()
    gamle_poeng = player.poeng
    
    player.move()

    for hindring in hindringer:
        if player.rect.colliderect(hindring.rect):
            player.collide(hindring)
    
    for spokelse in spokelser:
        spokelse.oppdater()

    for spokelse in spokelser:
        if spokelse.rect.colliderect(player.rect):
            return False
    
    for sau in sauer:
        if player.plukke_sau(sau):
            sau.blir_dratt = True
            break
            

    if player.carried_sau:
        player.carried_sau.folge(player.rect.centerx, player.rect.centery)

    player.faa_poeng(sauer)

    if player.poeng > gamle_poeng:
        sauer.append(Sau())
        hindringer.append(Hindring())
        spokelser.append(Spokelse())


    for sau in sauer:
            sau.draw(vindu)

    for hindring in hindringer:
        hindring.draw(vindu) 

    for spokelse in spokelser:
            spokelse.draw(vindu)
    player.draw(vindu)
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
    
    player.move()
    for hindring in hindringer:
        hindring.draw(vindu)
        spøkelse1.collide(hindring)
        player.collide(hindring)
    
    tegne_brett()
    
    player.oppdater()
    player.draw(vindu)
    
    spøkelse1.oppdater()
    spøkelse1.draw(vindu)

    
    if game_active:
        game_active = game_loop(x1, y1)
    else:
        poengtekst = font.render(f"Du fikk: {player.poeng} poeng", True, BLACK)
        poengtekst_rect = poengtekst.get_rect()
        poengtekst_rect.center = (VINDU_BREDDE//2, VINDU_HOYDE//2) 
        vindu.blit(poengtekst, poengtekst_rect)

    pg.display.flip()
    clock.tick(FPS)


pg.quit()
