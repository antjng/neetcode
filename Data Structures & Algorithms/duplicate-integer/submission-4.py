class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # solution 2: using sets. O(n)
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False

        # solution 1: using lists. O(n^2)
        # xs = []
        # for n in nums:
        #     if n in xs:
        #         return True
        #     xs.append(n)
        # return False
            