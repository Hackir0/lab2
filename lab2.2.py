def tack(num):
    if isinstance(num, tuple):
        wordLength = []
        for item in num:
            if isinstance(item,str):
               wordLength.append(len(item))
        print(wordLength)
        return

    if isinstance(num, list):
        theFirstIndexZero = None
        theSecondIndexZero = None
        for index, element in enumerate(num):
            if element == 0:
                if theFirstIndexZero is None:
                    theFirstIndexZero = index
                else:
                    theSecondIndexZero = index
                    break

        if theFirstIndexZero is not None and theSecondIndexZero is not None:
            product = 1
            for i in range(theFirstIndexZero + 1, theSecondIndexZero):
                product *= num[i]
            print("Произведение между первым и вторым нулевым элементом", product)
        else:
            print("В списке нет хотя бы двух нулевых элементов")
        return

    if isinstance(num, int):
        if num <= 1:
            print("Число не является простым")
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    print("Число не является простым")
                    return
            print("Число простое")
        return

    if isinstance(num, str):
        print("Таблица Unicode")
        for index, element in enumerate(num):
            print(f"Символ: {element}, Код Unicode: {ord(element)}")
        return

    print("Неизвестный тип переменной")


print("1 - В функцию передается кортеж\n"
      "2 - В функцию передается список\n"
      "3 - В функцию передаются число\n"
      "4 - В функцию передаются строка ")
try:
    x = int(input("Введите цифру, что вы хотите передать в функцию: "))
except ValueError:
    print("Ошибка ввода.")
if x == 1:
    myTuple = (1, "fwef", 2, True, False, "fwefw")
    tack(myTuple)
    # inputString = input("Введите элементы кортежа через пробел: ")
    # elements = inputString.split()
    # tack(tuple(elements))

if x == 2:
    input_str = input("Введите числа, разделенные пробелами: ")
    numbers = input_str.split()

    try:
        numbers = [int(x) for x in numbers]
    except ValueError:
        print("Ошибка: введите числа, разделенные пробелами.")
    tack(numbers)

if x == 3:
    try:
        input_num = int(input("Введите число: "))
        tack(input_num)
    except ValueError:
        print("Ошибка ввода.")

if x == 4:
    try:
        input_str = input("Введите строку: ")
        tack(input_str)
    except ValueError:
        print("Ошибка ввода.")
