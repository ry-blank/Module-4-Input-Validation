import unittest
import unittest.mock as mock
from input_validation import validation_with_if


class MyTestCase(unittest.TestCase):

    def test_average_equal(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert validation_with_if.average() == 90

    def test_average_not_equal_(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert validation_with_if.average() != 91

    def test_average_greater_than(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert validation_with_if.average() > 89

    def test_negative_one(self):
        with mock.patch('builtins.input', side_effects=[-85, 90, 95]):
            self.assertEqual(validation_with_if.average(), -1)

    def test_reject_negative_values_using_mock(self):
        with mock.patch('builtins.input', side_effect=[-85, 90, 95]):
            self.assertEqual(validation_with_if.average(), -1)


if __name__ == '__main__':
    unittest.main()
