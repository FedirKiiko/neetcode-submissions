class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 1
        count2 = 1
        unique = set(nums)
        for number in unique:
            count2 = 1
            if number - 1 in unique:
                continue
            else:
                save = number
                while save + 1 in unique:
                    count2 += 1
                    save += 1
            if count2 > count:
                count = count2
            

        return count
            