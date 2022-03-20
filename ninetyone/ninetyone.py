#!/usr/bin/env python3

from sys import stdin

from utils import sumOfDigits

def ninetyone(input):
    n = int(input)
    return n+1 if n%91==0 else n//91*91+91-n%91 if sumOfDigits(n%91)>=10 or n%91%10==0 else n

if __name__ == "__main__":
    userInput = stdin.read()
    print(ninetyone(userInput), end='')
