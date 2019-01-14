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