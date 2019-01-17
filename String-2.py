def double_char(str):
    '''
    Given a string, return a string where for every char in the original, there are two chars.
    :param str:
    :return:
    '''
    result = ''
    for letter in str:
        result = result + (letter*2)
    return result

print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))


def count_hi(str):
    '''
    Return the number of times that the string "hi" appears anywhere in the given string.
    :param str:
    :return:
    '''
    count = 0
    for letter in range(len(str)):
        if str[letter:letter+2] == 'hi':
            count = count + 1

    return count

print(count_hi('abc hi ho'))

def cat_dog(str):
    '''
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    :param str:
    :return:
    '''
    count_ledog = 0
    count_lecat = 0
    for letter in range(len(str)):
        if str[letter:letter+3] == 'cat':
            count_lecat = count_lecat + 1
        elif str[letter:letter+3] == 'dog':
            count_ledog = count_ledog + 1

    return count_ledog == count_lecat
print(cat_dog('catdog'))
print(cat_dog('catcat'))

def count_code(str):
    '''
    Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
    :param str:
    :return:
    '''
    count = 0
    for letter in range(len(str)-3):
        if str[letter:letter+2] == 'co' and str[letter+3] == 'e':
            count = count + 1
    return count

print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))

def end_other(a, b):
  '''
  Given two strings, return True if either of the strings appears at
  the very end of the other string, ignoring upper/lower case differences
  (in other words, the computation should not be "case sensitive").
  Note: s.lower() returns the lowercase version of a string.
  :param a:
  :param b:
  :return:
  '''
  a = a.lower()
  b = b.lower()
  #return (b.endswith(a) or a.endswith(b))
  return a[-(len(b)):] == b or a == b[-(len(a)):]