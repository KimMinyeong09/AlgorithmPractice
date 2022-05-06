class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        for i in range(len(nums)-1):
            if (nums[i] != nums[i+1]):
                nums[length] = nums[i]
                length += 1
        nums[length] = nums[len(nums)-1]
        return length + 1