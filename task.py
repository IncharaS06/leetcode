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


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):

            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            
            digits[i] = 0

            if i == 0:
                return [1] + digits


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countL = 0
        countR = 0
        result = 0
        for i in s:
            if i == 'L':
                countL += 1
            else:
                countR += 1
            if countR == countL:
                result += 1
        return result      
