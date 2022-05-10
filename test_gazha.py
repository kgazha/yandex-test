def find_difference(nums1, nums2):
    s1, s2 = set(nums1), set(nums2)
    return list(s1 - s2)


def remove_zeros(nums):
    idx = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[idx] = nums[i]
            idx += 1
    return nums[:idx]
