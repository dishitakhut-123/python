def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def main():
    nums1 = [1, 3, 5, 6]
    target1 = 5
    print(searchInsert(nums1, target1))
    nums2 = [1, 3, 5, 6]
    target2 = 2
    print(searchInsert(nums2, target2))
    nums3 = [1, 3, 5, 6]
    target3 = 7
    print(searchInsert(nums3, target3))


main()
