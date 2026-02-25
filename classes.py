from constants import *
import pygame as pg
import random as random
from dataclasses import dataclass

@dataclass(slots=True)
class Objekt:
    vx: int
    vy: int
    img: pg.Surface
    x: int
    y: int

    def draw(self, vindu: pg.Surface):
        vindu.blit(self.img, (self.x, self.y))
       
    

class Menneske(Objekt):
    def __init__(self):
        img = pg.image.load(IMAGE_DIR / "sprites/spøkelse.png")
        x = 100
        y = VINDU_HOYDE//2
        super().__init__(0, 0, img, x, y)
        self.rect = self.img.get_rect(topleft=(x, y))

class Spokelse(Objekt):
    class Spokelse(Objekt):
        def __init__(self):
            x = random.randint(0, VINDU_BREDDE)
            y = random.randint(0, VINDU_HOYDE)
            img = pg.image.load(IMAGE_DIR / "sprites/spøkelse.png")
            super().__init__(0, 0, img, x, y)
            self.rect = self.img.get_rect(topleft=(x, y))
        


class Hindring(Objekt):
    def __init__(self) -> None:
        img = pg.image.load(IMAGE_DIR / "sprites/spøkelse.png")
        x = 200
        y = 320
        super().__init__(0, 0, img, x, y)    

        


class Sau(Objekt):
    def __init__(self):
        super().__init__(
            vx = 0,
            vy = 0,
            img = pg.image.load("sau.png"),
            x = random.randint(0, VINDU_BREDDE),
            y = random.randint(0, VINDU_HOYDE)
        )
        

