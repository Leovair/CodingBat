def make_bricks(small, big, goal):
    '''
    We want to make a row of bricks that is goal inches long.
    We have a number of small bricks (1 inch each) and big bricks (5 inches each).
    Return True if it is possible to make the goal by choosing from the given bricks.
    This is a little harder than it looks and can be done without any loops.
    :param small:
    :param big:
    :param goal:
    :return:
    '''
    if goal >= 5 * big:
        remainder = goal - (5 * big)
    else:
        remainder = goal % 5

    return small >= remainder

def lone_sum(a, b, c):
    '''
    Given 3 int values, a b c, return their sum. However,
    if one of the values is the same as another of the values, it does not count towards the sum.
    :param a:
    :param b:
    :param c:
    :return:
    '''
    summ = 0

    if a != c and a != b:
        summ = summ + a
    if b != a and b != c:
        summ = summ + b
    if c != a and c != b:
        summ = summ + c

    return summ

def lucky_sum(a, b, c):
    '''
    Given 3 int values, a b c, return their sum. However,
    if one of the values is 13 then it does not count
    towards the sum and values to its right do not count. So for example,
    if b is 13, then both b and c do not count.
    :param a:
    :param b:
    :param c:
    :return:
    '''
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a+b
    else:
      return a+b+c



def no_teen_sum(a, b, c):
    # Given 3 int values, a b c, return their sum. However, if any of the values
    # is a teen -- in the range 13..19 inclusive -- then that value counts as 0,
    # except 15 and 16 do not count as a teens. Write a separate helper "def
    # fix_teen(n):"that takes in an int value and returns that value fixed for the
    # teen rule. In this way, you avoid repeating the teen code 3 times (i.e.
    # "decomposition"). Define the helper below and at the same indent level as
    # the main no_teen_sum().
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    # if 13 <= n <= 14 or 17 <= n <= 19:
    if n in [13, 14, 17, 18, 19]:
        return 0
    return n

def round_sum(a, b, c):
    '''
    For this problem, we'll round an int value up to the next multiple of 10 if its rightmost
    digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple
    of 10 if its rightmost digit is less than 5, so 12 rounds down to 10.
    Given 3 ints, a b c, return the sum of their rounded values.
    To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times.
    Write the helper entirely below and at the same indent level as round_sum().
    :param a:
    :param b:
    :param c:
    :return:
    '''
    return round10(a) + round10(b) + round10(c)

def round10(num):
    if num % 10 >= 5:
        return num + 10 - (num % 10)
    return num - (num % 10)

print(round_sum(16, 17, 18))
print(round_sum(12, 13, 14))
print(round_sum(25, 32, 102))
print(round_sum(16, 17, 18))


def close_far(a, b, c):
    """
    Given three ints, a b c, return True if one of b or c is "close"
    (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.
    Note: abs(num) computes the absolute value of a number.
    close_far(1, 2, 10) → True
    close_far(1, 2, 3) → False
    close_far(4, 1, 3) → True
    """
    a_b_diff = abs(a - b)
    a_c_diff = abs(a-c)
    b_c_diff = abs(b-c)

    return a_b_diff <= 1 and a_c_diff >= 2 and b_c_diff >= 2 or a_c_diff <= 1 and a_b_diff >= 2 and b_c_diff >= 2

def make_chocolate(small, big, goal):
    '''
    We want make a package of goal kilos of chocolate.
    We have small bars (1 kilo each) and big bars (5 kilos each).
    Return the number of small bars to use, assuming we always use
    big bars before small bars. Return -1 if it can't be done.
    :param small:
    :param big:
    :param goal:
    :return:
    '''
    if goal >= 5 * big:
        remainder = goal - 5 * big
    else:
        remainder = goal % 5

    if remainder <= small:
        return remainder
    return -1