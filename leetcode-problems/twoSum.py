# similar to insertion sort, performs in O(n^2)
class Solution(object):
    def twoSum(nums, target):
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0:
                if nums[i] + nums[j] == target:
                    return [j, i]
                j = j - 1
        return []


print(Solution.twoSum([3,7,11,18,1,2,20,25], 43))
print(Solution.twoSum([2,7,11,15], 9))