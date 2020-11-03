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

    def display_items_taken(self):
        """Display items and texts"""
        items = [
            item
            for item, pos in self.lab.items_position.items()
            if not self.lab.items_position[item]
        ]
        print(f"In your possession -> {' '.join(items)}")

        if (
            self.lab.collision_counter == 3
            and not self.lab.player.pos == self.lab.finish[0]
        ):
            print(f"{settings.GOT_SYRINGE} {settings.SYRINGE_UNICODE}")
        if (
            self.lab.collision_counter < 3
            and self.lab.player.pos == self.lab.finish[0]
        ):
            print(settings.LOSECLI)        
            self.lab.run = False
        # if self.lab.lose == True:

            
        if (
            self.lab.collision_counter == 3
            and self.lab.player.pos == self.lab.finish[0]
        ):
            print(settings.WINCLI)        
            self.lab.run = False


        if (
            self.lab.collision_counter < 3
            and not self.lab.player.pos == self.lab.finish[0]
        ):
            print("take all objects if you wanna get out.")

    def header(self):
        self.dashes = "# ------------------------- #"
        print(
            f"\n{self.dashes}\n#-MacGyver -- Get out vc-1 -#\n\
{self.dashes}"
        )

    def display(self):
        """Display the game"""
        self.header()

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

        self.display_items_taken()
