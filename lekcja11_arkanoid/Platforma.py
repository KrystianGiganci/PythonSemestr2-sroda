import pygame

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800


class Platforma(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Platforma, self).__init__()
        self.obraz = pygame.image.load("lekcja11_arkanoid/images/pad.png")
        self.porusza_sie = 0
        self.zresetuj_pozycje()

    def zresetuj_pozycje(self):
        self.pozycja = pygame.Rect(SZEROKOSC_EKRANU/2 - 70, WYSOKOSC_EKRANU-100, 140, 30)

    def ruszaj_platforma(self, wartosc):
        predkosc = 13
        self.pozycja.move_ip(wartosc*predkosc, 0)
        self.porusza_sie = wartosc
        if self.pozycja.left <= 0:
            self.pozycja.x = 0
        if self.pozycja.right >= SZEROKOSC_EKRANU:
            self.pozycja.x = SZEROKOSC_EKRANU - 140

    def aktualizuj(self):
        self.porusza_sie = 0
