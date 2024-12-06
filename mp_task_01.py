from threading import Thread
from time import perf_counter
from multiprocessing import Process
import requests
import asyncio

# список url
urls = ['https://www.example.com'] * 10


def fetch_url(url):
    response = requests.get(url)
    return response.text


def sequence():
    # время старта start_time
    start_time = perf_counter()

    # выполнение функции fetch_url для каждого url из urls
    for url in urls:
        fetch_url(url)

    # время окончания end_time
    end_time = perf_counter()

    print(f'sequence time: {end_time - start_time: 0.2f} \n')


def threads():
    # время старта start_time
    start_time = perf_counter()

    # массив потоков
    threads_arr = []

    # выполнение с помощью потоков функции fetch_url для каждого url из urls (с ожиданием окончания выполнения всех потоков)
    for url in urls:
        thread = Thread(target=fetch_url, args=(url,))
        threads_arr.append(thread)
        thread.start()

    for thread in threads_arr:
        thread.join()

    # время окончания end_time
    end_time = perf_counter()

    print(f'threads time: {end_time - start_time: 0.2f} \n')


def processes():
    # время старта start_time
    start_time = perf_counter()

    p_arr = []

    # выполнение с помощью процессов функции fetch_url для каждого url из urls (с ожиданием окончания выполнения всех потоков)
    for url in urls:
        p = Process(target=fetch_url, args=(url,))
        p_arr.append(p)
        p.start()

    for p in p_arr:
        p.join()

    # время окончания end_time
    end_time = perf_counter()

    print(f'processes time: {end_time - start_time: 0.2f} \n')


async def asyncMethod():
    # время старта start_time
    start_time = perf_counter()

    loop = asyncio.get_running_loop()
    # Создаём задачи для выполнения fetch_url в пуле потоков
    tasks = [loop.run_in_executor(None, fetch_url, url) for url in urls]
    await asyncio.gather(*tasks)

    # время окончания end_time
    end_time = perf_counter()

    print(f'async time: {end_time - start_time: 0.2f} \n')


if __name__ == '__main__':
    sequence()
    threads()
    processes()
    asyncio.run(asyncMethod())
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):
        
        sequence time:  ???

        threads time:  ???
        
        processes time:  ???
    """
