import time
import httpx


url = 'https://www.example.org/'
t = time.time()
response1 = httpx.get(url)
response2 = httpx.get(url)
response3 = httpx.get(url)
print(f'It took {time.time() - t} s')
print(f'response1: {response1}, response2: {response2}, response3: {response3}')
