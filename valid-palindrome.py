#https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        flag = True
        charSet = { i for i in range(ord('a'),ord('z')+1)}
        tempSet = { i for i in range(ord('0'),ord('9')+1)}
        charSet = charSet.union(tempSet)
        s = s.lower()
        testString = ''
        
        for code in str.encode(s):
            if code in charSet:
                testString = "".join([testString,chr(code)])
                
        length = len(testString)
        if length == 1:
            return flag
        
        for i in range(0,length//2):
            if testString[i] != testString[length-i-1]:
                flag = False
                
        return flag
