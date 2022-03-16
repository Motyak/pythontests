#!/usr/bin/env python3

from unittest import mock, TestCase, main
from datetime import datetime
import requests # get()

import today # _now()

class MockDatetime:
    pass

class TodayTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.customDate = datetime(1997, 4, 4)

    @mock.patch(f'{datetime.__name__}.datetime', wraps=datetime)
    def testTodayNowCallsDatetimeNow(self, mockDatetime):
        mockDatetime.now.return_value = self.customDate
        assert today._now() == self.customDate

    def testDatetimeNow(self):
        API_URL = 'http://worldclockapi.com/api/json/utc/now'
        API_FIELD = 'currentDateTime'
        API_FIELD_FORMAT = r'%Y-%m-%dT%H:%MZ'
        res = requests.get(url=API_URL).json()
        webDateAsStr = res[API_FIELD]
        dateAsStr = datetime.utcnow().strftime(API_FIELD_FORMAT)
        assert webDateAsStr == dateAsStr

if __name__ == '__main__':
    main()
