import sys
import os
import asyncio
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath('docs/2. Getting Started with asyncio'))
from ex_2_1 import async_sleep_for_one_second as async_sleep_ex_1
from ex_2_2 import async_sleep_for_one_second as async_sleep_ex_2


class TestAsyncSleep(unittest.TestCase):
    @patch('asyncio.sleep', return_value=None)
    def test_async_sleep_for_one_second(self, mock_sleep):
        with patch('builtins.print') as mock_print:
            asyncio.run(async_sleep_ex_1())

            # Check if the print statements were called correctly
            mock_print.assert_any_call('stared sleeping for 1 second!')
            mock_print.assert_any_call('Finished sleeping!')

            # Ensure that asyncio.sleep was called once
            mock_sleep.assert_called_once_with(1)


class TestAsyncSleep(unittest.TestCase):
    @patch('asyncio.sleep', return_value=None)
    def test_async_sleep_for_one_second(self, mock_sleep):
        with patch('builtins.print') as mock_print:
            with asyncio.Runner() as runner:
                runner.run(async_sleep_ex_2())

                # Check if the print statements were called correctly
                mock_print.assert_any_call('stared sleeping for 1 second!')
                mock_print.assert_any_call('Finished sleeping!')

                # Ensure that asyncio.sleep was called once
                mock_sleep.assert_called_once_with(1)


if __name__ == '__main__':
    unittest.main()
