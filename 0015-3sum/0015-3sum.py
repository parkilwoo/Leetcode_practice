class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 서로 다른 3개의 원소의 합이 0이 되는 원소 찾기
        res = []
        nums.sort()
        n = len(nums)
        # 첫번째 원소 고정
        for i in range(n-2):
            one = nums[i]
            if one > 0:
                break
            # one값이 이전과 같으면 이미 확인을 한 상태이므로 중복을 위해 continue
            if i > 0 and one == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                two, three = nums[l], nums[r]
                sum_v = one+two+three
                if sum_v < 0:
                    l += 1
                elif sum_v > 0:
                    r -= 1
                else:
                    res.append([one,two,three])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return res
