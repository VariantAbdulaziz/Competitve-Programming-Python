# https://leetcode.com/problems/boats-to-save-people/submissions/

class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        
        answer = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[right] > limit:
                right -= 1
            elif people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -=1
            answer += 1
            
        return answer