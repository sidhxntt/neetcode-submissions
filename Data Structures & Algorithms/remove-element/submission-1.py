
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # position to place next valid element

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k