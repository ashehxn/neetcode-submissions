# Time complexity - O(log m + log n)
# Space complexity: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target > matrix[-1][-1] or target < matrix[0][0]:
            return False
        
        low = 0
        high = len(matrix) - 1
        while low <= high:
            mid = low + (high - low) // 2
            valueRow = matrix[mid]

            if valueRow[0] <= target and target <= valueRow[-1]:
                break;
            elif valueRow[0] > target:
                high = mid - 1
            else:
                low = mid + 1

        innerLow = 0
        innerHigh = len(valueRow) - 1    
        while innerLow <= innerHigh:
            innerMid = innerLow + (innerHigh - innerLow) // 2
            guess = valueRow[innerMid]

            if guess == target:
                return True
            elif guess > target:
                innerHigh = innerMid - 1
            else:
                innerLow = innerMid + 1
        return False

