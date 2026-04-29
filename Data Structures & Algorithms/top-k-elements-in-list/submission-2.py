class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        freq = {}
        count = 1

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            freq[nums[i]] = count

        # sort by frequency properly
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        res = []
        for num, _ in sorted_items:
            res.append(num)

        return res[:k]