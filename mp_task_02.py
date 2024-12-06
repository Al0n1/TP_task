from threading import Thread
from time import perf_counter
from multiprocessing import Process
import asyncio
import math


# Функции для АТ-02

# запускать с n = 700004
def fibonacci(n):  # содержимое функции не менять
    """Возвращает последнюю цифру n-е числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(f'fibonacci = {b % 10}')


# запускать с f, a, b, n равными соответственно math.sin, 0, math.pi, 20000000
def trapezoidal_rule(f, a, b, n):  # содержимое функции не менять
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    print(f'trapezoidal_rule = {integral * h}')


def sequence():
    # время старта start_time
    start_time = perf_counter()

    # вычисление fibonacci от значения 700004
    fibonacci(700004)

    # вычисление trapezoidal_rule со значениями math.sin, 0, math.pi, 20000000
    trapezoidal_rule(math.sin, 0, math.pi, 20000000)

    # время окончания end_time
    end_time = perf_counter()

    print(f'sequence time: {end_time - start_time: 0.2f} \n')


def threads():
    # время старта start_time
    start_time = perf_counter()

    # массив потоков
    threads_arr = []

    # вычисления на потоках:
    thread_fib = Thread(target=fibonacci, args=(700004,))
    threads_arr.append(thread_fib)

    thread_trap = Thread(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000))
    threads_arr.append(thread_trap)

    # 1. вычисление fibonacci от значения 700004
    thread_fib.start()

    # 2. вычисление trapezoidal_rule со значениями math.sin, 0, math.pi, 20000000
    thread_trap.start()

    for thread in threads_arr:
        thread.join()  # ожидание завершения потоков

    # время окончания end_time
    end_time = perf_counter()

    print(f'threads time: {end_time - start_time: 0.2f} \n')


def processes():
    # время старта start_time
    start_time = perf_counter()

    # вычисления на процессах:
    # 1. вычисление fibonacci от значения 700004
    p_fib = Process(target=fibonacci, args=(700004,))
    p_fib.start()

    # 2. вычисление trapezoidal_rule со значениями math.sin, 0, math.pi, 20000000
    p_trap = Process(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000,))
    p_trap.start()

    # ожидание завершения процессов
    p_fib.join()
    p_trap.join()

    # время окончания end_time
    end_time = perf_counter()

    print(f'processes time: {end_time - start_time: 0.2f} \n')


async def asyncMethod():
    # время старта start_time
    start_time = perf_counter()

    task_fib = asyncio.create_task(asyncio.to_thread(fibonacci, 700004))
    task_trap = asyncio.create_task(asyncio.to_thread(trapezoidal_rule, math.sin, 0, math.pi, 20000000))

    await asyncio.gather(task_fib, task_trap)

    # время окончания end_time
    end_time = perf_counter()
    print(f'processes time: {end_time - start_time: 0.2f} \n')


if __name__ == '__main__':
    sequence()
    threads()
    processes()
    asyncio.run(asyncMethod())
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):
        
        fibonacci = 3
        trapezoidal_rule = 2.000000000000087
        sequence time:  ???
        
        fibonacci = 3
        trapezoidal_rule = 2.000000000000087
        threads time:  ??? 
        
        fibonacci = 3
        trapezoidal_rule = 2.000000000000087
        processes time:  ???
    """
