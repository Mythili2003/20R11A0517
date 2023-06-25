import requests
import time

def get_numbers(urls):
    result = []
    for url in urls:
        try:
            start_time = time.time()
            response = requests.get(url, timeout=0.5)
            elapsed_time = time.time() - start_time

            if response.status_code == 200 and elapsed_time <= 0.5:
                data = response.json()
                if 'numbers' in data:
                    result.extend(data['numbers'])
        except (requests.exceptions.RequestException, ValueError):
            pass

    result = sorted(set(result))
    return result

if __name__ == '__main__':
    urls = [
       'http://104.211.219.98/numbers/primes',
       'http://104.211.219.98/numbers/fibo',
       'http://104.211.219.98/numbers/odd',
       'http://104.211.219.98/numbers/rand'
    ]
    
    numbers = get_numbers(urls)
    response = {'numbers': numbers}
    print(response)
