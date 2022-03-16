#!/usr/bin/env python3

from sys import stdin
from math import floor

from utils import parseArgs

import today

def yearProgress(nday=today.nday(), year=today.year()):
    isLeapYear = year % 4 == 0
    nbOfDaysInYear = 365 + 1 * int(isLeapYear)
    percentage = floor(nday / nbOfDaysInYear * 100)
    return f'{percentage}%'

def yearProgressFromStr(str=''):
    if not str:
        yearProgress()
    args = parseArgs(str)
    return yearProgress(*[int(a) for a in args])

if __name__ == "__main__":
    userInput = stdin.read()
    res = yearProgressFromStr(userInput)
    print(res, end='')
