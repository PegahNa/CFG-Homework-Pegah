"""
read a file line by line and check the number of the last line.
Extract that number, increment by 1 and return the new number

If you have a file example.txt like this:

1. Melon
2. Pear
3. Apple

Read the last line, extract number 3 and increment it by 1.
"""

from unittest import mock
from unittest import TestCase, main
from code_to_test_mock import increment_line_number


class TestIncrementLineNumber(TestCase):

    @mock.patch('code_to_test_mock.get_file_content')
    def test_mock_file_read_function(self, mock_get_file_content):
        content = [
            '1. Hello',
            '2. Hi',
            '3. Good morning',
        ]
        mock_get_file_content.return_value = content

        self.assertEqual(
            increment_line_number('some_file'),
            4
        )

if __name__ == '__main__':
    main()
