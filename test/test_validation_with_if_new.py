import unittest
import unittest.mock as mock
from input_validation import validation_with_if_new


class MyTestCase(unittest.TestCase):

    def test_average_equal(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert validation_with_if_new.average(85, 90, 95) == 90

    def test_average_not_equal_(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert validation_with_if_new.average(85, 90, 95) != 91

    def test_average_greater_than(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert validation_with_if_new.average(85, 90, 95) > 89

    def test_negative_one(self):
        with mock.patch('builtins.input', side_effects=[-85, 90, 95]):
            assert validation_with_if_new.average(85, 90, 95), -1

    def test_input_validation_if(self):
        self.assertEqual(-1, validation_with_if_new.average(-85, 90, 95))


if __name__ == '__main__':
    unittest.main()
