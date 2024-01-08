import sys
combinations = [
    [1, 2, 3],
    [1, 4, 7],
    [1, 5, 9],
    [2, 5, 8],
    [3, 6, 9],
    [3, 2, 1],
    [3, 5, 7],
    [4, 5, 6],
    [7, 8, 9],
]
class PyTac():
    def __init__(self) -> None:
        self.grid = ["_" for x in range(9)]
        self.is_player_one = True

    def split_list(self):
        chunks = []
        for i in range(0, len(self.grid), 3):
            chunks.append(self.grid[i: i + 3])
        return chunks
    
    def check_winner(self):
        pi = "O" if self.is_player_one == True else "X"
        p = "one" if pi == "O" else "two"

        for c in combinations:
            if all(self.grid[(x - 1)] == pi for x in c ):
                print(f'Player {p} wins! Combination : {c}')
                return True

                
    def draw_grid(self):
        for row in self.split_list():
            s = ""
            for idx, block in enumerate(row):
                s += block
                if not idx == len(row) - 1:
                    s += " | "
            print(s)

    def play(self):
        while True:
            self.draw_grid()
            pos = []
            while True:
                user_input = input(f"Player {"one" if self.is_player_one == True else "two"} Pick the position you want:")
                # user_input = user_input.rstrip().lstrip()
                pos = user_input.split(" ")

                if len(pos) > 2:
                    print("You only need two coordinates. Try again.")
                    continue

                if not pos[0].isnumeric():
                    print("Only numbers are allowed. Try again.")
                    continue

                break

            try:
                if(self.grid[int(pos[0])] == "_"):
                    self.grid[int(pos[0])] = "O" if self.is_player_one == True else "X"
                else:
                    print("You can't override that block.")
                    continue
            except IndexError:
                print("Wrong coordinates. Try again.")
                continue

            if (self.check_winner()):
                self.draw_grid()
                return 0
            
            self.is_player_one = not self.is_player_one

            if all(map((lambda a : a != "_"), self.grid)):
                print("Draw!")
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
    # x.draw_grid()
    # x.check_winner(g=['O','_','_','O','_','_','O','_', '_'])