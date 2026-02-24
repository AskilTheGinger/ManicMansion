from constants import *
import pygame as pg
import random as random
from dataclasses import dataclass

@dataclass(slots=True)
class Objekt:
    vx = int
    vy = int
    img = str
    x = int
    y = int


    def draw(self, vindu:pg.Surface):
        vindu.blit(self.img, (self.x, self.y))
    

class Menneske(Objekt):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
        
        self.rect = pg.Rect(hoyde,bredde,HINDRING_STR,HINDRING_STR)

class Spokelse:
    def __init__(self,v:int) -> None:
        self.rect=pg.Rect(random.randint(0,VINDU_BREDDE),random.randint(0,VINDU_HOYDE),HINDRING_STR,HINDRING_STR)
        self.v= v
        self.img = IMAGE_DIR/"sprites/spøkelse.png"
        


class Hindring(Objekt):
    def __init__(self) -> None:
        self.farge = random.choice(FARGER)
        self.rect=pg.Rect(random.randint(0,VINDU_BREDDE),random.randint(0,VINDU_HOYDE),HINDRING_STR,HINDRING_STR)
    def draw(self,vindu:pg.Surface):
        pg.draw.rect(vindu,ORANGE,self.rect)
        


class Sau(Objekt):
    def __init__(self) -> None:
        self.rect=pg.Rect(random.randint(0,VINDU_BREDDE),random.randint(0,VINDU_HOYDE),HINDRING_STR,HINDRING_STR)

        

