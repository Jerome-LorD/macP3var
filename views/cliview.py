import settings as const


class CLIView:
    def __init__(self, lab):
        
        self.lab = lab

        self.pic = " "
        self.run = 1
        self.items_taken = []
        self.images = {"tube": const.TUBE_CHAR, "needle": const.NEEDLE_CHAR, "ether": const.ETHER_CHAR}


    def you_win(self):
        print(const.WINCLI)

    def you_lose(self):
        print(const.LOSECLI)

    def get_lst_items(self):
        if len(self.items_taken) >= 1:
            print(f'In your possession -> {" ".join(self.items_taken)}')
        if len(self.items_taken) == 3:
            print("You got the syringe, you can get out -> \U0001F489")



    def change_state(self):
        for name in self.lab.items_states.keys():
            if self.lab.items_states[name] == "found":
                self.lab.items_states[name] = "taken"
                self.items_taken.append(self.images[name])


    def display(self):
        print(self.lab.items_states)
        for pos_y in range(const.WIDTH):
            for pos_x in range(const.HEIGHT):
                position = pos_x, pos_y

                if position == self.lab.player.pos:
                    self.pic = const.PLAYER_CHAR
                elif position == self.lab.items_position["tube"]:
                    self.pic = const.TUBE_CHAR
                elif position == self.lab.items_position["needle"]:
                    self.pic = const.NEEDLE_CHAR
                elif position == self.lab.items_position["ether"]:
                    self.pic = const.ETHER_CHAR
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

        if self.lab.collision_counter < 3:
            print("take all objects if you wanna get out.") 

        self.change_state()
        self.get_lst_items()