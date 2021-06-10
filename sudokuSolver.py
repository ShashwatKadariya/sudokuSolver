# sudoku grid
grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(grid):
    empty = checkEmpty(grid)

    if not empty:
        return True
    else:
        y, x = empty

    for i in range(1, 10):
        if check(y, x, i, grid):
            grid[y][x] = i

            if solve(grid):
                return True

            grid[y][x] =  0
    return False


def checkEmpty(grid):
    k = len(grid)
    for i in range(k):
        for j in range(k):
            if grid[i][j] == 0:
                return i, j

    return False


def drawGrid(grid):
    j = len(grid)

    for i in range(j):
        print(grid[i])


def check(y, x, n, grid):
    j = len(grid)

    for i in range(j):
        if n == grid[y][i] and x != i:
            return False

    for i in range(j):
        if n == grid[i][x] and y != i:
            return False

    # here y//3 can have value 0, 1, 2
    # so, max y value we will get here is 2
    # here the grid is divided into individual 3 * 3 grid
    # so if our value is 2 then it means we are in third 3 * 3 grid
    # so if we multiply it with 3 we get 6 and we will search the 6th y position in grid
    # and in our loop if we add 2 with it we get 8, which is our maximum y position
    # same is true for x position

    gridY = y // 3 * 3
    gridX = x // 3 * 3

    for i in range(3):
        for j in range(3):
            if grid[gridY + i][gridX + j] == n:
                return False
    return True


if __name__ == "__main__":
    print("___________________________________________Original___________________________________________")
    drawGrid(grid)
    print("____________________________________________SOLVED____________________________________________")
    solve(grid)
    drawGrid(grid)
