class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        while True:
            result += matrix.pop(0)
            if not matrix:
                break
            i = 0
            while i in range(len(matrix)):
                result.append(matrix[i].pop(-1))
                if len(matrix[i]) == 0:
                    matrix.pop(i)
                    i -= 1
                i += 1
            if not matrix:
                break
            result += matrix.pop(-1)[::-1]
            if not matrix:
                break
            i = -1
            while i >= -len(matrix):
                result.append(matrix[i].pop(0))
                if len(matrix[i]) == 0:
                    matrix.pop(i)
                    i += 1
                i -= 1
            if not matrix:
                break
        return result