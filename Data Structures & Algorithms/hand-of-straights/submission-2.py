class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for num in hand:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        hand.sort()

        for num in hand:
            if count[num] == 0:
                continue

            for i in range(num, num + groupSize):
                if i not in count or not count[i]:
                    return False
                count[i] -= 1
        
        return True