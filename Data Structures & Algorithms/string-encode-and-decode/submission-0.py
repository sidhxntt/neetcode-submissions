class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + '#' + s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # find the delimiter '#'
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])          # get length
            word = s[j+1 : j+1+length]   # extract word

            res.append(word)
            i = j + 1 + length           # move pointer forward

        return res
