import unittest

from fifteen import waiting_time


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        arr = [3, 2, 1, 2, 6]
        expected = 17
        actual = waiting_time(arr)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        arr = [2, 1, 1, 1]
        expected = 6
        actual = waiting_time(arr)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        arr = [1, 2, 4, 5, 2, 1]
        expected = 23
        actual = waiting_time(arr)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        arr = [25, 30, 2, 1]
        expected = 32
        actual = waiting_time(arr)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        arr = [1, 1, 1, 1, 1]
        expected = 10
        actual = waiting_time(arr)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        arr = [4, 3, 1, 1, 3, 2, 1, 8]
        expected = 45
        actual = waiting_time(arr)
        self.assertEqual(actual, expected)

    def test_case_7(self):
        arr = [2]
        expected = 0
        actual = waiting_time(arr)
        self.assertEqual(actual, expected)

    def test_case_8(self):
        arr = [5, 4, 3, 2, 1]
        expected = 20
        actual = waiting_time(arr)
        self.assertEqual(actual, expected)

    def test_case_9(self):
        arr = [1, 2, 3, 4, 5]
        expected = 20
        actual = waiting_time(arr)
        self.assertEqual(actual, expected)

    def test_case_10(self):
        arr = [1, 1, 1, 4, 5, 6, 8, 1, 1, 2, 1]
        expected = 81
        actual = waiting_time(arr)
        self.assertEqual(actual, expected)