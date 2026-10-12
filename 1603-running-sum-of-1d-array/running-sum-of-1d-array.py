class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.sum=[]
        total=0
        for i in nums:
            total+=i
            self.sum.append(total)
        return self.sum    