from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # m = len(grid)
        # n = len(grid[0])

        # cnt = 0

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == '1':
        #             position_queue = deque([(i, j)])
        #             cnt += 1
        #             grid[i][j] = '0'
        #             while position_queue:
        #                 row, column = position_queue.popleft()
        #                 for dr, dc in [(-1,0), (1,0), (0,-1),(0,1)]:
        #                     next_row = row+dr
        #                     next_column = column+dc
        #                     if 0<=next_row<m and 0<=next_column<n and grid[next_row][next_column] == '1' :
        #                         position_queue.append((next_row, next_column))
        #                         grid[next_row][next_column] = '0'

        # return cnt

        row = len(grid)
        column = len(grid[0])
        cnt = 0

        def dfs(r, c):
            if grid[r][c] == '0':
                return None
            
            grid[r][c] = '0'
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                next_r, next_c = r+dr, c+dc
                if 0<=next_r<row and 0<=next_c<column and grid[next_r][next_c] == '1':
                    dfs(next_r, next_c)
        
        for r in range(row):
            for c in range(column):
                if grid[r][c] == '1':
                    cnt +=1
                    dfs(r,c)

        return cnt
                    