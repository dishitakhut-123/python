def twoSum(nums, target):
    seen = {}   # stores number : index

    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return [seen[needed], i]
        seen[num] = i


def main():
    # Example 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(twoSum(nums1, target1))   # [0, 1]

    # Example 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(twoSum(nums2, target2))   # [1, 2]

    # Example 3
    nums3 = [3, 3]
    target3 = 6
    print(twoSum(nums3, target3))   # [0, 1]


main()
