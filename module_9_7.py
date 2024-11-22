# декоратор - is_prime
def is_prime(func):
    def wrapper(*args):
        res = func(*args)

        if res % 1 == 0: # если у числа отсутствует дробная часть, то это целое число
            res = int(res)
        else:
            print(f"Число {res} не является целым!")
            return res
        if res <= 0:
            print(f"Число {res} не является натуральным!")
            return res
        elif res == 1:
            print(f"Число {res} не является ни простым, ни составным!")

        divider_counter = 0
        for cur_divider in range(2, res//2 + 1): # проверка на простоту полученного числа res
            if res % cur_divider == 0:
                divider_counter += 1
        if divider_counter == 0:
            print(f"Число {res} - ПРОСТОЕ.")
        else:
            print(f"Число {res} - СОСТАВНОЕ.")

        return res
    return wrapper


@is_prime
def sum_three(*args):
    res = 0
    for numb in args:
        res += numb
    return res


result = sum_three(2, 3, 24)
print(result)