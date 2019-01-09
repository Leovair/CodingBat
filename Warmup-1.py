def sleep_in(weekday, vacation):
    '''
    The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
    We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
    '''
    if not weekday or vacation:
        return True
    else:
        return False

def monkey_trouble(a_smile, b_smile):
  '''
  We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
  We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
  '''
  if a_smile and b_smile:
      return True
  elif not a_smile and not b_smile:
      return True
  else:
      return False


def sum_double(a, b):
  '''
  Given two int values, return their sum. Unless the two values are the same, then return double their sum.
  '''
  if a == b:
    return (a*2) + (b*2)
  else:
    return a+b

def diff21(n):
    '''
    Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
    '''
    cons_num_for_diff = 21
    if n > cons_num_for_diff:
        return (n - cons_num_for_diff) * 2
    else:
        return cons_num_for_diff - n


print(diff21(22))


def parrot_trouble(talking, hour):
    '''
    We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
    '''
    if talking and (20 < hour or hour < 7):
        return True
    else:
        return False


def makes10(a, b):
    '''
    Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10
    '''
    summ = a + b
    if summ == 10 or (a == 10 or b == 10):
        return True
    else:
        return False


print(makes10(10, 4))


def near_hundred(n):
    '''
    Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
    '''
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


print(near_hundred(290))


def pos_neg(a, b, negative):
    '''
    Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
    '''
    if negative:
        return (a < 0 and b < 0)
    else:
        return ((a < 0 and b > 0) or (a > 0 and b < 0))


def not_string(str):
    '''
    Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
    '''
    if len(str) >= 3 and str[:3] == "not":
        return print(str)
    else:
        return print('not ' + str)


print(not_string('lol'))


def missing_char(str, n):
    '''
    Given a non-empty string and an int n, return a new string where the char at index n has been removed.
    The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
    '''
    front = str[:n]
    back = str[n + 1:]
    return front + back


print(missing_char('Марат', 1))


def front_back(str):
    '''
    Given a string, return a new string where the first and last chars have been exchanged.
    '''
    if len(str) <= 1:
        return str

    start_str = str[len(str) - len(str)]
    end_str = str[len(str) - 1]
    middl_str = str[(len(str) - len(str)) + 1:(len(str) - len(str)) - 1]
    return end_str + middl_str + start_str


print(front_back('Zalupacree'))


def front3(str):
    '''
    Given a string, we'll say that the front is the first 3 chars of the string.
    If the string length is less than 3, the front is whatever is there.
    Return a new string which is 3 copies of the front.
    '''
    if len(str) < 3:
        return str * 3
    else:
        return str[:2] * 3


print(front3('htr'))
