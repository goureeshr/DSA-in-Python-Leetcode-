''' 643. Maximum Average Subarray I


You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000 '''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]
        
        max_avg = curr_sum/k

        for i in range(k,len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i-k]

            avg = curr_sum/k

            max_avg = max(max_avg,avg)
        return max_avg
