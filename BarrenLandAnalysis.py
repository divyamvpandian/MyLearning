import time
from collections import deque
from pylab import *

"""
You have a farm of 400m by 600m where coordinates of the field are from (0, 0) to (399, 599).
A portion of the farm is barren, and all the barren land is in the form of rectangles. Due to these rectangles of barren land, 
the remaining area of fertile land is in no particular shape. An area of fertile land is defined as the largest area of land that is not covered by any of the rectangles of barren land. Read input from STDIN. Print output to STDOUT
Input
You are given a set of rectangles that contain the barren land. These rectangles are defined in a string, which consists of four integers separated by single spaces, with no additional spaces in the string. The first two integers are the coordinates of the bottom left corner in the given rectangle, and the last two integers are the coordinates of the top right corner.
Output
Output all the fertile land area in square meters, sorted from smallest area to greatest, separated by a space.
"""

# Defining a area of 400 by 600 as 2D array
M = 600
N = 400


def main():
    # Initialize the Array with all 1s
    arr = [[1 for i in range(M)] for j in range(N)]

    # Defining inputs. Coordinates of the barren land rectangles
    # stdin = ["48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"]
    stdin = ["0 292 399 307"]

    # for every rectangular coordinate mark the values inside that rectangle as 0
    arr = markbarrenland(arr, stdin)

    fertileareas = []

    # 1 - Recursion - Timing out for large Arrays- DFS
    # fertileAreas = getallfertilelandsDFSrec(arr)

    # # 2 - Iteration - - DFS -- 0.7852 seconds
    starttimeofDFS = time.perf_counter()
    fertileareas = getallfertilelandsDFSiter(arr)
    endtimeofDFS = time.perf_counter()

    print(f"Areas calculated using DFS in {endtimeofDFS - starttimeofDFS:0.4f} seconds")

    # 3 - Iteration - - BFS  -- 1.4021 seconds
    starttimeofBFS = time.perf_counter()
    fertileareas = getallfertilelandsBFSiter(arr)
    endtimeofBFS = time.perf_counter()

    print(f"Areas calculated using BFS in {endtimeofBFS - starttimeofBFS:0.4f} seconds")

    fertileareas.sort()
    stdout = " ".join([str(area) for area in fertileareas])
    print(stdout)


def markbarrenland(arr, stdin):
    for rectangle in stdin:
        coordinates = rectangle.split(" ")
        x1 = int(coordinates[0])
        y1 = int(coordinates[1])
        x2 = int(coordinates[2])
        y2 = int(coordinates[3])
        arr = fillbarrenland(arr, x1, y1, x2, y2)
    return arr


def getallfertilelandsDFSrec(land):
    fertileAreas = []
    for row in range(len(land)):
        for col in range(len(land[0])):
            if land[row][col] == 1:
                currarea = areaConnectedCell(land, row, col)
                fertileAreas.append(currarea)
    return fertileAreas


def areaConnectedCell(land, row, col):
    # Do a Depth first search Recursively

    ## Exit condition for Recursion
    if row < 0 or col < 0 or row >= len(land) or col >= len(land[0]):
        return 0
    if land[row][col] == 0:
        return 0
    area = 1
    land[row][col] = 0  ## Use Barren land symbol for visited
    for r in range(row - 1, row + 2):  ## to loop from prev row to next row
        for c in range(col - 1, col + 2):  ## to loop from prev col to next col
            if r != -1 and c != -1 and r < len(land) and c < len(land[0]) and (r != row or c != col) and land[r][
                c] == 1:
                area += areaConnectedCell(land, r, c)
    return area


def printArr(arr):
    for row in arr:
        print(row)


def fillbarrenland(arr, x1, y1, x2, y2):
    # fill 1s from x1 to x2 and y1 to y2
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            arr[i][j] = 0
    return arr


def getallfertilelandsDFSiter(land):
    # stores if cell is processed or not
    visited = [[False for x in range(M)] for y in range(N)]  ## can use a set as well. slightly runtime is high
    ans = 0
    fertilelands = []
    for currRow, row in enumerate(land):
        for currCol, val in enumerate(row):
            if val and (currRow, currCol) and not visited[currRow][currCol]:
                currArea = 0
                # Add coordinates as tuple in the connectedCells stack
                connectedCells = [(currRow, currCol)]
                visited[currRow][currCol] = True
                while connectedCells:
                    r, c = connectedCells.pop()
                    currArea += 1
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if (0 <= nr < len(land) and 0 <= nc < len(land[0])
                                and land[nr][nc] and not visited[nr][nc]):
                            connectedCells.append((nr, nc))
                            visited[nr][nc] = True
                fertilelands.append(currArea)
    return fertilelands


def getallfertilelandsBFSiter(land):
    # stores if cell is processed or not
    visited = [[False for x in range(M)] for y in range(N)]
    area = 0
    fertileareas = []
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1 and not visited[i][j]:
                area = BFS(land, visited, i, j)
                fertileareas.append(area)
    return fertileareas


def BFS(land, visited, i, j):
    area = 0
    # create an empty queue and enqueue source node
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        area += 1
        r, c = q.popleft()
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if (0 <= nr < len(land) and 0 <= nc < len(land[0])
                    and land[nr][nc] == 1 and (nr, nc) and not visited[nr][nc]):
                q.append((nr, nc))
                visited[nr][nc] = True
    return area


if __name__ == "__main__":
    main()
