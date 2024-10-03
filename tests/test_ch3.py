import sys
import os
import time
import asyncio
import unittest
from unittest.mock import patch, AsyncMock, MagicMock

sys.path.append(os.path.abspath('docs/3. Handling CPU and IO Bound Tasks'))
from ex_3_1 import fetch_data as fetch_data_ex_1, main as main_ex_1
from ex_3_2 import fetch_data as fetch_data_ex_2, main as main_ex_2
from ex_3_3 import fetch_data as fetch_data_ex_3, main as main_ex_3
from ex_3_4 import fetch_data as fetch_data_ex_4, main as main_ex_4
from ex_3_5 import cpu_bound_task, without_multiprocessing, with_multiprocessing, main as main_ex_5


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


class TestEx2AsyncHttpx(unittest.IsolatedAsyncioTestCase):
    @patch('httpx.AsyncClient.get')
    async def test_fetch_data_success(self, mock_get):
        """Test successful fetching of data."""
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = 'Success'

        url = 'https://www.example.com/'
        response1, response2, response3 = await fetch_data_ex_2(url)
        mock_get.assert_called_with(url)
        assert mock_get.call_count == 3

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)
        self.assertEqual(response1.text, 'Success')
        self.assertEqual(response2.text, 'Success')
        self.assertEqual(response3.text, 'Success')

    @patch('ex_3_2.fetch_data', new_callable=AsyncMock)
    async def test_main_success(self, mock_fetch):
        """Test main function when fetch_data is successful."""
        mock_fetch.return_value.status_code = 200
        mock_fetch.return_value = '<Response [200 OK]>', '<Response [200 OK]>', '<Response [200 OK]>'

        with patch('builtins.print') as mocked_print:
            await main_ex_2()
            mocked_print.assert_any_call(f"response1: {mock_fetch.return_value[0]}, "
                                         f"response2: {mock_fetch.return_value[1]}, "
                                         f"response3: {mock_fetch.return_value[2]}")


class TestEx3AsyncHttpx(unittest.IsolatedAsyncioTestCase):
    @patch('httpx.AsyncClient.get')
    async def test_fetch_data_success(self, mock_get):
        """Test successful fetching of data."""
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = 'Success'

        url = 'https://www.example.com/'
        response1, response2, response3 = await fetch_data_ex_3(url)
        mock_get.assert_called_with(url)
        assert mock_get.call_count == 3

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)
        self.assertEqual(response1.text, 'Success')
        self.assertEqual(response2.text, 'Success')
        self.assertEqual(response3.text, 'Success')

    @patch('ex_3_3.fetch_data', new_callable=AsyncMock)
    async def test_main_success(self, mock_fetch):
        """Test main function when fetch_data is successful."""
        mock_fetch.return_value.status_code = 200
        mock_fetch.return_value = ['<Response [200 OK]>', '<Response [200 OK]>', '<Response [200 OK]>']

        with patch('builtins.print') as mocked_print:
            await main_ex_3()
            mocked_print.assert_any_call(f'obj: {mock_fetch.return_value}, obj type: {type(mock_fetch.return_value)}')


class TestEx4AsyncHttpx(unittest.TestCase):
    @patch('httpx.get')
    def test_fetch_data_success(self, mock_get):
        """Test successful fetching of data."""
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = 'Success'

        url = 'https://www.example.com/'
        response1, response2, response3 = fetch_data_ex_4(url)
        mock_get.assert_called_with(url)
        assert mock_get.call_count == 3

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)
        self.assertEqual(response1.text, 'Success')
        self.assertEqual(response2.text, 'Success')
        self.assertEqual(response3.text, 'Success')

    @patch('ex_3_4.fetch_data', new_callable=MagicMock)
    def test_main_success(self, mock_fetch):
        """Test main function when fetch_data is successful."""
        mock_fetch.return_value.status_code = 200
        mock_fetch.return_value = '<Response [200 OK]>', '<Response [200 OK]>', '<Response [200 OK]>'

        with patch('builtins.print') as mocked_print:
            main_ex_4()
            mocked_print.assert_any_call(f"response1: {mock_fetch.return_value[0]}, "
                                         f"response2: {mock_fetch.return_value[1]}, "
                                         f"response3: {mock_fetch.return_value[2]}")


class TestMultiprocessingPerformance(unittest.TestCase):

    def setUp(self):
        self.step = 2
        self.value = 100000000

    def test_with_and_without_mp(self):
        value1, value2, time_taken = without_multiprocessing(self.step, self.value)
        self.assertEqual(value1, value2)
        self.assertEqual(value1, self.value * self.step)

        value1_mp, value2_mp, time_taken_mp = with_multiprocessing(self.step, self.value)
        self.assertEqual(value1_mp, value2_mp)
        self.assertEqual(value1_mp, self.value * self.step)
        self.assertEqual(value2_mp, self.value * self.step)
        self.assertLessEqual(time_taken_mp * 1.7, time_taken,
                             msg='time taken without mp is less than 1.7 times of with mp!')

    def test_main(self):
        with patch('builtins.print') as mocked_print:
            main_ex_5()
            value = self.value * self.step
            mocked_print.assert_any_call(f'Without multiprocessing, value1: {value}, value2: {value}')
            mocked_print.assert_any_call(f'======================================')
            mocked_print.assert_any_call(f'With multiprocessing, value1: {value}, value2: {value}')


if __name__ == '__main__':
    unittest.main()
