def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

try:

    num = int(input("Введите число "))
    if 0 <= num <= 1000:
        print(is_prime(num))
    else:
        print("Введите число из диапозона (0,1000)")
except ValueError:
    print("Некорректный ввод")
