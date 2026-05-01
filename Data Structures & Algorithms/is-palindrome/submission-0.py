class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(ch.lower() for ch in s if ch.isalnum())
        front = 0
        back = len(word) - 1

        while front < back:
            if word[front] != word[back]:
                return False   
            
            front += 1
            back -= 1
        
        return True