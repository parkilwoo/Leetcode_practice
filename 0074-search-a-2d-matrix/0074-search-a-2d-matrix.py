class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        r_left = 0
        r_right = row - 1
    
        while r_left <= r_right:
            r_middle = (r_left + r_right) // 2
            if target < matrix[r_middle][0]:
                r_right = r_middle - 1
            elif target > matrix[r_middle][-1]:
                r_left = r_middle + 1
            else:
                break
        
        if not r_right >= r_left:
            return False

        c_matrix = matrix[r_middle]
        c_left = 0
        c_right = col - 1

        while c_left <= c_right:
            c_middle = (c_left + c_right) // 2
            c_middle_value = c_matrix[c_middle]
            if target > c_middle_value:
                c_left = c_middle + 1
            elif target < c_middle_value:
                c_right = c_middle - 1
            else:
                return True
        return False