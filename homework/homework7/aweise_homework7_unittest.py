import unittest
import datetime


# @desc - I tried to make this unit test as robust as possible to test for the
# various timedelta units, but also cut things short for the sake of 
# reviewing (I think we can all agree that datetime works).
#
# Tests:
# date + date
# timedelta + timedelta
# timedelta + timedelta type check
# date + timedelta type check
# date + timedelta
# date - date
# timedelta - timedelta
# timedelta - timedelta type check
# date - timedelta type check
# date - timedelta
class TestDateTime(unittest.TestCase):

    def setUp(self):
        self.date_1 = datetime.date(
            year = 2020,
            month = 3,
            day = 22,
        )
        self.date_2 = datetime.date(
            year = 1991,
            month = 1,
            day = 7,
        )
        self.timedelta_weeks = datetime.timedelta(weeks = 1)
        self.timedelta_days = datetime.timedelta(days = 10)
        self.timedelta_hours = datetime.timedelta(hours = 10)
        self.timedelta_minutes = datetime.timedelta(minutes = 10)
        self.timedelta_seconds = datetime.timedelta(seconds = 10)
        self.timedelta_milliseconds = datetime.timedelta(milliseconds = 10)
        self.timedelta_microseconds = datetime.timedelta(microseconds = 10)
        

    def test_add(self):
        # date + date
        with self.assertRaises(TypeError):
            self.date_1 + self.date_2
        # timedelta + timedelta
        self.assertEqual(
            self.timedelta_days + self.timedelta_hours,
            datetime.timedelta(
                days = 10, 
                hours = 10,
            )
        )
        # timedelta + timedelta type check
        self.assertIsInstance( 
            self.timedelta_minutes + self.timedelta_hours,
            datetime.timedelta
        )
        # date + timedelta type check
        self.assertIsInstance(
            self.date_1 + self.timedelta_days,
            datetime.date
        )
        # date + timedelta in weeks
        self.assertEqual(
            self.date_1 + self.timedelta_weeks, 
            datetime.date(
                year = 2020, 
                month = 3, 
                day = 29,
            )
        )
        # date + timedelta in days
        self.assertEqual(
            self.date_1 + self.timedelta_days,
            datetime.date(
                year = 2020,
                month = 4,
                day = 1,
            )
        )
        # date + timedelta in hours
        self.assertEqual(
            self.date_1 + self.timedelta_hours,
            datetime.date(
                year = 2020, 
                month = 3, 
                day = 22,
            )
        )
        # date + timedelta in minutes
        self.assertEqual(
            self.date_1 + self.timedelta_minutes,
            datetime.date(
                year = 2020, 
                month = 3, 
                day = 22,
            )
        )
        # date + timedelta in seconds
        self.assertEqual(
            self.date_1 + self.timedelta_seconds,
            datetime.date(
                year = 2020, 
                month = 3, 
                day = 22,
            )
        )
        # date + timedelta in milliseconds
        self.assertEqual(
            self.date_1 + self.timedelta_milliseconds,
            datetime.date(
                year = 2020, 
                month = 3, 
                day = 22,
            )
        )
        # date + timedelta in microseconds
        self.assertEqual(
            self.date_1 + self.timedelta_microseconds,
            datetime.date(
                year = 2020, 
                month = 3, 
                day = 22,
            )
        )


    def test_subtract(self):
        # date - date
        self.assertEqual(
            self.date_1 - self.date_2, 
            datetime.timedelta(10667)
        )
        # timedelta - timedelta
        self.assertEqual(
            self.timedelta_days - self.timedelta_hours,
            datetime.timedelta(
                days = 9, 
                hours = 14,
            )
        )
        # timedelta - timedelta type check
        self.assertIsInstance( 
            self.timedelta_minutes - self.timedelta_hours,
            datetime.timedelta
        )
        # date - timedelta type check
        self.assertIsInstance(
            self.date_1 - self.timedelta_days,
            datetime.date
        )
        # date - timedelta in weeks
        self.assertEqual(
            self.date_1 - self.timedelta_weeks, 
            datetime.date(
                year = 2020, 
                month = 3, 
                day = 15,
            )
        )
        # date - timedelta in days
        self.assertEqual(
            self.date_1 - self.timedelta_days,
            datetime.date(
                year = 2020,
                month = 3,
                day = 12,
            )
        )
        # date - timedelta in hours
        self.assertEqual(
            self.date_1 - self.timedelta_hours,
            datetime.date(
                year = 2020, 
                month = 3, 
                day = 22,
            )
        )
        # date - timedelta in minutes
        self.assertEqual(
            self.date_1 - self.timedelta_minutes,
            datetime.date(
                year = 2020, 
                month = 3, 
                day = 22,
            )
        )
        # date - timedelta in seconds
        self.assertEqual(
            self.date_1 - self.timedelta_seconds,
            datetime.date(
                year = 2020, 
                month = 3, 
                day = 22,
            )
        )
        # date - timedelta in milliseconds
        self.assertEqual(
            self.date_1 - self.timedelta_milliseconds,
            datetime.date(
                year = 2020, 
                month = 3, 
                day = 22,
            )
        )
        # date - timedelta in microseconds
        self.assertEqual(
            self.date_1 - self.timedelta_microseconds,
            datetime.date(
                year = 2020, 
                month = 3, 
                day = 22,
            )
        )

    
if __name__ == '__main__':
    unittest.main()