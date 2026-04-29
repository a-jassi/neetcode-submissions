class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        longest_sequence = 0

        for num in nums:
            seq_len = 1
            if (num - 1) not in elements:
                curr = num
                while (curr + 1) in elements:
                    seq_len += 1
                    curr += 1
            longest_sequence = max(longest_sequence, seq_len)
        
        return longest_sequence
