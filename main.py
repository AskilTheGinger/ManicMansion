import pygame as pg

from constants import *
from classes import *

pg.init()
pg.mixer.init()

vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()
font = pg.font.SysFont(None, 48)

player = Menneske()

hindringer:list[Hindring] = []
sauer:list[Sau] = []
spokelser:list[Spokelse] = []

pg.mixer.music.load(IMAGE_DIR/"sound/musikk.mp3")
pg.mixer.music.set_volume(0.1)
pg.mixer.music.play(-1)

sauelyd = pg.mixer.Sound(IMAGE_DIR /"sound/sau.mp3")
SAU_LYD_EVENT = pg.USEREVENT + 1
første_intervall = random.randint(3000, 10000)   
pg.time.set_timer(SAU_LYD_EVENT, første_intervall, loops=1)


for _ in range(3):
    hindringer.append(Hindring())

for _ in range(3):
    sauer.append(Sau())

spokelser.append(Spokelse())

mur = pg.image.load(IMAGE_DIR/"mur.png").convert_alpha()
mur_venstre = pg.transform.scale(mur, (FRI_BREDDE, VINDU_HOYDE))
mur_hoyre = pg.transform.flip(mur_venstre,True, False)

def tegne_brett():
    poengtekst = font.render(f"Poeng: {player.poeng}", True, BLACK)
    fri_rect_venstre = pg.Rect(0,0,FRI_BREDDE,VINDU_HOYDE)
    fri_rect_hoyre = pg.Rect(FRI_HOYRE,0,FRI_BREDDE,VINDU_HOYDE)
    vindu.blit(mur_venstre, fri_rect_venstre)
    vindu.blit(mur_hoyre, fri_rect_hoyre)
    poengtekst_rect = poengtekst.get_rect()
    poengtekst_rect.topleft = (50, 50) 
    vindu.blit(poengtekst, poengtekst_rect)

def game_loop():
    tegne_brett()
    gamle_poeng = player.poeng
    
    player.move()

    for hindring in hindringer:
        for hindringa in hindringer:
            hindring.collide(hindringa)

        if player.rect.colliderect(hindring.rect):
            player.collide(hindring)
    

    for spokelse in spokelser:
        spokelse.oppdater()
        if spokelse.rect.colliderect(player.rect):
            return False
    
    for sau in sauer:
        for saua in sauer:
            sau.collide(saua)
        if player.plukke_sau(sau):
            break
    
    player.oppdater()

    if player.bært_sau:
        player.bært_sau.folge(player.rect.centerx, player.rect.centery)
        for sau in sauer:
            if player.rect.colliderect(sau.rect) and sau != player.bært_sau:
                return False


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
bakgrunn = pg.image.load(IMAGE_DIR/"bakgrunn.png").convert()
bakgrunn = pg.transform.scale(bakgrunn, (VINDU_BREDDE, VINDU_HOYDE))

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == SAU_LYD_EVENT:
            sauelyd.play()
            neste_intervall = random.randint(3000, 8000)
            pg.time.set_timer(SAU_LYD_EVENT, neste_intervall, loops=1)

    vindu.blit(bakgrunn,(0,0))
    if game_active:
        game_active = game_loop()
    else:
        pg.time.set_timer(SAU_LYD_EVENT, 0)
        poengtekst = font.render(f"Du fikk: {player.poeng} poeng", True, BLACK)
        poengtekst_rect = poengtekst.get_rect()
        poengtekst_rect.center = (VINDU_BREDDE//2, VINDU_HOYDE//2) 
        vindu.blit(poengtekst, poengtekst_rect)
    pg.display.flip()
    clock.tick(FPS)


pg.quit()
