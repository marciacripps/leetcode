#leetcode Two Sum https://leetcode.com/problems/two-sum/description/ 
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


# def find_indices(arr, target):
#     # Loop through the array by index
#     for i in range(len(arr)):
#         for k in range(i + 1, len(arr)):  # Start from i+1 to avoid duplicates
#             if arr[i] + arr[k] == target:
#                 return [i, k]

# find_indices([1,2,3,4,5],9)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        
        # Loop through the list
        for i, num in enumerate(nums):
            # Calculate the complement (what we need to reach the target)
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_to_index:
                # If it exists, return the pair of indices
                return [num_to_index[complement], i]
            
            # Otherwise, store the number with its index in the dictionary
            num_to_index[num] = i
