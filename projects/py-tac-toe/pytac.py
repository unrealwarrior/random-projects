combinations = [
    [1, 2, 3],
    [1, 5, 7],
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
    
    def check_winner(self, g=None):
        p = "O" if self.is_player_one == True else "X"

        for c in combinations:
            if all(g[(x - 1)] == p for x in c ):
                return print(f'you win! combination : {c}')

                




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
                print(user_input)
                pos = user_input.split(" ")

                if len(pos) > 2:
                    print("You only need two coordinates. Try again.")
                    continue

                if not pos[0].isnumeric() or not pos[1].isnumeric():
                    print("Only numbers are allowed. Try again.")
                    continue

                break

            try:
                self.grid[int(pos[0])][int(pos[1])] = "O" if self.is_player_one == True else "X"

            except IndexError:
                print("Wrong coordinates. Try again.")
                continue

            self.is_player_one = not self.is_player_one


if __name__ == "__main__":
    x = PyTac()
    x.draw_grid()
    x.check_winner(g=['O','_','_','_','O','_','_','_','O'])