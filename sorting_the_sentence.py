# solution to https://leetcode.com/problems/sorting-the-sentence/submissions/

class Solution:
    def sortSentence(self, s: str) -> str:
        aDict = {}
        wordCount = 0
        temp = ""
        for elem in s:
            if elem != " ":
                temp += elem
            else:
                aDict[temp[-1]] = temp[:-1]
                temp = ""
                wordCount += 1
        
        # for the final word
        aDict[temp[-1]] = temp[:-1]
        wordCount +=1
        
        sentence = ""
        i = 1
        while i < wordCount:
            sentence += aDict[str(i)] + " "
            i += 1
        
        # not to have to add the space after the final word
        sentence += aDict[str(wordCount)]
        
        return sentence