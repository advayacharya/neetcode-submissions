class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in ind:
                return [ind[diff],i]
            ind[n]=i
        