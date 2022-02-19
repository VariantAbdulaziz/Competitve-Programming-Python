from math import lcm
from math import lcm
class Solution:
    def carFleet(self, target, position, speed):
        
        def canCatchUp(car1, car2):
            if car1[1] <= car2[1]:
                return False
            if (target - car1[0]) / car1[1] <= (target - car2[0])/ car2[1]:
                return True
            return False

        cars = list(zip(position, speed))
        cars.sort(key=lambda x:x[0])

        stack = []
        for car in cars:
            while stack and canCatchUp(stack[-1], car):
                stack.pop()

            stack.append(car)
        return len(stack)