class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_1 = len(nums1)
        len_2 = len(nums2)
        sum_len = len_1 + len_2
        if not sum_len:
            return 0
        
        target_index = (sum_len // 2) + 1
        is_middle = sum_len % 2

        i = 0
        j = 0
        
        merged_list = []
        while i < len_1 and j < len_2 and target_index > 0:
            if nums1[i] < nums2[j]:
                merged_list.append(nums1[i])
                i += 1
            else:
                merged_list.append(nums2[j])
                j += 1
            target_index -= 1

        if not target_index:
            return merged_list[-1] if is_middle else sum(merged_list[-2:]) / 2
        
        if len_1 == i:
            while target_index > 0:
                merged_list.append(nums2[j])
                target_index -= 1
                j += 1
        else:
            while target_index > 0:
                merged_list.append(nums1[i])
                target_index -= 1
                i += 1
        return merged_list[-1] if is_middle else sum(merged_list[-2:]) / 2