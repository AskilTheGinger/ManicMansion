from constants import *
import pygame as pg
import random as random

class Menneske:
    def __init__(self,hoyde:int,bredde:int) -> None:
        self.rect = pg.Rect(hoyde,bredde,HINDRING_STR,HINDRING_STR)
        

class Spokelse:
    def __init__(self,v:int) -> None:
        self.rect=pg.Rect(random.randint(0,VINDU_BREDDE),random.randint(0,VINDU_HOYDE),HINDRING_STR,HINDRING_STR)
        self.v= v

        
        


class Hindring:
    def __init__(self) -> None:
        self.farge = random.choice(FARGER)
        self.rect=pg.Rect(random.randint(0,VINDU_BREDDE),random.randint(0,VINDU_HOYDE),HINDRING_STR,HINDRING_STR)
    def draw(self,vindu:pg.Surface):
        pg.draw.rect(vindu,ORANGE,self.rect)
        


class Sau:
    def __init__(self) -> None:
        self.rect=pg.Rect(random.randint(0,VINDU_BREDDE),random.randint(0,VINDU_HOYDE),HINDRING_STR,HINDRING_STR)

        

