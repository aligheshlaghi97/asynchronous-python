import sys
import os
import time
import asyncio
import unittest
from unittest.mock import patch, AsyncMock, MagicMock

sys.path.append(os.path.abspath('docs/6. Exploring Features of New Python Versions'))
import ex_6_1 as ex1
import ex_6_2 as ex2
import ex_6_3 as ex3


class TestEagerTaskFactory(unittest.TestCase):
    def test_with_eager_task_factory(self):
        """Test running light_coro with eager_task_factory function."""
        with patch('builtins.print') as mocked_print:
            asyncio.run(ex1.main())
            mocked_print.assert_any_call("Before running task group!")
            mocked_print.assert_any_call("After running task group with eager task factory!")
            self.assertEqual(mocked_print.call_count, 3)

    def test_without_eager_task_factory(self):
        """Test running light_coro without eager_task_factory function."""
        with patch('builtins.print') as mocked_print:
            asyncio.run(ex2.main())
            mocked_print.assert_any_call("Before running gather!")
            mocked_print.assert_any_call("After running gather without eager task factory!")
            self.assertEqual(mocked_print.call_count, 4)

    def test_compare_running_time(self):
        """Test if running light_coro with eager_task_factory function is 4 times faster than without it."""
        with patch('builtins.print') as mocked_print:
            asyncio.run(ex1.main())
            printed_outputs = [call[0][0] for call in mocked_print.call_args_list]
            time_taken_output = next((output for output in printed_outputs if "It took" in output), None)
            self.assertIsNotNone(time_taken_output, "The output containing time taken was not found.")

            time_taken_with_eager = float(time_taken_output.split()[2])
            self.assertGreater(time_taken_with_eager, 0)

        with patch('builtins.print') as mocked_print:
            asyncio.run(ex2.main())
            printed_outputs = [call[0][0] for call in mocked_print.call_args_list]
            time_taken_output = next((output for output in printed_outputs if "It took" in output), None)
            self.assertIsNotNone(time_taken_output, "The output containing time taken was not found.")

            time_taken_without_eager = float(time_taken_output.split()[2])
            self.assertGreater(time_taken_without_eager, 0)

        self.assertGreater(time_taken_without_eager, time_taken_with_eager * 4)


class TestEx3CurrentTask(unittest.TestCase):
    def test_current_task_one_million_calls(self):
        """Test if asyncio.current_task is called 1 million times."""
        with patch('asyncio.current_task') as mocked_current_task:
            asyncio.run(ex3.main())
            self.assertEqual(mocked_current_task.call_count, 1_000_000)


if __name__ == '__main__':
    unittest.main()

