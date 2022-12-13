class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [hashmap.get(target - num), index]
            hashmap[num] = index