#!/usr/bin/env python3

import sys # stdin
import math # floor()

import utils # parseArgs()
import today # nday(), year()

def yearProgress(nday=today.nday(), year=today.year()):
    isLeapYear = year % 4 == 0
    nbOfDaysInYear = 365 + 1 * int(isLeapYear)
    percentage = math.floor(nday / nbOfDaysInYear * 100)
    return f'{percentage}%'

def yearProgressFromStr(str=''):
    if not str:
        yearProgress()
    args = utils.parseArgs(str)
    return yearProgress(*[int(a) for a in args])

if __name__ == "__main__":
    userInput = sys.stdin.read()
    res = yearProgressFromStr(userInput)
    print(res, end='')
