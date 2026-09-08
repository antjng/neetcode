class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        xs = []
        for n in nums:
            if n in xs:
                return True
            xs.append(n)
        return False
            