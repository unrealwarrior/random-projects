from dataclasses import dataclass

@dataclass
class Utils():
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
    
    def flatten_list(self, grid=None):
        if grid == None: grid = self.grid
        new_list = []
        for row in grid:
            for block in row:
                new_list.append(block)
        return new_list

