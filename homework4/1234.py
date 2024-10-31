try:
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))

    a, b = int(a), int(b)

    if a < b:
        for i in range(a + 1, b):
            print(i, end=" ")
    elif a > b:
        for i in range(a - 1, b, -1):
            print(i, end=" ")
    else:
        print("Числа a и b равны, между ними нет целых чисел.")
except ValueError:
    print("Ошибка: Пожалуйста, введите числовые значения.")
