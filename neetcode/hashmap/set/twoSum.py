class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type: ignore
        hashmap = {} # value : index

        for index, value in enumerate(nums):
            diff = target - value
            if diff in hashmap:
                return [hashmap[diff], index]
            
            hashmap[value] = index

        return