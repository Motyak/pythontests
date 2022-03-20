#!/usr/bin/env python3

from unittest import mock, TestCase, main
from datetime import datetime
import requests # get()
import sys # stderr

import today # _now()

class TodayTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.customDate = datetime(1997, 4, 4)

    @mock.patch(f'{datetime.__name__}.datetime', wraps=datetime)
    def testTodayNowCallsDatetimeNow(self, mockDatetime):
        mockDatetime.now.return_value = self.customDate
        assert today._now() == self.customDate

    def testDatetimeNowMatchesSystemTime(self):
        print(datetime.now())
        userInput = input('Does this match your system clock? (Y/n)\n>')
        assert not userInput or userInput.lower() == 'y'

    def testSystemTimeMatchesWebTime(self):
        API_URL = 'http://worldclockapi.com/api/json/utc/now'
        API_FIELD = 'currentDateTime'
        API_FIELD_FORMAT = r'%Y-%m-%dT%H:%MZ'

        dateAsStr = datetime.utcnow().strftime(API_FIELD_FORMAT)
        try:
            res = requests.get(url=API_URL).json()
            webDateAsStr = res[API_FIELD]
            if dateAsStr != webDateAsStr:
                print(f"WARN: Your system clock ({dateAsStr}) isn't on time, "
                        + f'should be {webDateAsStr}', file=sys.stderr)
        except:
            print(f"WARN: We couldn't check if your system clock is on time "
                    + f'({dateAsStr})', file=sys.stderr)

        assert True

if __name__ == '__main__':
    main()
