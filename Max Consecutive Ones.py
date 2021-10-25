class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        count=0
        for i in nums:
            if i:
                count+=1
                if count>ans:
                    ans=count
            else:
                count=0
        return ans