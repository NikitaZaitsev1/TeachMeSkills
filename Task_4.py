from datetime import datetime

def time_test(fn):
    def wrapper(*args):
        start_time = datetime.now()
        fn(*args)
        finish_time = datetime.now() - start_time
        print(f'Время выполнения: {finish_time} секунд')
    return wrapper
@time_test
def summ_cub():
    num_n = int(input('Введите число: '))
    item = 1
    summ_cub = 0
    while item <= num_n:
        summ_cub += item ** 3
        item += 1
    print(f'Сумма кубов всех целых чисел от 1 до {num_n} ровняется {summ_cub}')
@time_test
def find_factorial(finish_number):
    factorial = 1
    if finish_number > 0:
        for i in range(1, finish_number + 1):
            factorial *= i
    elif finish_number == 0:
        factorial = 1
    print(factorial)
summ_cub()
find_factorial(10)
