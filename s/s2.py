from unittest import TestCase
from s1 import say_hi

our_input = 'Pegah'
expected_output = f'Hi, {our_input}'

my_test_case_class = TestCase()

def test_say_hi_success():
    our_input = 'Pegah'
    result = say_hi(our_input)
    my_test_case_class.assertEqual(
        result,
        expected_output,
        "Success"
    )

def test_say_hi_failure():
    our_input = 'Pegah'
    another_input = 'John'
    my_test_case_class.assertNotEqual(
        say_hi(our_input),
        say_hi(another_input),
        "Failure"
    )


test_say_hi_success()
test_say_hi_failure()

