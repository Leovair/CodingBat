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

def big_diff(nums):
  """
  Given an array length 1 or more of ints, return the difference between the
  largest and smallest values in the array. Note: the built-in min(v1, v2) and
  max(v1, v2) functions return the smaller or larger of two values.
  """
  # maxx = nums[0]
  # minn = nums[0]
  # for i in range(len(nums)):
  #     if nums[i] > maxx:
  #         maxx = nums[i]
  # if nums[i] < minn:
  #     minn = nums[i]
  # return maxx - minn

  return max(nums) - min(nums)

def centered_average(nums):
  """
  Return the "centered" average of an array of ints, which we'll say is the
  mean average of the values, except not counting the largest and smallest
  values in the array. Use int division to produce the final average. You may
  assume that the array is length 3 or more.
  """
  sum = 0
  centered = nums
  centered.remove(max(nums))
  centered.remove(min(nums))
  for element in centered:
    sum += element
  return sum / len(centered)

def sum13(nums):
  """
  Return the sum of the numbers in the array, returning 0 for an empty array.
  Except the number 13 is very unlucky, so it does not count and numbers that
  come immediately after a 13 also do not count.
  """
  if len(nums) == 0:
      return 0

  for i in range(0, len(nums)):
      if nums[i] == 13:
          nums[i] = 0
          if i + 1 < len(nums):
              nums[i + 1] = 0
  return sum(nums)

def sum67(nums):
  """
  Return the sum of the numbers in the array, except ignore sections of numbers
  starting with a 6 and extending to the next 7 (every 6 will be followed by at
  least one 7). Return 0 for no numbers.
  """
  for i in range(0, len(nums)):
    if nums[i] == 6:
      nums[i] = 0
      for j in range(i+1, len(nums)):
        temp = nums[j]
        nums[j] = 0
        if temp == 7:
          i = j + 1
          break
  return sum(nums)

def has22(nums):
  """
  Given an array of ints, return True if the array contains
  a 2 next to a 2 somewhere. Hello!
  """
  for i,v in enumerate(nums[:-1]):
    if v == 2 and nums[i+1] == 2:
      return True
  return False