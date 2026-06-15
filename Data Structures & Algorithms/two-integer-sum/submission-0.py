# Time complexity - O(n²)
# Space complexity - O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 1
        while True:
            if i == j:
                j += 1
                continue
            if nums[i] + nums[j] == target: return [i, j]
            else:
                if j != len(nums) - 1:
                    j += 1
                else:
                    i += 1
                    j = 0
