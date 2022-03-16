#!/usr/bin/env python3

from sys import stdin
from math import floor

class UserInput:
    def __init__(self, nday, year):
        self.nday, self.year = int(nday), int(year)

def getNdayAndYear(str):
    return UserInput(*str.split(';'))

def yearprogress(input):
    userInput = getNdayAndYear(input)
    isLeapYear = userInput.year % 4 == 0
    nbOfDaysInYear = 365 + 1 * int(isLeapYear)
    percentage = floor(userInput.nday / nbOfDaysInYear * 100)
    return f'{percentage}%'

if __name__ == "__main__":
    userInput = stdin.read()
    print(yearprogress(userInput), end='')
