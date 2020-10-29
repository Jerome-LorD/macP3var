import os
import settings as const
import pygame as pg
from pygame.locals import *

main_dir = os.path.split(os.path.abspath(__file__))[0][:-5] # 

class PYView:
    def __init__(self, lab):
        pg.display.init()
        pg.init()

        self.lab = lab
        self.res = ()
        
        self.screen_size = 600, 660
        self.screen = pg.display.set_mode(self.screen_size)
        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((255, 0, 0))

        pg.display.set_caption("MacGyver - V1.0")
        self.fps = 30

        self.font = self.set_font("Ranchers-Regular.ttf")
        self.make_syringe = self.font.render("Make a syringe", True, (255,255,255), (0,0,0))
        self.you_win = "Congrats, you win!"
        self.lose = "You lose! you die... GAME OVER !!!"
        self.bvo = self.font.render("Nice job! Now, you can get out.", True, (255,255,255), (0,0,0))
        self.endgame_w = self.font.render(self.you_win, True, (0,255,0), (0,0,0))
        self.endgame_l = self.font.render(self.lose, True, (255,0,0), (0,0,0))

        self.cadre_box = pg.Rect(0,603,600,53)        
        self.cadre = self.endgame_w.get_rect(topleft=(30,610))

        self.white = (255, 255, 255)
        pg.draw.rect(self.background, self.white, self.cadre_box, 10) 


    def set_font(self, filename):
        fonts_dir = os.path.join(main_dir, "data\\fonts\\Ranchers")  
        if filename is not None:
            font_base = os.path.join(fonts_dir, filename)
            try:
                font = pg.font.Font(font_base, 30)
            except FileNotFoundError:
                raise SystemExit(f"Cannot load file: {filename}")
            return font


    def set_img(self, filename):
        sprites_dir = os.path.join(main_dir, "data\\ressource")
        if filename is not None:
            img = os.path.join(sprites_dir, filename)
            try:
                return pg.image.load(img).convert_alpha()
            except FileNotFoundError:
                raise SystemExit(f"Cannot load image: {filename}")
    def blit_txt(self):
        pg.draw.rect(self.background, self.white, self.cadre_box, 10)

    
    def display(self):
        
        for y in range(const.WIDTH):
            for x in range(const.HEIGHT):
                position = x, y
                
                if position == self.lab.player.pos:
                    self.res = self.set_img("MacGyver3.png"), (x * 40, y * 40)
                elif position == self.lab.items_position["tube"]:
                    self.res = self.set_img("tube_plastique2.png"), (x * 40, y * 40)
                elif position == self.lab.items_position["needle"]:
                    self.res = self.set_img("aiguille2.png"), (x * 40, y * 40)
                elif position == self.lab.items_position["ether"]:
                    self.res = self.set_img("ether2.png"), (x * 40, y * 40)                    
                elif position in self.lab.wall:
                    self.res = self.set_img("brick.png"), (x * 40, y * 40)
                elif position in self.lab.start:
                    self.res = self.set_img("start.png"), (x * 40, y * 40)
                elif position in self.lab.finish:
                    self.res = self.set_img("gardien2.png"), (x * 40, y * 40)
                elif position in self.lab.road:
                    self.res = self.set_img("fond.png"), (x * 40, y * 40)

                self.screen.blit(self.res[0],self.res[1])
                
                pg.display.flip()
