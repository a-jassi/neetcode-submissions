class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0

        l, r = 0, len(people) - 1

        while l <= r:
            total = people[l] + people[r]
            if total > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            
            res += 1
        return res
