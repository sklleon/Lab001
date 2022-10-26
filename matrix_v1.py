import random

import pygame as pg


class MatrixLetters:
    def __init__(self, app):
        self.app = app
        self.letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789'
        self.font_size = 12
        self.font = pg.font.SysFont('arial', self.font_size, bold=True)
        self.columns = app.Width // self.font_size
        self.drops = [1 for i in range(0, self.columns)]

    def draw(self):
        for i in range(0, len(self.drops)):
            char = random.choice(self.letters)
            char_render = self.font.render(char, False, (0, 255, 255))
            pos = i * self.font_size, (self.drops[i]-1) * self.font_size
            self.app.surface.blit(char_render,pos)
            if self.drops[i] * self.font_size> app.Height and random.uniform(0,1)>0.975:
                self.drops[i]=0
            self.drops[i] += 1

    def run(self):
        self.draw()


class MatrixApp:
    def __init__(self):
        self.RES = self.Width, self.Height = 1000, 700
        pg.init()
        self.screen = pg.display.set_mode(self.RES)
        self.surface = pg.Surface(self.RES, pg.SRCALPHA)
        self.clock = pg.time.Clock()
        self.matrixLetters = MatrixLetters(self)

    def draw(self):
        # self.surface.fill(pg.Color('black'))
        self.surface.fill((0,0,0,10))
        self.matrixLetters.run()
        self.screen.blit(self.surface, (0, 0))

    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip()
            self.clock.tick(30)


# if __name__ == '__name__':
#     app = MatrixApp()
#     app.run()

app = MatrixApp()
app.run()
