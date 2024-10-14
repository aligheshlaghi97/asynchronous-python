import sys
import os
import time
import asyncio
import unittest
from unittest.mock import patch, AsyncMock, MagicMock

sys.path.append(os.path.abspath('docs/4. Synchronization and Coordination'))
import ex_4_1 as ex1
import ex_4_2 as ex2
import ex_4_3 as ex3


class TestEx1AsyncTask(unittest.TestCase):
    @patch('asyncio.sleep', return_value=None)
    def test_task(self, mock_sleep):
        """Test task function."""
        ex1.value = 0

        asyncio.run(ex1.task())
        self.assertEqual(ex1.value, 1)

        asyncio.run(ex1.task())
        self.assertEqual(ex1.value, 2)

        mock_sleep.assert_called_with(0.01)

    def test_main_success(self):
        """Test main function"""
        with patch('builtins.print') as mocked_print:
            asyncio.run(ex1.main())
            mocked_print.assert_any_call(1)


class TestEx2AsyncTask(unittest.TestCase):
    @patch('asyncio.sleep', return_value=None)
    def test_task(self, mock_sleep):
        """Test task function."""
        ex2.value = 0
        lock = asyncio.Lock()
        asyncio.run(ex2.task(lock))
        self.assertEqual(ex2.value, 1)

        asyncio.run(ex2.task(lock))
        self.assertEqual(ex2.value, 2)

        mock_sleep.assert_called_with(0.00)

    def test_main_success(self):
        """Test main function"""
        with patch('builtins.print') as mocked_print:
            asyncio.run(ex2.main())
            mocked_print.assert_any_call(10000)


class TestEx3Semaphore(unittest.IsolatedAsyncioTestCase):
    @patch('asyncio.sleep', return_value=None)
    def test_limited_resource(self, mock_sleep):
        """Test limited resource function."""
        ex2.value = 0
        lock = asyncio.Lock()
        asyncio.run(ex2.task(lock))
        self.assertEqual(ex2.value, 1)

        asyncio.run(ex2.task(lock))
        self.assertEqual(ex2.value, 2)

        with patch('builtins.print') as mocked_print:
            asyncio.run(ex3.main())
            mocked_print.assert_any_call("Accessing limited resource")
            mocked_print.assert_any_call("Finished using limited resource")

        mock_sleep.assert_called_with(1)

    def test_main_success(self):
        """Test main function"""
        with patch('builtins.print') as mocked_print:
            time_start = time.time()
            asyncio.run(ex3.main())
            time_taken = time.time() - time_start

            self.assertLess(time_taken, 3)
            self.assertLess(2, time_taken)

            mocked_print.assert_any_call("Accessing limited resource")
            mocked_print.assert_any_call("Finished using limited resource")


if __name__ == '__main__':
    unittest.main()