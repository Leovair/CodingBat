def cigar_party(cigars, is_weekend):
    '''
    When squirrels get together for a party, they like to have cigars.
    A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
    Unless it is the weekend, in which case there is no upper bound on the number of cigars.
     Return True if the party with the given values is successful, or False otherwise.
    :param cigars:
    :param is_weekend:
    :return:
    '''
    if 40 <= cigars <= 60 or (cigars >= 40 and is_weekend):
        return True

print(cigar_party(30, False))


def date_fashion(you, date):
    '''
    You and your date are trying to get a table at a restaurant.
    The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date"
    is the stylishness of your date's clothes. The result getting the table is encoded as an
    int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes).
    With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
    :param you:
    :param date:
    :return:
    '''
    if you <= 2 or date <=2:
        return 0

    if you >=8 or date >= 8:
        return 2
    else:
        return 1

def squirrel_play(temp, is_summer):
    '''
    The squirrels in Palo Alto spend most of the day playing.
    In particular, they play if the temperature is between 60 and 90 (inclusive).
    Unless it is summer, then the upper limit is 100 instead of 90.
    Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
    :param temp:
    :param is_summer:
    :return:
    '''
    if is_summer:
        return temp >= 60 or temp <= 100
    return temp >= 60 or temp <= 90


def caught_speeding(speed, is_birthday):
    '''
    You are driving a little too fast, and a police officer stops you.
    Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket.
    If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1.
    If speed is 81 or more, the result is 2.
    Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
    :param speed:
    :param is_birthday:
    :return:
    '''
