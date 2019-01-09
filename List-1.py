def first_last6(nums):
    '''
    Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
    :param nums:
    :return:
    '''
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else:
        return False


print(first_last6([6, 1, 2, 3]))


def same_first_last(nums):
    '''
    Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
    :param nums:
    :return:
    '''
    if len(nums) >= 1 and nums[0] == nums[-1]:
        return True
    else:
        return False


print(same_first_last([1, 2, 3, 1]))


def make_pi():
    '''
    Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
    :return:
    '''
    return [3, 1, 4]


def common_end(a, b):
    '''
    Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element.
    Both arrays will be length 1 or more.
    :param a:
    :param b:
    :return:
    '''
    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    else:
        return False


common_end([1, 2, 3], [7, 3])


def sum3(nums):
    '''
    Given an array of ints length 3, return the sum of all the elements.
    :param nums:
    :return:
    '''
    if len(nums) >= 3:
        return nums[0] + nums[1] + nums[2]
    else:
        return False


sum3([1, 2, 3])


def rotate_left3(nums):
    '''
    Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
    :param nums:
    :return:
    '''
    if len(nums) >= 3:
        return nums[1:] + nums[0:1]
    else:
        return False


rotate_left3([5, 11, 9])


def reverse3(nums):
    '''
    Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
    :param nums:
    :return:
    '''
    if len(nums) >= 3:
        return nums[::-1]
    else:
        return False


print(reverse3([5, 11, 9]))


def max_end3(nums):
    '''
    Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value.
    Return the changed array.
    :param nums:
    :return:
    '''
    if nums[0] > nums[2]:
        return [nums[0], nums[0], nums[0]]
    return [nums[2], nums[2], nums[2]]


max_end3([11, 5, 9])


def sum2(nums):
    '''
    Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
    :param nums:
    :return:
    '''
    none = 0
    if len(nums) > 1:
        return nums[0] + nums[1]
    elif len(nums) == 1:
        return nums[0]
    return none
