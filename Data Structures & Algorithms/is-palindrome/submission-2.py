class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz01234567890"
        result = ""
        for letter in s:
            if letter.lower() in alphabet:
                result += letter.lower()
        return result == result[::-1]
            