#!/usr/bin/env python

"""
Palindrome number test and generator
"""

__all__ = ['ispalinum', 'palinum', 'palinumlist', 'paligraph']


def ispalinum(n):

    """
    Checks passed number if it is a palindrome.
    """

    m = n
    a = 0

    while (m != 0):
        a = m % 10 + a * 10
        m = m / 10

    if (n == a):
        return True
    else:
        return False


def palinum(numlen):

    """
    Returns a palindrome integer of a specified length.
    """

    from random import random
    
    n = random()
    n = float('0.' + str(n).strip('0.'))
    n = int(n * (10 ** numlen))
    s = list(str(n))
    l = len(s)
    if not l % 2.0:
        r = s[:l/2]
        s = r + list(reversed(r))
    else:
        r = s[:int((l/2.0)-0.5)]
        s = r + list(s[int((l/2.0)-0.5)]) + list(reversed(r)) 
    return int(''.join(s))


def palinumlist(listlen, numlen):

    return list(palinum(numlen) for n in range(listlen))


def paligraph(start, end):
        
    s = start
    m = end / 2 + 1
    e = end + 1
    r1 = range(s, m, 1)
    r2 = range(m, e, 1)

    for n1 in r1:
        n2 = r2.pop()
        rn1 = palinum(n1)
        rn2 = palinum(n2)
        sleft = '0' if n1 < 10 else ''
        sright = '0' if n2 < 10 else ''
        print '{}{} {} {} {}{}'.format(sleft, n1,
        rn1, rn2,
        n2, sright)

