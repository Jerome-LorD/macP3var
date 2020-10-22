class PYView:
    def __init__(self, lab, player):
        self.lab = lab
        self.player = player

        self.holster = []

        self.reso = 40
        self.run = 1

        self.wall = pygame.transform.scale2x(spritesheet("floor-tiles-20x20.png").image_at((340,100,20,20)))
        self.startpol = pygame.transform.scale2x(spritesheet("floor-tiles-20x20.png").image_at((160,20,20,20)))

        self.plastic_tube = pygame.transform.scale(spritesheet("tube_plastique_3.png").image_at((0,0,259,194)), (30,30))
        self.plastic_tube2 = pygame.transform.scale(spritesheet("tube_plastique_3.png").image_at((0,0,259,194)), (35, 35))
        self.ether = pygame.transform.scale(spritesheet("ether.png").image_at((0,0,225,225)), (30,30))
        self.ether2 = pygame.transform.scale(spritesheet("ether.png").image_at((0,0,225,225)), (35, 35))
        self.needle = pygame.transform.scale(spritesheet("aiguille.png").image_at((0,0,545,720)), (30,30))
        self.needle2 = pygame.transform.scale(spritesheet("aiguille.png").image_at((0,0,545,720)), (35,35))
        self.syringe = pygame.transform.scale(spritesheet("seringue.png").image_at((0,0,90,90)), (30,30))
        
        self.gatekeeper = spritesheet("gardien.png").image_at((0,0,40,40))
        self.macgyver = spritesheet("MacGyver.png").image_at((0,0,40,40))


        self.take_tube = False
        self.take_needle = False
        self.take_ether = False

        self.font = set_font("Ranchers-Regular.ttf")
        self.make_syringe = self.font.render("Make a syringe", True, (255,255,255), (0,0,0))
        self.you_win = "Congrats, you win!"
        self.lose = "You lose! you die... GAME OVER !!!"
        self.bvo = self.font.render("Nice job! Now, you can get out.", True, (255,255,255), (0,0,0))
        self.endgame_w = self.font.render(self.you_win, True, (0,255,0), (0,0,0))
        self.endgame_l = self.font.render(self.lose, True, (255,0,0), (0,0,0))

        self.cadre = self.endgame_w.get_rect(topleft=(30,610))
        self.cadre_box = pygame.Rect(0,603,600,53)
        self.white = (255, 255, 255)

    def get_player_controls(self):
        self.direction = self.player.pos
        for event in pygame.event.get():
            if event.type == QUIT:
                self.run = 0
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.direction = self.player.move("left")
                elif event.key == K_UP:
                    self.direction = self.player.move("up")
                elif event.key == K_RIGHT:
                    self.direction = self.player.move("right")
                elif event.key == K_DOWN:
                    self.direction = self.player.move("down")
        return 1

    def get_holster(self):
        if len(self.holster) >= 1:
            for i in range(len(self.holster)):
                if self.holster[i] == self.plastic_tube2:
                    self.plastic_tube = pygame.transform.scale(self.plastic_tube, (0, 0))
                    screen.blit(self.holster[i], (455,610))
                elif self.holster[i] == self.needle2:
                    self.needle = pygame.transform.scale(self.needle, (0, 0))
                    screen.blit(self.holster[i], (500,610))
                elif self.holster[i] == self.ether2:
                    self.ether = pygame.transform.scale(self.ether, (0, 0))
                    screen.blit(self.holster[i], (545,610))
        # if len(self.holster) == 3:
        #     self.blit_you_can_get_out()



    def blit_wall(self, struct):
        for wall_pos in struct.wall_lst:
            screen.blit(self.wall, tuple(wall_pos))

    def blit_start(self, struct):
        screen.blit(self.startpol, tuple(struct.start))

    def blit_player(self, player_pos):
        screen.blit(self.macgyver, player_pos)

    def blit_gatekeeper(self, struct):
        screen.blit(self.gatekeeper, tuple(struct.finish))

    def blit_tube(self, tube_pos):
        screen.blit(self.plastic_tube, tuple(tube_pos))

    def blit_needle(self, needle_pos):
        screen.blit(self.needle, tuple(needle_pos))

    def blit_ether(self, ether_pos):
        screen.blit(self.ether, tuple(ether_pos))

    def blit_syringe(self):
        screen.blit(self.syringe, self.player.pos+(0,20)) # self.player.pos+(20,20)|(410, 612)

    def blit_border(self):
        pygame.draw.rect(background, self.white, self.cadre_box, 10)

    def blit_make_syringe(self):
        screen.blit(self.make_syringe, (30, 610))

    def blit_you_win(self):
        screen.blit(self.endgame_w, (30, 610))

    def blit_you_lose(self):
        screen.blit(self.endgame_l, (30, 610))

    def blit_you_can_get_out(self):
        screen.blit(self.bvo, (30, 610))