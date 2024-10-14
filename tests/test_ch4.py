import sys
import os
import time
import asyncio
import unittest
from unittest.mock import patch, AsyncMock, MagicMock

sys.path.append(os.path.abspath('docs/4. Synchronization and Coordination'))
import ex_4_1 as ex1


class TestEx1AsyncTask(unittest.TestCase):
    @patch('asyncio.sleep', return_value=None)
    def test_task(self, mock_sleep):
        """Test task function."""
        ex1.value = 0

        asyncio.run(ex1.task())
        assert ex1.value == 1

        asyncio.run(ex1.task())
        assert ex1.value == 2

        mock_sleep.assert_called_with(0.01)

    def test_main_success(self):
        """Test main function"""
        with patch('builtins.print') as mocked_print:
            asyncio.run(ex1.main())
            mocked_print.assert_any_call(1)


if __name__ == '__main__':
    unittest.main()
