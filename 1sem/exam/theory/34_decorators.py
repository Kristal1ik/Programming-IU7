import time


def timing_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Функция {func.__name__} выполнялась {end_time - start_time:.2f} секунд")

    return wrapper


@timing_decorator
def some_long_running_function():
    time.sleep(2)
    print("Функция завершила работу")


some_long_running_function()