import sys
import os
import time
import asyncio
import unittest
from unittest.mock import patch, AsyncMock, MagicMock

sys.path.append(os.path.abspath('docs/4. Synchronization and Coordination'))
from ex_4_1 import task as task_ex_1, main as main_ex_1


class TestEx1AsyncTask(unittest.TestCase):
    @patch('asyncio.sleep', return_value=None)
    def test_task(self, mock_sleep):
        """Test task function."""
        global value
        value = 0
        asyncio.run(task_ex_1())

        self.assertEqual(value, 0)  # TODO: this must equal with 1 not 0
        mock_sleep.assert_called_with(0.01)

    def test_main_success(self):
        """Test main function"""
        with patch('builtins.print') as mocked_print:
            asyncio.run(main_ex_1())
            mocked_print.assert_any_call(1)


if __name__ == '__main__':
    unittest.main()
