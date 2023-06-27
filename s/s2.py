# Importing package we're going to use
import unittest
# Importing our code that we're going to test
from s1 import say_hi

# Create a test case
def test_say_hi():
    name = "Luke"
    expected_result = "Hi, Luke"
    result = say_hi(name)
    assert result == expected_result


# Create a test suite
suite = unittest.TestSuite()
# Add the function to the test suite
suite.addTest(unittest.FunctionTestCase(test_say_hi))

# Run the tests
unittest.TextTestRunner().run(suite)
