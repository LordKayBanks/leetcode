# 164. Maximum Gap
#
# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
#
# Try to solve it in linear time/space.
#
# Return 0 if the array contains less than 2 elements.
#
# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
#
# Credits:
# Special thanks to @porker2008 for adding this problem and creating all test cases.


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxgap = 0
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            maxgap = max(maxgap, nums[i + 1] - nums[i])
        return maxgap


if __name__ == '__main__':
    print Solution().maximumGap([3, 4, 9, 5, 1])
