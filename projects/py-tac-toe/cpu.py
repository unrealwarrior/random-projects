from utils import Utils
import itertools
edge_blocks = [[0, 0], [0, 2], [2, 0], [2, 2]]

class BotPlayer(Utils):
    def __init__(self, grid) -> None:
        self.grid = grid
    
    def _add_block(self, grid, pos):
        grid[pos[0]][pos[1]] = "O"
        return grid
    
    def check_block_surroundings(self, pos_x, pos_y, grid):
        g = self.split_list(grid=grid)
        # last played position
        # pos_x = pos_x - 1
        # pos_y = pos_y - 1
        # g = self._add_block(g, pos=(pos_x, pos_y))

        # check if there's items on the left
        if (pos_y - 1) < 0:
            print(f"No more blocks on the left of [{pos_x}][{pos_y}]")
            return False
        else:
            y = pos_y - 1
            b = g[pos_x][y]
            if b == "O":
                flag = self.check_block_surroundings(pos_x, y, grid=[y for x in g for y in x])  
                if flag == False:
                    print("time to go right.") 
                else:
                    g = flag
                
                    
            elif b == "_":                    
                print(f"block at [{pos_x}][{y}] was added.")
                g[pos_x][y] = "B"
                return g
        if (pos_y + 1) > (len(g[0]) - 1):
            print("no more blocks on the right.")
        else:
            y = pos_y + 1
            b = g[pos_x][y]
            if b == "O":
                flag = self.check_block_surroundings(pos_x, y, grid=[y for x in g for y in x])
                if flag == False:
                    print("time to go somewhere.") 
                else:
                    g = flag
            elif b == "_":                    
                print(f"block at [{pos_x}][{y}] was added.")
                g[pos_x][y] = "B"
                return g


        return g






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
z = x.check_block_surroundings(pos_x=0, pos_y=2, grid=["_","O","_","_","_","_","_","_","_",])
[print(x) for x in z]


# g = ["_","_","_","_","_","_","_","_","_",]
# g = x.split_list(g)
# # z = [y for x in g for y in x]
# print(z)