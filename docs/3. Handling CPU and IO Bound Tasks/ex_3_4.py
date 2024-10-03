import time
import httpx


def fetch_data(url):
    response1 = httpx.get(url)
    response2 = httpx.get(url)
    response3 = httpx.get(url)
    return response1, response2, response3


def main():
    url = 'https://www.example.org/'
    t = time.time()
    response1, response2, response3 = fetch_data(url)
    print(f'It took {time.time() - t} s')
    print(f'response1: {response1}, response2: {response2}, response3: {response3}')


if __name__ == '__main__':
    main()
