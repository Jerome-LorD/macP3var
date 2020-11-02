import settings


class CLIView:
    """Manage and display all prints"""

    def __init__(self, lab):

        self.lab = lab

        self.pic = " "
        self.items_taken = []
        self.images = {
            "tube": settings.TUBE_CHAR,
            "needle": settings.NEEDLE_CHAR,
            "ether": settings.ETHER_CHAR,
        }

    def get_lst_items(self):
        """docstr"""
        if len(self.items_taken) >= 1 and not self.lab.player.pos == self.lab.finish[0]:
            print(f'In your possession -> {" ".join(self.items_taken)}')
        if len(self.items_taken) == 3 and not self.lab.player.pos == self.lab.finish[0]:
            print(f"You got the syringe, you can get out -> {settings.SYRINGE_UNICODE}")

    def display_txt(self):
        """Display texts in the bottom frame"""
        if self.lab.collision_counter < 3 and self.lab.player.pos == self.lab.finish[0]:
            print(settings.LOSECLI)
        elif (
            self.lab.collision_counter == 3
            and self.lab.player.pos == self.lab.finish[0]
        ):
            print(settings.WINCLI)
        else:
            print("take all objects if you wanna get out.")

    def change_state(self):
        """Get the images and manage the filling of items_taken"""
        for name in self.lab.items_states.keys():
            if self.lab.items_states[name] == "found":
                self.lab.items_states[name] = "taken"
                self.items_taken.append(self.images[name])

    def display(self):
        """Display the game"""
        for pos_y in range(settings.WIDTH):
            for pos_x in range(settings.HEIGHT):
                position = pos_x, pos_y

                if position == self.lab.player.pos:
                    self.pic = settings.PLAYER_CHAR
                elif position == self.lab.items_position["tube"]:
                    self.pic = settings.TUBE_CHAR
                elif position == self.lab.items_position["needle"]:
                    self.pic = settings.NEEDLE_CHAR
                elif position == self.lab.items_position["ether"]:
                    self.pic = settings.ETHER_CHAR
                elif position in self.lab.wall:
                    self.pic = "X"
                elif position == self.lab.start:
                    self.pic = "S"
                elif position in self.lab.finish:
                    self.pic = "F"
                else:
                    self.pic = " "

                print(self.pic, end=" ")
            print()
        print()

        self.change_state()
        self.get_lst_items()
        self.display_txt()
