class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        1. 모든 row는 반복되지 않고 1-9를 포함해야 한다
        2. 모든 column은 반복되지 않고 1-9를 포함해야 한다
        3. 3*3 박스는 반복되지 않고 1-9를 포함해야 한다
        """
        row_set_list = [set() for _ in range(9)]
        column_set_list = [set() for _ in range(9)]
        box_set_list = [set() for _ in range(9)]
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v == '.':
                    continue
                # row 검사
                if v in row_set_list[i]:
                    return False
                row_set_list[i].add(v)
                # column 검사
                if v in column_set_list[j]:
                    return False
                column_set_list[j].add(v)
                # box 검사
                # [(2,2), (5,2), (8,2),
                #  (2,5), (5,5), (8,5)
                #  (2,8), (5,8), (8,8)]
                area_idx = j//3 + i//3*3
                if v in box_set_list[area_idx]:
                    return False
                box_set_list[area_idx].add(v)

        return True