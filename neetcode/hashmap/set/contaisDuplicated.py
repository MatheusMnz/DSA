class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: # type: ignore
        hashset = set()

        for element in nums:
            if element in hashset:
                return True
            hashset.add(element)
        return False