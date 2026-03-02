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
        
       

class Sau(Objekt):
    def __init__(self):
        img = pg.image.load(IMAGE_DIR / "sau/west.png")
        scaled_img = pg.transform.scale_by(img, 2)
        rect = scaled_img.get_rect(topleft=(
            random.randint(VINDU_BREDDE-FRI_BREDDE,VINDU_BREDDE-scaled_img.get_width()),
            random.randint(0, VINDU_HOYDE-scaled_img.get_height())))
        super().__init__(0, 0, scaled_img, rect)


class Menneske(Objekt):
    def __init__(self):
        img = pg.image.load(IMAGE_DIR / "karakter/south.png")
        scaled_img = pg.transform.scale_by(img, 2.7)
        rect = scaled_img.get_rect(topleft=(100, VINDU_HOYDE // 2))
        self.bærer_sau = False
        self.poeng = 0
        super().__init__(0, 0, scaled_img, rect)
    def move(self):
        speed=5
        keys = pg.key.get_pressed()

        if keys[pg.K_w] and self.rect.y > 0:
            self.rect.y -= speed
        if keys[pg.K_s] and self.rect.y < VINDU_HOYDE - self.rect.height:
            self.rect.y += speed
        if keys[pg.K_a] and self.rect.x > 0:
            self.rect.x -= speed
        if keys[pg.K_d] and self.rect.x < VINDU_BREDDE - self.rect.width:
            self.rect.x += speed

    def collide(self, x:int, y:int):
        self.rect.x = x
        self.rect.y = y

    def plukke_sau(self, sau:Sau):
        if self.rect.colliderect(sau.rect) and self.bærer_sau == False:
            self.bærer_sau = True
            return True
        return False
    
    def faa_poeng(self):
        if self.bærer_sau == True and self.rect.right < FRI_BREDDE:
            self.poeng += 1
            self.bærer_sau = False

class Spokelse(Objekt):
    def __init__(self):
        img = pg.image.load(IMAGE_DIR / "spøkelse.png")
        scaled_img = pg.transform.scale_by(img, 0.5)
        x = FRI_BREDDE + random.randint(0, VINDU_BREDDE - (FRI_BREDDE*2)-scaled_img.get_width())
        y = random.randint(0, VINDU_HOYDE-80)
        vx = -4
        vy = 4
        rect = scaled_img.get_rect(topleft=(x, y))
        super().__init__(vx, vy, scaled_img, rect)
    
    def oppdater(self):
        super().oppdater()
        
        if FRI_BREDDE>=self.rect.left or self.rect.left>=(VINDU_BREDDE-FRI_BREDDE-self.rect.width):
            self.vx*=-1
        if 0 >= self.rect.top or self.rect.top>=(VINDU_HOYDE-self.rect.height):
            self.vy*=-1

class Hindring(Objekt):
    def __init__(self):
        img = pg.image.load(IMAGE_DIR / "stein.png")
        scaled_img = pg.transform.scale_by(img, 0.3)
        posisjon_x = random.randint(FRI_BREDDE, VINDU_BREDDE-FRI_BREDDE-scaled_img.get_width())
        posisjon_y = random.randint(0, VINDU_HOYDE-scaled_img.get_height())
        rect = scaled_img.get_rect(topleft=(posisjon_x, posisjon_y))
        super().__init__(0, 0, scaled_img, rect)