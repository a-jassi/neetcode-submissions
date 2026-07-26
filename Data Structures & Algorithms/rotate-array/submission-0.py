class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = [0] * len(nums)
        for i in range(len(nums)):
            shift = (i + (k % len(nums))) % len(nums)
            tmp[shift] = nums[i]
            
        for i in range(len(nums)):
            nums[i] = tmp[i]

