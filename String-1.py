def hello_name(name):
    """
    Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
    """
    return 'Hello ' + name + '!'


you_name = input('Введите ваше имя уважаемый: ')
print(hello_name(you_name))


def make_abba(a, b):
    """
    Given two strings, a and b, return the result of putting them together
    in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
    """
    return (a + b) + (b + a)


print(make_abba('Hi', 'Bye'))


def make_tags(tag, word):
    """
    The web is built with HTML strings like "<i>Yay</i>" which draws Yay as
    italic text. In this example, the "i" tag makes <i> and </i> which surround
    the word "Yay". Given tag and word strings, create the HTML string with tags
    around the word, e.g. "<i>Yay</i>".
    """
    return '<' + tag + '>' + word + '</' + tag + '>'


print(make_tags('b', 'Bye'))


def make_out_word(out, word):
    """
    Given an "out" string length 4, such as "<<>>", and a word, return a new
    string where the word is in the middle of the out string, e.g. "<<word>>".
    """
    if len(out) > 3:
        return out[:2] + word + out[2:]
    else:
        return False


print(make_out_word('<<>>', 'Yay'))


def extra_end(str):
    """
    Given a string, return a new string made of 3 copies of the last 2 chars
    of the original string. The string length will be at least 2.
    """
    if len(str) > 2:
        return str[len(str) - 2:] * 3
    else:
        return str * 3


print(extra_end('Hello'))


def first_two(str):
    """
    Given a string, return the string made of its first two chars, so the
    String "Hello" yields "He". If the string is shorter than length 2, return
    whatever there is, so "X" yields "X", and the empty string "" yields the
    empty string "".
    """
    if len(str) > 2:
        return str[:2]
    elif len(str) < 1:
        return str
    else:
        return str


print(first_two('Hello'))


def first_half(str):
    """
    Given a string of even length, return the first half. So the string "WooHoo"
    yields "Woo".
    """
    if len(str) < 1:
        return str
    else:
        return str[:len(str) / 2]


def without_end(str):
    """
    Given a string, return a version without the first and last char,
    so "Hello" yields "ell". The string length will be at least 2.
    """
    if len(str) > 3:
        minus_first_char = (len(str) - len(str)) + 1
        minus_last_char = len(str) - 1
        return str[minus_first_char: minus_last_char]
    else:
        return str


print(without_end('coding'))


def combo_string(a, b):
    """
    Given 2 strings, a and b, return a string of the form short+long+short,
    with the shorter string on the outside and the longer string on the inside.
    The strings will not be the same length, but they may be empty (length 0).
    """
    if len(a) > len(b):
        return b + a + b
    elif len(a) < len(b):
        return a + b + a


def non_start(a, b):
    """
    Given 2 strings, return their concatenation, except omit the first char
    of each. The strings will be at least length 1.
    """
    return a[1:] + b[1:]


print(non_start('Hello', 'There'))


def left2(str):
    """
    Given a string, return a "rotated left 2" version where the first 2 chars
    are moved to the end. The string length will be at least 2.
    """
    return str[2:] + str[:2]
