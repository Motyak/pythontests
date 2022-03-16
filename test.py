#!/usr/bin/env python3

from re import match
from os import listdir
from sys import stderr

from yearprogress import yearProgressFromStr
FUNCTION_TO_TEST = yearProgressFromStr

TESTS_PATH = './tests/'

def test():
    test_files = listdir(TESTS_PATH)

    if not test_files:
        return

    tests = []
    for fname in test_files:
        m = match(r'(.*)_out\.txt', fname)
        if m:
            tests.append(m.group(1))

    if not tests:
        return
        
    for t in tests:
        input = open(TESTS_PATH + t + '.txt', encoding='utf8').read()
        expecting = open(TESTS_PATH + t + '_out.txt', encoding='utf8').read()
        output = FUNCTION_TO_TEST(input)

        if output != expecting:
            print(
                f"Test '{t}' is failing:", 
                "\n-Expected: ", r"'''", f"{expecting}", r"'''", 
                "\n-Had: ", r"'''", f"{output}", r"'''",
                file=stderr, sep=''
            )
            exit(1)

test()
