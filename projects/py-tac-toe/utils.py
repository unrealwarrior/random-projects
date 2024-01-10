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
        chunks = []
        for i in range(0, len(grid), 3):
            chunks.append(grid[i: i + 3])
        return chunks