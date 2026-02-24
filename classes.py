from constants import *
import pygame as pg
import random as random

class Menneske:
    def __init__(self) -> None:
        pass

class Spokelse:
    def __init__(self) -> None:
        self.rect=pg.Rect(random.randint(0,VINDU_BREDDE),random.randint(V))

        pass

class Hindring:
    def __init__(self) -> None:
        self.farge = random.choice(FARGER)

        pass


class Sau:
    def __init__(self) -> None:
        pass
