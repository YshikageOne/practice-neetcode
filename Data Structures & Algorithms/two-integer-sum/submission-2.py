class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevNum = {} # previous number : index

        for ind, currentNum in enumerate(nums):
            dif = target - currentNum

            if dif in prevNum:
                return [prevNum[dif], ind]

            prevNum[currentNum] = ind
        return