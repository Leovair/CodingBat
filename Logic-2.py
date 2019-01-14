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

def fix_teen(n):
    # if 13 <= n <= 14 or 17 <= n <= 19:
    if n in [13, 14, 17, 18, 19]:
        return 0
    return n

def no_teen_sum(a, b, c):
    # Given 3 int values, a b c, return their sum. However, if any of the values
    # is a teen -- in the range 13..19 inclusive -- then that value counts as 0,
    # except 15 and 16 do not count as a teens. Write a separate helper "def
    # fix_teen(n):"that takes in an int value and returns that value fixed for the
    # teen rule. In this way, you avoid repeating the teen code 3 times (i.e.
    # "decomposition"). Define the helper below and at the same indent level as
    # the main no_teen_sum().
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


