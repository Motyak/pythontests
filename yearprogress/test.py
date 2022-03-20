#!/usr/bin/env python3

import re # match()
import os # listdir()
import sys # stderr

from yearprogress import yearProgressFromStr
FUNCTION_TO_TEST = yearProgressFromStr

TESTS_PATH = './examples/'

def test():
    test_files = os.listdir(TESTS_PATH)

    if not test_files:
        return

    tests = []
    for fname in test_files:
        m = re.match(r'(.*)_out\.txt', fname)
        if m:
            tests.append(m.group(1))

    if not tests:
        return
        
    for t in tests:
        input = open(TESTS_PATH + t + '.txt', encoding='utf8').read()
        expecting = open(TESTS_PATH + t + '_out.txt', encoding='utf8').read()
        output = FUNCTION_TO_TEST(input)

        if str(output) != expecting:
            print(
                f"Test '{t}' is failing:", 
                "\n-Expected: ", r"'''", f"{expecting}", r"'''", 
                "\n-Had: ", r"'''", f"{output}", r"'''",
                file=sys.stderr, sep=''
            )
            exit(1)

test()
