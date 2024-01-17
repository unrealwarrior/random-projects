from utils import Utils
import itertools
import sys
import random
edge_blocks = [[0, 0], [0, 2], [2, 0], [2, 2]]


class BotPlayer():
    def __init__(self, grid) -> None:
        self.grid = grid
        pass    
    
    def flatten_list(self, grid=None):
        new_list = []
        for row in grid:
            for block in row:
                new_list.append(block)
        return new_list
    

    def flip_list(self, grid=None, reverse=False):
        if grid : self.grid = grid
        new_grid = []
        for idx in range(len(self.grid)):
            x = []
            for index in range(len(self.grid[0])):
                x.append(self.grid[index][idx]) if reverse else x.append(self.grid[idx][index])
            new_grid.append(x)
        return new_grid
    
    def check_surroundings(self, grid, pos):

        print(pos[1] >= len(grid[0]))
        if pos[1] < 0 or pos[1] >= len(grid[0]):
            return False
        block = grid[pos[0]][pos[1]] 
        if block == "O" or block == "B":
            return False
        elif block == "_":
            return True
    
    def check_block_surroundings(self, pos_x, pos_y, grid):
        # split a one dimensional array to chunks
        g = self.split_list(grid=grid)
        self.grid = g
        axis = "y"          
        direction_flag = ""
        # if bot plays first, let him check a random block
        if list(map(lambda a : a == "_", [y for x in g for y in x])):
            print("test")
            g = self.get_random_block(grid=g)
            return g
        
        # check if there's items on the left
        if (pos_y - 1) >= 0:
            direction_flag = "left"
        else:
            direction_flag = "right"
        print(f"Lookup direction: {direction_flag}")
        # y = (pos_y - 1) if direction_flag == "left" else (pos_y + 1)
        y = pos_y
        x = pos_x
        while True:
            print(f"Next block lookup: grid[{x}][{y}]")
            # check for random strategies ex: O|_|_ or _|O|_ 
            if self.check_surroundings(grid=g, pos=(x, y)):
                print(f"block at [{x}][{y}] was added.")
                g[x][y] = "B"
                return g if axis == "y" else self.flip_list(grid=g, reverse=True)
            else:
                if ((y - 1) < 0):
                    direction_flag = "right"
                    print("going right.")
                    y = (pos_y + 1) if axis == "y" else (pos_x + 1)     # restore initial position on the x-axis
                    continue
                else:
                    print("More blocks available. Looping...")
                    y = y - 1 if direction_flag == "left" else y + 1

                    if (y + 1) > len(g[0]):
                        if axis == "x":
                            print("No more blocks to fill.")
                            return g
                        print("No more lookups.")
                        direction_flag = "left"
                        axis = "x"
                        y = pos_x - 1   # restore x-axis initial position for y-axis lookup
                        x = pos_y
                        print("flipping positions")
                        g = self.flip_list(reverse=True)
                        print(g)
                        continue                     
                    # continue

    def get_random_block(self, grid):
        # flatten the grid
        g = self.flatten_list(grid)
        ids = []
        for index, block in enumerate(g):
            if block == "_":
                ids.append(index)
        i = random.choice(ids)
        g[i] = "B"
        return self.split_list(grid=g)

     

    def add_block(self, pos_x, pos_y):
        g = self.split_list()
        if g[pos_x][pos_y] == "O" or g[pos_x][pos_y] == "X":
            return False
        else:
            g[pos_x][pos_y] = "B"
            return g
        
    def bot_play(self, last_pos = 1):

        # split grid into three diffrent chunks
        new_grid = self.split_list()

        # player's last move in chunked grid
        x_pos, y_pos = divmod((last_pos - 1) , 3)
        
        # debug
        new_grid[x_pos][y_pos] = "X"
        new_grid[1][1] = "X"


        print(f'x: {x_pos}')
        print(f"y: {y_pos}")

        # if the player picked one of the four edges
        # check from the middle if there's a chance of winning

        if [x_pos, y_pos] in [e for e in edge_blocks]:
            # find out if the mid one is occupied by the player
            if new_grid[1][1] == "X":
                if new_grid[0][0] == "X":
                    new_grid[2][2] = "B"

                elif new_grid[0][2] == "X":
                    new_grid[2][0] = "B"

                elif new_grid[2][0] == "X":
                    new_grid[0][2] = "B"

                elif new_grid[2][2] == "X":
                    new_grid[0][0] = "B"
   

        self.grid = list(itertools.chain(*new_grid))
        [print(x) for x in new_grid]
        print(self.grid)


        
if __name__ == "__main__":
    grid = ["_","_","_","_","_","_","_","_","_"]
    x = BotPlayer(grid)
    # x.bot_play()

    # grid = ["_","2","3","_","5","6","_","8","9",]
    while True:
        if(all(map(lambda a: a != "_", grid))):
            print("all blocks were played.")
            sys.exit()
        # coords = input("> enter your coordinates: ")
        # posx, posy = coords.split(" ")
        # pos = (int(posx) * 3) + int(posy)
        # grid[pos] = 'O'
        posx = 0
        posy = 0
        grid = x.check_block_surroundings(pos_x=int(posx), pos_y=int(posy), grid=[grid for x in grid for grid in x])
        [print(g) for g in grid]
        grid = [grid for x in grid for grid in x]
