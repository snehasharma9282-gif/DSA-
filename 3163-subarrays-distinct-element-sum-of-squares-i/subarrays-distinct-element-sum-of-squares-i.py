class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        total = 0
        n = len(nums)

        for i in range(n):
            unique = set()

            for j in range(i, n):
                unique.add(nums[j])
                count = len(unique)
                total += count * count

        return total
