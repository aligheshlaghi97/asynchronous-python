import sys
import os
import time
import asyncio
import unittest
from unittest.mock import patch, AsyncMock

sys.path.append(os.path.abspath('docs/2. Getting Started with asyncio'))
from ex_2_1 import async_sleep_for_one_second as async_sleep_ex_1
from ex_2_2 import async_sleep_for_one_second as async_sleep_ex_2
from ex_2_3 import nested as nested_ex_3, main as main_ex_3
from ex_2_4 import sleep_coro as sleep_coro_ex_4, main as main_ex_4
from ex_2_5 import sleep_coro as sleep_coro_ex_5, main as main_ex_5
from ex_2_6 import sleep_coro as sleep_coro_ex_6, main as main_ex_6
from ex_2_7 import sleep_coro as sleep_coro_ex_7, main as main_ex_7
from ex_2_8 import sleep_coro as sleep_coro_ex_8, main as main_ex_8


class TestEx1AsyncSleep(unittest.TestCase):
    @patch('asyncio.sleep', return_value=None)
    def test_async_sleep_for_one_second(self, mock_sleep):
        with patch('builtins.print') as mock_print:
            asyncio.run(async_sleep_ex_1())

            # Check if the print statements were called correctly
            mock_print.assert_any_call('stared sleeping for 1 second!')
            mock_print.assert_any_call('Finished sleeping!')

            # Ensure that asyncio.sleep was called once
            mock_sleep.assert_called_once_with(1)


class TestEx2AsyncSleep(unittest.TestCase):
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


class TestEx3AsyncNested(unittest.IsolatedAsyncioTestCase):
    async def test_nested(self):
        result = await nested_ex_3()
        self.assertEqual(result, 42)

    def test_main(self):
        with patch('builtins.print') as mock_print:
            asyncio.run(main_ex_3())
            mock_print.assert_any_call(42)


class TestEx4AsyncSleep(unittest.IsolatedAsyncioTestCase):
    @patch('asyncio.sleep', return_value=None)
    async def test_sleep_async_for_ten_second(self, mock_sleep):
        with patch('builtins.print') as mock_print:
            await sleep_coro_ex_4(10)

            mock_print.assert_any_call('Started sleeping for 10 seconds!')
            mock_print.assert_any_call('Finished sleeping for 10 seconds!')

            mock_sleep.assert_called_once_with(10)

    async def test_main_async_sleep_for_one_second(self):
        with patch('builtins.print') as mock_print:
            await main_ex_4()
            mock_print.assert_any_call('Started sleeping for 1 seconds!')
            mock_print.assert_any_call('Finished sleeping for 1 seconds!')


class TestEx5AsyncSleep(unittest.IsolatedAsyncioTestCase):
    @patch('asyncio.sleep', return_value=None)
    async def test_sleep_async_for_five_second(self, mock_sleep):
        with patch('builtins.print') as mock_print:
            await sleep_coro_ex_5(5)

            mock_print.assert_any_call('Started sleeping for 5 seconds!')
            mock_print.assert_any_call('Finished sleeping for 5 seconds!')

            mock_sleep.assert_called_once_with(5)

    async def test_main_async_sleep_two_concurrent_one_sec_sleep_took_about_one_sec(self):
        with patch('builtins.print') as mock_print:
            start_time = time.time()
            await main_ex_5()
            self.assertLess(time.time() - start_time, 1.1)
            mock_print.assert_any_call('Started sleeping for 1 seconds!')
            mock_print.assert_any_call('Finished sleeping for 1 seconds!')


class TestEx6AsyncSleep(unittest.IsolatedAsyncioTestCase):
    @patch('asyncio.sleep', return_value=None)
    async def test_sleep_async_for_three_second(self, mock_sleep):
        with patch('builtins.print') as mock_print:
            await sleep_coro_ex_6(3)

            mock_print.assert_any_call('Started sleeping for 3 seconds!')
            mock_print.assert_any_call('Finished sleeping for 3 seconds!')

            mock_sleep.assert_called_once_with(3)

    async def test_main_async_sleep_for_one_second(self):
        with patch('builtins.print') as mock_print:
            await main_ex_6()
            mock_print.assert_any_call('Started sleeping for 1 seconds!')
            mock_print.assert_any_call('Finished sleeping for 1 seconds!')


class TestEx7AsyncSleep(unittest.IsolatedAsyncioTestCase):
    @patch('asyncio.sleep', return_value=None)
    async def test_sleep_async_for_seven_second(self, mock_sleep):
        with patch('builtins.print') as mock_print:
            result = await sleep_coro_ex_7(7)
            self.assertEqual(result, 7)
            mock_print.assert_any_call('Started sleeping for 7 seconds!')
            mock_print.assert_any_call('Finished sleeping for 7 seconds!')

            mock_sleep.assert_called_once_with(7)

    async def test_main_async_sleep_two_concurrent_two_and_three_sec_sleep_took_about_three_sec(self):
        with patch('builtins.print') as mock_print:
            start_time = time.time()
            await main_ex_7()
            self.assertLess(time.time() - start_time, 3.1)

            mock_print.assert_any_call('Before running task group!')

            mock_print.assert_any_call('Started sleeping for 2 seconds!')
            mock_print.assert_any_call('Started sleeping for 3 seconds!')
            mock_print.assert_any_call('Finished sleeping for 2 seconds!')
            mock_print.assert_any_call('Finished sleeping for 3 seconds!')

            mock_print.assert_any_call('After running task group!')
            mock_print.assert_any_call('task1: 2, task2: 3')


class TestEx8AsyncSleep(unittest.IsolatedAsyncioTestCase):
    @patch('asyncio.sleep', return_value=None)
    async def test_sleep_async_for_four_second(self, mock_sleep):
        with patch('builtins.print') as mock_print:
            await sleep_coro_ex_8(4)

            mock_print.assert_any_call('Started sleeping for 4 seconds!')
            mock_print.assert_any_call('Finished sleeping for 4 seconds!')

            mock_sleep.assert_called_once_with(4)

    async def test_main_async_sleep_for_two_second_expect_timeout(self):
        with patch('builtins.print') as mock_print:
            await main_ex_8()
            mock_print.assert_any_call('Started sleeping for 2 seconds!')
            mock_print.assert_any_call('timeout!')


if __name__ == '__main__':
    unittest.main()
