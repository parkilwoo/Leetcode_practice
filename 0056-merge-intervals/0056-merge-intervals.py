class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        interval이 겹쳐지는 범위를 찾아서 merge 하고 모든 interval 리턴

        Merge -> 두 배열이 겹쳐지는 범위가 있으면 두 배열의 최소값~최대값이 merge
        """
        
        # 1. 시작점 기준으로 정렬
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        
        for interval in intervals[1:]:
            # result의 최근 배열과 merge 가능한지 비교
            previous = result[-1]
            if interval[0] <= previous[1]:
                merge = [previous[0], max(interval[1], previous[1])]
                result[-1] = merge
            else:
                result.append(interval)

        return result
            