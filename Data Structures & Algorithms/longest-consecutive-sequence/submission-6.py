class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        count = 1
        ordered = sorted(set(nums))
        count2 = 1
        for i in range(1, len(ordered)):
            if ordered[i] - ordered[i - 1] == 1 or ordered[i] - ordered[i - 1] == -1:
                count2 += 1
            else:
                count2 = 1
            if count2 > count:
                count = count2
            
        return count
        