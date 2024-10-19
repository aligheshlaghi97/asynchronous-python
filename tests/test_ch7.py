import sys
import os
import unittest
from unittest.mock import patch, AsyncMock, MagicMock
import threading
import requests
import time
sys.path.append(os.path.abspath('docs/7. Web Applications'))
import ex_7_1 as ex1
import ex_7_2 as ex2


class TestGunicornApp(unittest.TestCase):
    def test_app_gunicorn(self):
        with patch('builtins.print') as mocked_print:
            data = b'Hello, World!\n'
            response_headers = [
                ('Content-type', 'text/plain'),
                ('Content-Length', str(len(data)))
            ]
            result = ex1.app(None, mocked_print)
            mocked_print.assert_any_call("200 OK", response_headers)
            self.assertEqual(next(result), data)


class TestUvicornApp(unittest.IsolatedAsyncioTestCase):
    async def test_app_uvicorn(self):
        with patch('asyncio.sleep') as send_data:
            data1_to_send = {
                'type': 'http.response.start',
                'status': 200,
                'headers': [
                    [b'content-type', b'text/plain'],
                ],
            }
            data2_to_send = {
                'type': 'http.response.body',
                'body': b'Hello, world!',
            }
            scope = {
                "type": "http"
            }
            await ex2.app(scope, None, send_data)
            send_data.assert_any_call(data1_to_send)
            send_data.assert_any_call(data2_to_send)


if __name__ == '__main__':
    unittest.main()
