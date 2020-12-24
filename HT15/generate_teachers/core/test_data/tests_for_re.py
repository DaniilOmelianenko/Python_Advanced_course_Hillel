from unittest import TestCase
# from unittest.mock import patch, Mock
from unittest.mock import patch

from regular import delete_negative_floats, find_all_dates, sum_floats


class SumFloatsTestCase(TestCase):

    @patch('regular.findall', return_value=['-12.3', '-10', '3', '-1', '-1', '-1', '-11.1']) # noqa
    def test_sum_floats(self, mock_findall):
        test_text = '-12.3-10-da3.-1-1-1-11.1/-'
        expected_result = ['-12.3', '-10', '3', '-1', '-1', '-1', '-11.1']
        string = sum_floats(test_text)
        mock_findall.assert_called_once()
        self.assertEqual(expected_result, string)


class DeleteNegativeFloatsTestCase(TestCase):

    @patch('regular.sub', return_value='test')
    def test_delete_negative_floats(self, mock_sub):
        test_text = '-123.00001test'
        expected_result = 'test'
        string = delete_negative_floats(test_text)
        # mock_sub.assert_called_once()
        self.assertEqual(mock_sub.call_count, 1)
        self.assertEqual(expected_result, string)


class FindDatesTestCase(TestCase):

    def test_non_existent_dates(self):
        test_text = '29-02-2016 30-02-2016 31-02-2016 29-02-2017 31-04-1991'
        expected_result = ['29-02-2016']
        dates = find_all_dates(test_text)
        self.assertEqual(expected_result, dates)

    def test_single_digits_dates(self):
        test_text = '3-3-2016 01-1-1500 9-01-2020 01-05-2017'
        expected_result = ['3-3-2016', '01-1-1500', '9-01-2020', '01-05-2017']
        dates = find_all_dates(test_text)
        self.assertEqual(expected_result, dates)
