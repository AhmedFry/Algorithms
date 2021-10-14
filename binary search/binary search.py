def search(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            print(left , pivot, right)
            
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
            
        else:
            pivot = None
        return pivot

yourList = []
target = None
print(search(yourList, target))