from constants import *
import pygame as pg
import random as random
from dataclasses import dataclass
from math import sin, cos, atan2, pi

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
        self.blir_dratt = False
        super().__init__(0, 0, scaled_img, rect)
    def folge(self, x:int, y:int):
        if self.blir_dratt == True:
            self.rect.center = x, y 


class Menneske(Objekt):
    def __init__(self):
        img = pg.image.load(IMAGE_DIR / "karakter/south.png")
        scaled_img = pg.transform.scale_by(img, 2.7)
        rect = scaled_img.get_rect(topleft=(100, VINDU_HOYDE // 2))
        self.bærer_sau = False
        self.bært_sau: Sau | None = None
        self.yretning:int=0
        self.xretning:int=0
        self.poeng = 0
        self.fart = 5
        self.img_path = {
            "north": pg.image.load(IMAGE_DIR / "karakter/north.png"),
            "south": pg.image.load(IMAGE_DIR / "karakter/south.png"),
            "east": pg.image.load(IMAGE_DIR / "karakter/east.png"),
            "west": pg.image.load(IMAGE_DIR / "karakter/west.png"),
            "north-east": pg.image.load(IMAGE_DIR / "karakter/north-east.png"),
            "south-east": pg.image.load(IMAGE_DIR / "karakter/south-east.png"),
            "north-west": pg.image.load(IMAGE_DIR / "karakter/north-west.png"),
            "south-west": pg.image.load(IMAGE_DIR / "karakter/south-west.png"),
        }
        super().__init__(0, 0, scaled_img, rect)

    def move(self):
        img = self.img_path["south"]
        keys = pg.key.get_pressed()
        if self.bærer_sau:
            self.fart = 3
        else:
            self.fart = 5
        if keys[pg.K_w] and self.rect.y > 0:
            self.vy = -self.fart
            img = self.img_path["north"]
        if keys[pg.K_s] and self.rect.y < VINDU_HOYDE - self.rect.height:
            self.vy = self.fart
            img = self.img_path["south"]
        if keys[pg.K_a] and self.rect.x > 0:
            self.vx = -self.fart
            img = self.img_path["west"]
        if keys[pg.K_d] and self.rect.x < VINDU_BREDDE - self.rect.width:
            self.vx = self.fart
            img = self.img_path["east"]
        
        if keys[pg.K_w] and keys[pg.K_d]:
            img = self.img_path["north-east"]
        if keys[pg.K_s] and keys[pg.K_d]:
            img = self.img_path["south-east"]
        if keys[pg.K_s] and keys[pg.K_a]:
            img = self.img_path["south-west"]
        if keys[pg.K_a] and keys[pg.K_w]:
            img = self.img_path["north-west"]
        
        self.img = pg.transform.scale_by(img, 2.7)
        
    def oppdater(self):
        super().oppdater()
        self.vx=0
        self.vy=0
    def collide(self, hindring:Objekt):
        if self.rect.colliderect(hindring.rect):
            if type(hindring)==Hindring:
                vinkel:int = int((atan2(self.rect.centery-hindring.rect.centery, self.rect.centerx-hindring.rect.centerx)-pi/4)//(pi/2))-1
                self.rect.x-= round(cos(vinkel*pi/2))
                self.rect.y-= round(sin(vinkel*pi/2))
                self.vx=0
                self.vy=0
                
            if type(hindring)==Sau:
                return True


    def plukke_sau(self, sau:Sau):
        if self.rect.colliderect(sau.rect) and not self.bærer_sau:
            self.bærer_sau = True
            self.bært_sau = sau
            sau.blir_dratt = True
            return True
        return False
    
    def faa_poeng(self, sauer:list[Sau]):
        if self.bærer_sau and self.rect.right < FRI_BREDDE:
            self.poeng += 1
            self.bærer_sau = False
            if self.bært_sau is not None and self.bært_sau in sauer:
                sauer.remove(self.bært_sau)
            self.bært_sau = None


class Spokelse(Objekt):
    def __init__(self):
        img = pg.image.load(IMAGE_DIR / "spøkelse.png")
        scaled_img = pg.transform.scale_by(img, 0.5)
        x = FRI_BREDDE + random.randint(0, VINDU_BREDDE - (FRI_BREDDE*2)-scaled_img.get_width())
        y = random.randint(0, VINDU_HOYDE-80)
        vx = -4
        vy=4
        nytt_img = pg.transform.scale_by(img, 0.5)
        rect = img.get_rect(topleft=(x, y))
        #skalerer det ned slik at den ikke er større enn spriten
        rect.width= int(round(rect.width/2))
        rect.height =int(round(rect.height/2))
        super().__init__(vx, vy, nytt_img, rect)
               
    
    def oppdater(self):
        super().oppdater()
        
        if FRI_BREDDE>=self.rect.left or self.rect.left>=(VINDU_BREDDE-FRI_BREDDE-self.rect.width) or  0 >= self.rect.top or self.rect.top>=(VINDU_HOYDE-self.rect.height):
            speed=(self.vx**2+self.vy**2)**(1/2)
            #finner vinkelen slik at den randomiserte farten ikke er vendt tilbake mot boksen
            vinkel = ((atan2(((self.rect.centery-(VINDU_HOYDE/2))),(self.rect.centerx-(VINDU_BREDDE/2)))-pi/4)//(pi/2))-1
            #booter den ut av hindringen
            self.rect.x+= round(cos(vinkel*pi/2))*speed
            self.rect.y+= round(sin(vinkel*pi/2))*speed
            #lager en tilfeldig vinkel som er vekk fra objektet
            ranvinkel=random.uniform(-pi/6+(vinkel*pi/2),pi/6+(vinkel*pi/2))
            self.vx=speed*cos(ranvinkel)
            self.vy=speed*sin(ranvinkel)
            
    

class Hindring(Objekt):
    def __init__(self):
        img = pg.image.load(IMAGE_DIR / "stein.png")
        scaled_img = pg.transform.scale_by(img, 0.3)
        posisjon_x = random.randint(FRI_BREDDE, VINDU_BREDDE-FRI_BREDDE)
        posisjon_y = random.randint(0, VINDU_HOYDE)
        rect = img.get_rect(topleft=(posisjon_x, posisjon_y))
          #skalerer det ned slik at den ikke er større enn spriten
        rect.width= int(round(rect.width*0.3))
        rect.height =int(round(rect.height*0.3))
        super().__init__(0, 0, scaled_img, rect)


