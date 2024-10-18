import sys
import os
import time
import asyncio
import unittest
from unittest.mock import patch, AsyncMock, MagicMock

sys.path.append(os.path.abspath('docs/5. Advanced Techniques'))
import ex_5_1 as ex1
import ex_5_2 as ex2
import ex_5_3 as ex3
import ex_5_4 as ex4


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


class TestEx2ExceptionHandler(unittest.TestCase):
    @patch('asyncio.sleep', return_value=None)
    def test_shorter_task(self, mock_sleep):
        """Test shorter task function."""
        with patch('builtins.print') as mocked_print:
            with patch('ex_5_2.Exception') as mock_exception, self.assertRaises(Exception):
                asyncio.run(ex2.shorter_task())
                mock_exception.assert_called_once_with("Some exception happened!")
            mocked_print.assert_called_once_with("Executing the task to raise an exception!")
            mock_sleep.assert_called_once_with(0.01)

    @patch('asyncio.sleep', return_value=None)
    def test_longer_task(self, mock_sleep):
        """Test longer task function."""
        with patch('builtins.print') as mocked_print:
            asyncio.run(ex2.longer_task())
            mocked_print.assert_any_call("Executing the task which will complete!")
            mock_sleep.assert_called_once_with(1)
            mocked_print.assert_any_call("longer_task is done!")

    def test_exception_handler(self):
        """Test exception handler."""
        with patch('builtins.print') as mocked_print:
            context = {"exception": "Test exception!"}
            ex2.exception_handler(None, context)
            mocked_print.assert_called_once_with("Exception: Test exception!")

    @patch('asyncio.sleep', return_value=None)
    def test_main(self, mock_sleep):
        """Test main function."""
        with patch('builtins.print') as mocked_print:
            asyncio.run(ex2.main())
            mocked_print.assert_any_call("Main coroutine started!")
            mocked_print.assert_any_call("Executing the task to raise an exception!")
            mocked_print.assert_any_call("Executing the task which will complete!")
            mock_sleep.assert_any_call(1)
            mock_sleep.assert_any_call(0.01)
            mocked_print.assert_any_call("longer_task is done!")
            mocked_print.assert_any_call("Exception: Some exception happened!")
            mocked_print.assert_any_call("Main coroutine done!")


class TestEx3CancelTask(unittest.TestCase):
    @patch('asyncio.sleep', return_value=None)
    def test_cancel_me(self, mock_sleep):
        """Test cancel_me function."""
        asyncio.run(ex3.cancel_me())
        mock_sleep.assert_called_once_with(1)

    @patch('asyncio.sleep', return_value=None)
    def test_main(self, mock_sleep):
        """Test main function"""
        with patch('builtins.print') as mocked_print:
            asyncio.run(ex3.main())
            mocked_print.assert_called_once_with("main(): cancel_me is cancelled now")
            mock_sleep.assert_any_call(0.01)


class TestEx4ChainTasks(unittest.IsolatedAsyncioTestCase):
    @patch('asyncio.sleep', return_value=None)
    async def test_task1(self, mock_sleep):
        """Test task1 function."""
        with patch('builtins.print') as mocked_print:
            result = await ex4.task1()
            mock_sleep.assert_called_once_with(1)
            mocked_print.assert_called_once_with(">task1()")
            self.assertEqual(result, 1)

    @patch('asyncio.sleep', return_value=None)
    async def test_task2(self, mock_sleep):
        """Test task2 function."""
        with patch('builtins.print') as mocked_print:
            value = 1
            await ex4.task2(value)
            mock_sleep.assert_called_once_with(1)
            mocked_print.assert_called_once_with(f">task2() got {value}")

    @patch('asyncio.sleep', return_value=None)
    def test_main(self, mock_sleep):
        """Test main function"""
        with patch('builtins.print') as mocked_print:
            asyncio.run(ex4.main())
            mocked_print.assert_any_call(">task1()")
            mocked_print.assert_any_call(f">task2() got 1")

            mocked_print.assert_any_call("Main: chain is done")
            mock_sleep.assert_any_call(1)
            self.assertTrue(ex4.event.is_set())


if __name__ == '__main__':
    unittest.main()
