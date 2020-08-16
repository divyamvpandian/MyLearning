import time
from collections import deque
from pylab import *


class BarrenLand:
    def __init__(self, l, w):
        if l<0 or w<0:
            raise TypeError("length and width has to be non negative number")
        self.length = l
        self.width = w
        self.land = [[1 for i in range(l)] for j in range(w)]
        self.size=l*w

    def fillBarrenLand(self, x1, y1, x2, y2):
        # fill 1s from x1 to x2 and y1 to y2
        if any([x1 < 0, x2 < 0, y1 < 0, y2 < 0, x1 >= self.width, x2 >= self.width, y1 >= self.length,
                y2 >= self.length]):
            raise TypeError("Coordinates not within bounds")

        else:
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    self.land[i][j] = 0

    def getallfertilelandsarea(self):
        # stores if cell is processed or not
        visited = [[False for x in range(self.length)] for y in
                   range(self.width)]  ## can use a set as well. slightly runtime is high
        ans = 0
        fertilelands = []
        for currRow, row in enumerate(self.land):
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
                            if (0 <= nr < len(self.land) and 0 <= nc < len(self.land[0])
                                    and self.land[nr][nc] and not visited[nr][nc]):
                                connectedCells.append((nr, nc))
                                visited[nr][nc] = True
                    fertilelands.append(currArea)
        return fertilelands

    def getallfertilelandsBFSiter(self):
        # stores if cell is processed or not
        visited = [[False for x in range(self.length)] for y in range(self.width)]
        area = 0
        fertileareas = []
        for i in range(self.width):
            for j in range(self.length):
                if self.land[i][j] == 1 and not visited[i][j]:
                    area = self.BFS(visited, i, j)
                    fertileareas.append(area)
        return fertileareas

    def BFS(self, visited, i, j):
        area = 0
        # create an empty queue and enqueue source node
        q = deque()
        q.append((i, j))
        visited[i][j] = True
        while q:
            area += 1
            r, c = q.popleft()
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (0 <= nr < len(self.land) and 0 <= nc < len(self.land[0])
                        and self.land[nr][nc] == 1 and (nr, nc) and not visited[nr][nc]):
                    q.append((nr, nc))
                    visited[nr][nc] = True
        return area

    def printLand(self):
        for row in self.land:
            print(row)

    def getallfertilelandsDFSrec(self):
        fertileAreas = []
        for row in range(len(self.land)):
            for col in range(len(self.land[0])):
                if self.land[row][col] == 1:
                    currarea = self.areaConnectedCell(row, col)
                    fertileAreas.append(currarea)
        return fertileAreas

    def areaConnectedCell(self, row, col):
        # Do a Depth first search Recursively
        ## Exit condition for Recursion
        if row < 0 or col < 0 or row >= len(self.land) or col >= len(self.land[0]):
            return 0
        if self.land[row][col] == 0:
            return 0
        area = 1
        self.land[row][col] = 0  ## Use Barren land symbol for visited
        for r in range(row - 1, row + 2):  ## to loop from prev row to next row
            for c in range(col - 1, col + 2):  ## to loop from prev col to next col
                if r != -1 and c != -1 and r < len(self.land) and c < len(self.land[0]) and (r != row or c != col) and \
                        self.land[r][
                            c] == 1:
                    area += self.areaConnectedCell(self.land, r, c)
        return area


def main():
    d = BarrenLand(600, 400)
    # stdin = ["0 292 399 307"]
    stdin = ["48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"]
    for rectangle in stdin:
        coordinates = rectangle.split(" ")
        x1 = int(coordinates[0])
        y1 = int(coordinates[1])
        x2 = int(coordinates[2])
        y2 = int(coordinates[3])
        d.fillBarrenLand(x1, y1, x2, y2)

    fertileareas = []
    # 2 - Iteration - - DFS -- 0.7852 seconds
    starttimeofDFS = time.perf_counter()
    fertileareas = d.getallfertilelandsarea()
    endtimeofDFS = time.perf_counter()

    print(f"Areas calculated using DFS in {endtimeofDFS - starttimeofDFS:0.4f} seconds")
    fertileareas.sort()
    stdout = " ".join([str(area) for area in fertileareas])
    print(stdout)

    # 1 - Recursion - Timing out for large Arrays- DFS
    # fertileAreas = getallfertilelandsDFSrec(arr)

    # 3 - Iteration - - BFS  -- 1.4021 seconds
    starttimeofBFS = time.perf_counter()
    fertileareas = d.getallfertilelandsBFSiter()
    endtimeofBFS = time.perf_counter()
    print(f"Areas calculated using BFS in {endtimeofBFS - starttimeofBFS:0.4f} seconds")

    fertileareas.sort()
    stdout = " ".join([str(area) for area in fertileareas])
    print(stdout)


if __name__ == "__main__":
    main()
