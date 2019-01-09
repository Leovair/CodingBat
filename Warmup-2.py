def string_times(str, n):
    '''
    Given a string and a non-negative int n, return a larger string that is n copies of the original string.
    :param str:
    :param n:
    :return:
    '''
    if len(str) < 0:
        return str
    elif n >= 0:
        not_minus = abs(n)
        return str * not_minus


print(string_times('lo', 0))


def front_times(str, n):
    '''
    Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
    :param str:
    :param n:
    :return:
    '''
    front_len = 3
    if len(str) < front_len:
        front_len = len(str)

    front = str[:front_len]
    result = ''
    for i in range(n):
        result = result + front
    return result

print(front_times('chubbaka', 3))


def string_bits(str):
    '''
    Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
    :param str:
    :return:
    '''
    result = ''
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result


print(string_bits('Heeololeo'))


def string_splosion(str):
    '''
    Given a non-empty string like "Code" return a string like "CCoCodCode".
    :param str:
    :return:
    '''
    result = ''
    for i in range(len(str)):
        result = result + str[:i]

    return result + str


print(string_splosion('Code'))


def last2(str):
    '''
    Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
    :param str:
    :return:
    '''
    # cтрока слишком коротка
    if len(str) < 2:
        return 0

    last = str[len(str) - 2:]
    count = 0

    for i in range(len(str) - 2):
        sub = str[i:i + 2]
        if sub == last:
            count = count + 1
    return count


last2('xaxxaxaxx')


def array_count9(nums):
    '''
    Given an array of ints, return the number of 9's in the array.
    :param nums:
    :return:
    '''
    count = 0
    for i in nums:
        if i == 9:
            count = count + 1
    return count


print(array_count9([1, 9, 9, 3, 9]))


def array_front9(nums):
    '''
    Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
    :param nums:
    :return:
    '''
    count = len(nums)
    if count > 4:
        count = 4

    for i in range(count):
        if nums[i] == 9:
            return True
    return False


print(array_front9([1, 2, 9, 3, 4]))


def array123(nums):
    '''
    Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
    :param nums:
    :return:
    '''
    desir = [1, 2, 3]
    if str(desir)[1:-1] in str(nums):
        return True
    return False


def string_match(a, b):
    '''
    Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
    :param a:
    :param b:
    :return:
    '''
    shorter = min(len(a), len(b))
    count = 0

    for i in range(shorter - 1):
        a_sub = a[i: i + 2]
        b_sub = b[i: i + 2]
        if a_sub == b_sub:
            count = count + 1
    return count


print(string_match('xxcaazz', 'xxbaaz'))
