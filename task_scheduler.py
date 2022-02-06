class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        
        aHash = {}
    
        for task in tasks:
            if task not in aHash:
                aHash[task] = 0
            aHash[task] +=1

        counter = list(aHash.values())

        counter.sort(reverse=True)

        result = 0
        while len(counter) != 0:
            count = i = 0
            while count <= n:
                if 0 <= i < len(counter):
                    counter[i] -= 1
                    if counter[i] == 0:
                        counter.pop(i)
                        i -= 1
                    i += 1
                count += 1
                if len(counter) ==  0:
                    break
            result += count
            counter.sort(reverse=True)
            

        return result