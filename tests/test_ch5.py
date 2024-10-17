import sys
import os
import time
import asyncio
import unittest
from unittest.mock import patch, AsyncMock, MagicMock

sys.path.append(os.path.abspath('docs/5. Advanced Techniques'))
import ex_5_1 as ex1


class TestEx1ExceptionPropagate(unittest.TestCase):
    @patch('asyncio.sleep', return_value=None)
    def test_shorter_task(self, mock_sleep):
        """Test shorter task function."""
        with patch('builtins.print') as mocked_print:
            with patch('ex_5_1.Exception') as mock_exception, self.assertRaises(Exception):
                asyncio.run(ex1.shorter_task())
                mock_exception.assert_called_once_with("Some exception happened!")
            mocked_print.assert_called_once_with("Executing the task to raise an exception!")
            mock_sleep.assert_called_once_with(0.1)

    @patch('asyncio.sleep', return_value=None)
    def test_longer_task(self, mock_sleep):
        """Test longer task function."""
        with patch('builtins.print') as mocked_print:
            asyncio.run(ex1.longer_task())
            mocked_print.assert_any_call("Executing the task which will complete!")
            mock_sleep.assert_called_once_with(1)
            mocked_print.assert_any_call("longer_task is done!")

    @patch('asyncio.sleep', return_value=None)
    def test_main(self, mock_sleep):
        """Test main function."""
        with patch('builtins.print') as mocked_print:
            asyncio.run(ex1.main())
            mocked_print.assert_any_call("Main coroutine started!")
            mocked_print.assert_any_call("Executing the task to raise an exception!")
            mocked_print.assert_any_call("Executing the task which will complete!")
            mock_sleep.assert_any_call(1)
            mock_sleep.assert_any_call(0.1)
            mocked_print.assert_any_call("longer_task is done!")
            mocked_print.assert_any_call("Exception: Some exception happened!")
            mocked_print.assert_any_call("Main coroutine done!")


if __name__ == '__main__':
    unittest.main()
