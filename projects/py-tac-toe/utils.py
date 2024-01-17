from dataclasses import dataclass

@dataclass
class Utils():
    colors = {
    "HEADER" : '\033[95m',
    "BLUE" : '\033[94m',
    "CYAN" : '\033[96m',
    "GREEN" : '\033[92m',
    "WARNING" : '\033[93m',
    "FAIL" : '\033[91m',
    "ENDC" : '\033[0m',
    "BOLD" : '\033[1m',
    "UNDERLINE" : '\033[4m'
    }

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
    def __init__(self) -> None:
        pass

    def split_list(self, grid=None):
        if grid == None: grid = self.grid
        chunks = []
        for i in range(0, len(grid), 3):
            chunks.append(grid[i: i + 3])
        return chunks
    
    def color_print(self, c, msg):
        c = c.upper()
        print(self.colors[c] + msg + self.colors["ENDC"])
