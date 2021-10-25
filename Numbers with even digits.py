class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ansCount=0
        count=0
        for i in nums:
            count=0
            while i!=0:
                i//=10
                count+=1
                print(i)
            if count%2==0:
                ansCount+=1
        return ansCount