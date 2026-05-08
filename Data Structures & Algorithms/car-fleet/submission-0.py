class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # catch up if target - position[behind] / speed[behind] <= target - position[ahead] / speed[ahead]

        posSpeed = []
        for i in range(len(position)):
            posSpeed.append([position[i], speed[i]])
        posSpeed.sort(reverse=True)

        stack = []

        for p, s in posSpeed:
            time = ((target - p) / s)
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)