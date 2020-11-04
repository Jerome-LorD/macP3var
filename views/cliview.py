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
        """Display items taken and texts"""
        items = [
            item
            for item, pos in self.lab.items_position.items()
            if not self.lab.items_position[item]
        ]
        if items:
            print(f"{settings.POSSESSION} {' '.join(items)}")

        if (
            self.lab.collision_counter == 3
            and not self.lab.player.pos == self.lab.finish[0]
        ):
            print(f"{settings.GOT_SYRINGE} {settings.SYRINGE_UNICODE}")
        if self.lab.collision_counter < 3\
                and self.lab.player.pos == self.lab.finish[0]:
            print(settings.LOSECLI)
            self.lab.run_state = 1

        if (
            self.lab.collision_counter == 3
            and self.lab.player.pos == self.lab.finish[0]
        ):
            print(f"{settings.WINCLI} {settings.SYRINGE_UNICODE}")
            self.lab.run_state = 1

        if (
            self.lab.collision_counter < 3
            and not self.lab.player.pos == self.lab.finish[0]
            and self.lab.run_state == 0
        ):
            print(settings.ADVICE)

    def header(self):
        """Display header"""
        print(
            f"\n{settings.DASHES}\n{settings.HEADER}\n\
{settings.DASHES}"
        )

    def display(self):
        """Display the game"""
        self.header()

        reversed_items_position = {
            pos: name for name, pos in self.lab.items_position.items()
        }

        for pos_y in range(settings.WIDTH):
            for pos_x in range(settings.HEIGHT):
                position = pos_x, pos_y

                if position == self.lab.player.pos:
                    self.pic = settings.PLAYER_CHAR
                elif position in self.lab.items_position.values():
                    self.pic = self.images[reversed_items_position[position]]
                elif position in self.lab.walls:
                    self.pic = "X"
                elif position == self.lab.starts:
                    self.pic = "S"
                elif position in self.lab.finish:
                    self.pic = "F"
                else:
                    self.pic = " "

                print(self.pic, end=" ")
            print()
        print()

        self.display_items_taken()
