from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         freq = {}
        
#         # Count characters from s
#         for ch in s:
#             if ch in freq:
#                 freq[ch] += 1
#             else:
#                 freq[ch] = 1
        
#         # Subtract using t
#         for ch in t:
#             if ch not in freq:
#                 return False
#             freq[ch] -= 1
#             if freq[ch] < 0:
#                 return False
        
#         return True