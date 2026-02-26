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

    def draw(self, vindu: pg.Surface):
        vindu.blit(self.img, self.rect)
       

class Menneske(Objekt):
    def __init__(self):
        img = pg.image.load(IMAGE_DIR / "menneske.png")
        rect = img.get_rect(topleft=(100, VINDU_HOYDE // 2))
        super().__init__(0, 0, img, rect)


class Spokelse(Objekt):
    def __init__(self):
        x = FRI_BREDDE + random.randint(0, VINDU_BREDDE - FRI_BREDDE)
        y = random.randint(0, VINDU_HOYDE)
        img = pg.image.load(IMAGE_DIR / "spøkelse.png")
        rect = img.get_rect(topleft=(x, y))
        super().__init__(0, 0, img, rect)


class Hindring(Objekt):
    def __init__(self):
        img = pg.image.load(IMAGE_DIR / "spøkelse.png")
        rect = img.get_rect(topleft=(200, 320))
        super().__init__(0, 0, img, rect)


class Sau(Objekt):
    def __init__(self):
        img = pg.image.load("sau.png")
        rect = img.get_rect(topleft=(
            random.randint(0, VINDU_BREDDE),
            random.randint(0, VINDU_HOYDE)
        ))
        super().__init__(0, 0, img, rect)