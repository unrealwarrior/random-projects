from utils import Utils
import itertools
import sys
import random


class BotPlayer():
    edge_blocks = [[0, 0], [0, 2], [2, 0], [2, 2]]
    def __init__(self, grid) -> None:
        # self.grid = grid
        pass    

    def flip_list(self, grid=None, reverse=False):
        new_grid = []
        for idx, _ in enumerate(grid):
            x = []
            for index in range(len(grid[0])):
                x.append(grid[index][idx]) if reverse else x.append(grid[idx][index])
            new_grid.append(x)
        self.grid = new_grid
        return new_grid
    
    def check_surroundings(self, grid, pos):
        if pos[1] < 0 or pos[1] >= len(grid[0]):
            return False
        
        # check surroundings on the last player mark
        # pick a random empty adjecent block and return it

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
        if all(map(lambda a : a == "_", [y for x in g for y in x])):
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
            # check random strategies
            if pos_x == 1 and pos_y == 1:
                flag = self.check_edge_blocks(pos=(x, y))
                if flag:
                    return g if axis == "y" else self.flip_list(grid=g, reverse=True)
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
                        print("before")
                        print(g)
                        g = self.flip_list(g, reverse=True)
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
        
    def check_edge_blocks(self, pos):
        print("checking edge blocks strategy")
        # split grid into three diffrent chunks
        print(self.grid)
        # # player's last move in chunked grid
        # x_pos, y_pos = divmod((last_pos - 1) , 3)
        
        # # debug
        # self.grid[x_pos][y_pos] = "X"
        # self.grid[1][1] = "X"

        print(f'x: {pos[0]}')
        print(f"y: {pos[1]}")

        # if the player picked one of the four edges
        # check from the middle if there's a chance of winning

        # find out if the mid one is occupied by the player
        available_edges = []
        print(pos)
        for e in self.edge_blocks:
            if self.grid[e[0]][e[1]] == "_":
                available_edges.append(e)
        if len(available_edges) > 0:
            rand = random.choice(available_edges)
            self.grid[rand[0]][rand[1]] = "B"
            # self.grid = list(itertools.chain(*self.grid))
            print(self.grid)
            return True
        else:
            return False


        
if __name__ == "__main__":
    grid = ["_","_","_","_","_","_","_","_","_"]
    x = BotPlayer(grid)
    # x.bot_play()

    # grid = ["_","2","3","_","5","6","_","8","9",]
    while True:
        # x.flip_list(grid=[["1","2","3"],["1","2","3"],["1","2","3"]], reverse=False)
        # print("false")
        # x.flip_list(grid=[["1","2","3"],["1","2","3"],["1","2","3"]], reverse=True) # true reverses
        if(all(map(lambda a: a != "_", grid))):
            print("all blocks were played.")
            sys.exit()
        coords = input("> enter your coordinates: ")
        posx, posy = coords.split(" ")
        pos = (int(posx) * 3) + int(posy)
        grid[pos] = 'O'
        # posx = 0
        # posy = 0
        grid = x.check_block_surroundings(pos_x=int(posx), pos_y=int(posy), grid=[grid for x in grid for grid in x])
        [print(g) for g in grid]
        grid = [grid for x in grid for grid in x]
