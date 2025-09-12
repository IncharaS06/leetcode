class Solution:
    def reverseDegree(self, s: str) -> int:
        output=0
        for index,i in enumerate(s):
            output+=(123-ord(i))*(index+1)
        return output
