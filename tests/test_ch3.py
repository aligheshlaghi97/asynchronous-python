import sys
import os
import time
import asyncio
import unittest
from unittest.mock import patch, AsyncMock

sys.path.append(os.path.abspath('docs/3. Handling CPU and IO Bound Tasks'))
from ex_3_1 import fetch_data as fetch_data_ex_1, main as main_ex_1


class TestEx1AsyncHttpx(unittest.IsolatedAsyncioTestCase):
    @patch('httpx.AsyncClient.get')
    async def test_fetch_data_success(self, mock_get):
        """Test successful fetching of data."""
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = 'Success'

        url = 'https://www.example.com/'
        response = await fetch_data_ex_1(url)
        mock_get.assert_called_once_with(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Success')

    @patch('httpx.AsyncClient.get')
    async def test_fetch_data_failure(self, mock_get):
        """Test failure when fetching data."""
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        url = 'https://www.example.com/'
        response = await fetch_data_ex_1(url)
        mock_get.assert_called_once_with(url)

        self.assertEqual(response.status_code, 404)

    @patch('ex_3_1.fetch_data', new_callable=AsyncMock)
    async def test_main_success(self, mock_fetch):
        """Test main function when fetch_data is successful."""
        mock_fetch.return_value.status_code = 200
        mock_fetch.return_value = '<Response [200 OK]>'

        with patch('builtins.print') as mocked_print:
            await main_ex_1()
            mocked_print.assert_any_call(f"response is: {mock_fetch.return_value}")


if __name__ == '__main__':
    unittest.main()
