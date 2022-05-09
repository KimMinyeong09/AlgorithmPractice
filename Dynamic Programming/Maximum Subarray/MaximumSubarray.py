class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_sum = [0 for i in range(len(nums))]
        sub_sum[0] = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            sub_sum[i] = max(nums[i], sub_sum[i-1]+nums[i])
            if max_sum < sub_sum[i]:
                max_sum = sub_sum[i]
        return max_sum