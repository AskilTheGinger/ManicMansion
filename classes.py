from constants import *
import pygame as pg
import random as random
from dataclasses import dataclass

@dataclass(slots=True)
class Objekt:
    vx: int
    vy: int
    img: pg.Surface
    rect: pg.Rect
    
    def oppdater(self):
        self.rect.left+=self.vx
        self.rect.top+=self.vy

    def draw(self, vindu: pg.Surface):
        vindu.blit(self.img, self.rect)
        
       

class Menneske(Objekt):
    def __init__(self):
        img = pg.image.load(IMAGE_DIR / "spøkelse.png")
        rect = img.get_rect(topleft=(100, VINDU_HOYDE // 2))
        super().__init__(0, 0, img, rect)
    def move(self):
        speed=5
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.rect.y -= speed
        if keys[pg.K_s]:
            self.rect.y += speed
        if keys[pg.K_a]:
            self.rect.x -= speed
        if keys[pg.K_d]:
            self.rect.x += speed
    def collide(self, hindring:Objekt):
        if self.rect.colliderect(hindring.rect):
            self.rect.left-=self.vx
            self.rect.top-=self.vy

        
        


    

        
        
    


class Spokelse(Objekt):
    def __init__(self):
        x = FRI_BREDDE + random.randint(0, VINDU_BREDDE - FRI_BREDDE*2)
        y = random.randint(0, VINDU_HOYDE-80)
        vx = -4
        vy=4
        img = pg.image.load(IMAGE_DIR / "spøkelse.png")
        nytt_img = pg.transform.scale_by(img, 0.5)
        rect = img.get_rect(topleft=(x, y))
        super().__init__(vx, vy, nytt_img, rect)
    
    def oppdater(self):
        super().oppdater()
        
        if FRI_BREDDE>=self.rect.left or self.rect.left>=(VINDU_BREDDE-FRI_BREDDE-self.rect.width):
            self.vx*=-1
        if 0>=self.rect.top or self.rect.top>=(VINDU_HOYDE-self.rect.height):
            self.vy*=-1

        
    

@dataclass (slots=True)
class Hindring(Objekt):
    def __init__(self):
        self.vx=0
        self.vy=0
        img = pg.image.load(IMAGE_DIR / "stein.png")
        scaled_img = pg.transform.scale_by(img, 0.3)
        posisjon_x = random.randint(FRI_BREDDE, VINDU_BREDDE-FRI_BREDDE)
        posisjon_y = random.randint(0, VINDU_HOYDE)
        rect = img.get_rect(topleft=(posisjon_x, posisjon_y))
        super().__init__(0, 0, scaled_img, rect)


class Sau(Objekt):
    def __init__(self):
        img = pg.image.load("spøkelse.png")
        rect = img.get_rect(topleft=(
            random.randint(0, VINDU_BREDDE),
            random.randint(0, VINDU_HOYDE)
        ))
        super().__init__(0, 0, img, rect)