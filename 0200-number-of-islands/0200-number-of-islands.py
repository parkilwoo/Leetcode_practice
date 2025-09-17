from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    position_queue = deque([(i, j)])
                    cnt += 1
                    grid[i][j] = '0'
                    while position_queue:
                        row, column = position_queue.popleft()
                        for dr, dc in [(-1,0), (1,0), (0,-1),(0,1)]:
                            next_row = row+dr
                            next_column = column+dc
                            if 0<=next_row<m and 0<=next_column<n and grid[next_row][next_column] == '1' :
                                position_queue.append((next_row, next_column))
                                grid[next_row][next_column] = '0'

        return cnt