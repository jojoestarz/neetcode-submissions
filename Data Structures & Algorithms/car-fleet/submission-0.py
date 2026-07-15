class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = []
        stack = []
        for p,s in zip(position,speed):
            paired.append([p,s])
        for i in sorted(paired)[::-1]:
            stack.append((target-i[0])/i[1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack )