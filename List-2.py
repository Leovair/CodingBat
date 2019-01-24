def count_evens(nums):
    '''
    Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
    :param nums:
    :return:
    '''
    count = 0
    for n in nums:
       if n % 2 == 0:
           count = count + 1
    return count



print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))