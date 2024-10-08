class Solution:
    def backtrack(self, input, current, result):
        result.append(current[:])

        for i in range(len(input)):
            current.append(input[i])
            self.backtrack(input[i + 1:], current, result)
            current.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]: # type: ignore
        res = []
        self.backtrack(nums, [], res)
        return res
