class NumArray(object):

    def __init__(self, nums):
        self.sum=[]
        total=0
        for num in nums:
            total+=num
            self.sum.append(total)



    def sumRange(self,left, right):
       if left==0:
        return self.sum[right]

       else:
            return self.sum[right]-self.sum[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)