import sys
from utils import Utils
from cpu import BotPlayer
import itertools

class PyTac(Utils, BotPlayer):
    def __init__(self) -> None:
        self.grid = ["_" for _ in range(9)]
        self.is_player_one = True
    
    # determine winner
    def check_winner(self):
        pi = "O" if self.is_player_one == True else "X"
        p = "one" if pi == "O" else "two"
        g = self.flatten_list(grid=self.grid)
        for c in self.combinations:
            print(c)
            if all(g[(x - 1)] == pi for x in c ):
                print(f'Player {p} wins! Combination : {c}')
                return True
            return False
      
    # draw grid on console
    def draw_grid(self, grid=None):
        if grid == None: grid = self.grid
        # grid = self.split_list(grid)
        new_grid = ""
        for row in grid:
            for idx, block in enumerate(row):
                new_grid += block
                if not idx == len(row) - 1:
                    new_grid += " | "
            new_grid += "\n"
        print(new_grid)
        return new_grid

    def play(self):
        self.grid = self.split_list()
        while True:
            self.draw_grid()
            pos = []

            while True:
                user_input = input(f"Player {"one" if self.is_player_one == True else "two"} Pick the position you want:")
                pos = user_input.split(" ")
                if not pos[0].isnumeric() and not pos[1].isnumeric():
                    print("Only numbers are allowed. Try again.")
                    continue

                x = int(pos[0]) 
                y = int(pos[1])
                break

            try:
                if(self.grid[x][y] == "_"):
                    self.grid[x][y] = "O" if self.is_player_one == True else "X"
                else:
                    print("You can't override that block.")
                    continue
            except IndexError:
                print("Wrong coordinates. Try again.")
                continue
            self.check_block_surroundings(pos_x=x, pos_y=y, grid=list(itertools.chain(*self.grid)))

            winner = self.check_winner()
            print(winner)
            # self.is_player_one = not self.is_player_one
            if winner or (all(map((lambda a : a != "_"), self.flatten_list(grid=self.grid)))):      # tried self.check_winner() but for some reason did not work.
                if not winner : print("Draw!")
                while True:
                    u = input("Do you wanna play again? : ")
                    if u in ["Y", "y"]:
                        self.reset_game()
                        break
                    elif u in ["N", "n"]:
                        sys.exit()
                    else:
                        print("Wrong input. Try again.")
                        continue
    
    def reset_game(self):
        self.is_player_one = True
        self.grid = ["_" for x in range(9)]


if __name__ == "__main__":
    x = PyTac()
    x.play()
