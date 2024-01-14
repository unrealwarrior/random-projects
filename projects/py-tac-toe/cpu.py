from utils import Utils
import itertools
edge_blocks = [[0, 0], [0, 2], [2, 0], [2, 2]]

def flip_list(arr):
    ass = []
    for idx in range(len(arr)):
        x = []
        for index in range(len(arr[0])):
            x.append(arr[index][idx])
        ass.append(x)
    print(ass)
    return ass

class BotPlayer(Utils):
    def __init__(self, grid) -> None:
        # self.grid = grid
        pass    
    
    def check_surroundings(self, grid, pos):
        block = grid[pos[0]][pos[1]] 
        if block == "O" or block == "B":
            return False
        elif block == "_":
            return True
    
    def check_block_surroundings(self, pos_x, pos_y, grid):
        # split a one dimensional array to chunks
        g = self.split_list(grid=grid)
        direction_flag = ""
        # check if there's items on the left
        if (pos_y - 1) >= 0:
            direction_flag = "left"
        else:
            direction_flag = "right"
        print(f"Lookup direction: {direction_flag}")
        y = (pos_y - 1) if direction_flag == "left" else (pos_y + 1)
        b = g[pos_x][y]
        while True:
            print(f"Next block lookup: grid[{pos_x}][{y}]")

            if self.check_surroundings(grid=g, pos=(pos_x, y)):
                print(f"block at [{pos_x}][{y}] was added.")
                g[pos_x][y] = "B"
                return g
            else:
                if ((y - 1) < 0):
                    direction_flag = "right"
                    print("going right.")
                    y = pos_y       # restore initial position on the y-axis
                    continue
                else:
                    print("More blocks available. Looping...")
                    y = y - 1 if direction_flag == "left" else y + 1
                    if (y + 1) > len(g[0]):
                        print("No more lookups.")
                        return g
                    continue

        # else:
        #     print(f"No more blocks on the left of [{pos_x}][{pos_y}]")
        #     # check if there's blocks on the right 
        #     if (pos_y + 1) > (len(g[0]) - 1):
        #         print("no more blocks on the right.")
        #     else:
        #         y = pos_y + 1
        #         b = g[pos_x][y]
        #         if b == "O":
        #             flag = self.check_block_surroundings(pos_x, y, grid=[y for x in g for y in x])
        #         elif b == "_":                    
        #             print(f"block at [{pos_x}][{y}] was added.")
        #             g[pos_x][y] = "B"
        #             return g
                        
                            

                    
        # if axis == "y":
        #     # try the y-axis now
        #     g = flip_list(g)
        #     if (pos_x - 1) < 0:
        #         print("no more blocks above.")
        #         return flip_list(g)
        #     else:
        #         x = pos_x -1 
                
        #         b = g[x][pos_y]
        #         if b == "O":
        #             g = flip_list(g)
        #             flag = self.check_block_surroundings(x, pos_y, grid=[y for x in g for y in x], axis="y")
        #             if flag == False:
        #                 print("time to go somewhere.") 
        #             else:
        #                 g = flag
        #         elif b == "_":                    
        #             print(f"block at [{x}][{pos_y}] was added.")
        #             g[x][pos_y] = "B"
        #             g = flip_list(g)
        #             print("test")
        #             return g
                
        #     if (pos_x + 1) > (len(g[0]) - 1):
        #         print("no more blocks below.")
        #         return flip_list(g)
        #     else:
        #         x = pos_x + 1
                
        #         b = g[x][pos_y]
        #         if b == "O":
        #             g = flip_list(g)
        #             flag = self.check_block_surroundings(x, pos_y, grid=[y for x in g for y in x])
        #             if flag == False:
        #                 print("time to go somewhere.") 
        #             else:
        #                 g = flag
        #         elif b == "_":                    
        #             print(f"block at [{x}][{pos_y}] was added.")
        #             g[x][pos_y] = "B"
        #             g = flip_list(g)
        #             print("test")
        #             return g




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

grid = ["O","_","_","_","_","_","_","_","_",]
while True:
    coords = input("> enter your coordinates: ")
    posx, posy = coords.split(" ")
    pos = (int(posx) * 3) + int(posy)
    grid[pos] = 'O'
    grid = x.check_block_surroundings(pos_x=int(posx), pos_y=int(posy), grid=[grid for x in grid for grid in x])
    print([print(g) for g in grid])
    grid = [grid for x in grid for grid in x]
