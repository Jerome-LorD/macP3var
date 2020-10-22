class CLIView:
    def __init__(self, lab, player):
        
        self.lab = lab
        self.player = player

        # self.holster = []
        self.player_img = PLAYER_CLI
        self.tube_img = TUBE_CLI
        self.needle_img = NEEDLE_CLI
        self.ether_img = ETHER_CLI
        self.pic = " "
        self.holster = []
        self.run = 1


    def you_win(self):
        print("Congats, You WIN")

    def you_lose(self):
        print("You lose, you die\nGAME OVER")


    def get_player_controls(self):
        self.direction = ""
        board = ["up", "right", "down", "left", "q"]
        try:        
            self.direction = str(input("Chose the direction: "))
        except ValueError:
            print('Invalid input! Type character please.')
            self.run = 1
        if self.direction == "q":
            print("thx, until next time")
            self.run = 0
        if self.direction not in board:
            print("Command not in the board")
            self.run = 1
        return

    def get_holster(self):
        if len(self.holster) >= 1:
            print(f'In your possession -> {"".join(self.holster)}')
        if len(self.holster) == 3:
            print("You got the syringe, you can get out -> \U0001F489")

    def display(self, player_pos):

        self.tube_pos = tuple(self.lab.tools_rand.__getitem__(0)[0])
        self.needle_pos = tuple(self.lab.tools_rand.__getitem__(1)[0])
        self.ether_pos = tuple(self.lab.tools_rand.__getitem__(2)[0])

        for pos_y in range(15):
            for pos_x in range(15):
                position = pos_x, pos_y

                if position == player_pos:
                    self.pic = self.player_img
                elif position == self.tube_pos:
                    self.pic = self.tube_img
                elif position == self.needle_pos:
                    self.pic = self.needle_img
                elif position == self.ether_pos:
                    self.pic = self.ether_img
                elif position in self.lab.wall:
                    self.pic = "X"
                elif position in self.lab.start:
                    self.pic = "S"
                elif position in self.lab.finish:
                    self.pic = "F"
                else:
                    self.pic = " "

                print(self.pic, end=" ")
            print()
        print()

        

        if self.lab.collide_tube(self.player.pos):
            self.holster.append(self.tube_img)
            self.tube_img = " "
        # self.get_holster()
        if self.lab.collide_needle(self.player.pos):
            self.holster.append(self.needle_img)
            self.needle_img = " "
        # self.get_holster()
        if self.lab.collide_ether(self.player.pos):
            self.holster.append(self.ether_img)
            self.ether_img = " "
        # self.get_holster()
        self.get_holster()
        if self.lab.collide_gatekeeper(self.player.pos) and len(self.holster) > 2:
            self.you_win()
            return 0
        if self.lab.collide_gatekeeper(self.player.pos) and len(self.holster) < 3:
            self.you_lose()
            return 0