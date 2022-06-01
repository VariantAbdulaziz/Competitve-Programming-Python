# source: https://leetcode.com/problems/word-ladder/submissions/

# strategy: bfs | hashmap
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        book = defaultdict(lambda: [])
        def build_adj(word):
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                book[key].append(word)
                
        def gen_keys(word):
            keys = []
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                keys.append(key)
            
            return keys
        
        def bfs():
            if beginWord == endWord:
                return 1
            q = [(beginWord, 1)]
            explored = set()
            while q:
                word, lvl = q.pop(0)
                
                for key in gen_keys(word):
                    for next_word in book[key]:
                        if next_word not in explored:
                            if next_word == endWord:
                                return lvl + 1
                            q.append((next_word, lvl+1))
                            explored.add(next_word)
                        
            return 0
        
        build_adj(beginWord)
        for word in wordList:
            build_adj(word)
        
        return bfs()