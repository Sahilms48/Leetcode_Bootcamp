class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        results =[1]*(len(nums))
        prefix=1
        for i in range (len(nums)):
            results[i]=prefix
            prefix=prefix*nums[i]

        suffix=1
        for i in range (len(nums)-1, -1, -1):
            results[i]=results[i]*suffix
            suffix=suffix*nums[i]

        return results
        


        
