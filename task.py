class Solution:
    def reverseDegree(self, s: str) -> int:
        output=0
        for index,i in enumerate(s):
            output+=(123-ord(i))*(index+1)
        return output


class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        seen = False

        for i in s:
            if i == '*' and seen == False:
                count += 1
            if i == '|':
                seen = not seen 
        return count
