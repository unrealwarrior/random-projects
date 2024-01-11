from utils import Utils
import itertools
edge_blocks = [[0, 0], [0, 2], [2, 0], [2, 2]]

class BotPlayer(Utils):
    def __init__(self, grid) -> None:
        self.grid = grid
    
    def _add_block(self, grid, pos):
        grid[pos[0]][pos[1]] = "X"
        return grid
    
    def check_block_surroundings(self, pos_x, pos_y, grid):
        g = self.split_list(grid=grid)
        pos_x = pos_x - 1
        pos_y = pos_y - 1
        g = self._add_block(g, pos=(pos_x, pos_y))
       
        

        if (pos_x - 1) < 0:
            print("no more items on the left.")

        try:

            if g[pos_x][(pos_y + 1)] == "X":
                print("+1 triggered.")
                g[pos_x][(pos_y + 2)] = "B"

        except IndexError:
            print("out of range")


        # check block surroundings on the x-axis
        try:
            if g[pos_x][(pos_y - 1)] == "X":
                g[pos_x][(pos_y - 2)] = "B"
                
            else:
                print("no items on the left of the block.")
        except IndexError:
            print("out of range.")
        # # check block surroundings on the y-axis

        # if (pos_y - 1) < 0:
        #     print("no more items above.")
        
        # # it's a 3x3 grid, doesn't matter
        # if (pos_y + 1) > len(g[0]):
        #     print("no more items below.")

        # if g[pos_x][(pos_y - 1)] == "X":
        #     g[pos_x][(pos_y + 1)] == "B"

        # elif g[pos_x][(pos_y + 1)] == "X":
        #     g[pos_x][(pos_y - 1)] == "B"


        [print(x) for x in g]     



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


        

x = BotPlayer(["_","_","_","_","_","_","_","_","_",])
# x.bot_play()
x.check_block_surroundings(pos_x=1, pos_y=3, grid=["X","_","_","_","_","_","_","_","_",])
