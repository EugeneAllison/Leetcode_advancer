from typing import Optional, List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        window = set()

        for R in range(len(nums)):
            if nums[R] in window:
                return True
            else:
                window.add(nums[R])
            if R - L >= k:  # 直接按照题干的意思写了(不是)，这样写不好，不直观
                window.remove(nums[L])
                L += 1

        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        window = set()

        for R in range(len(nums)):
            if R - L > k:  # 还是先判断更加直观，随时保证不超范围
                window.remove(nums[L]) 
                # 注意，这是一个set，所以 remove() 是一个 O(1) 的操作，而 list.remove() 是一个 O(n) 的操作
                L += 1
            if nums[R] in window:
                return True
            else:
                window.add(nums[R])

        return False
