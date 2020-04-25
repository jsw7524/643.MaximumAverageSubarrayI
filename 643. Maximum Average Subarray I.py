class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxAVG = -10000
        tmp = 0.0
        for i in range(k):
            tmp+=nums[i]
        maxAVG=tmp
        for n in range(k,len(nums)):
            tmp = tmp +nums[n] - nums[n-k]
            if tmp  > maxAVG:
                maxAVG = tmp
        return maxAVG / k

sln=Solution()
assert 12.75000==sln.findMaxAverage([1,12,-5,-6,50,3],4)
assert 1.00000==sln.findMaxAverage([1],1)
assert 2.00000==sln.findMaxAverage([0,1,1,3,3],4)
assert 2.80000==sln.findMaxAverage([4,0,4,3,3],5)