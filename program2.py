def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return [seen[needed], i]
        seen[num] = i


def main():
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(twoSum(nums1, target1))
    nums2 = [3, 2, 4]
    target2 = 6
    print(twoSum(nums2, target2))
    nums3 = [3, 3]
    target3 = 6
    print(twoSum(nums3, target3))


main()
