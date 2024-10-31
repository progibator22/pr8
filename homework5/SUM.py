total_sum = 0.0

while True:
    user_input = input("Введите число (или 'stop'/'end' для завершения): ")
    
    if user_input == "stop" or user_input == "end" or user_input == "STOP" or user_input == "END":
        print("Завершение программы.")
        break

    try:
        number = float(user_input)
        total_sum += number
        print(f"Вы ввели число: {number}")
    except ValueError:
        print("Это не число, пропускаем итерацию.")

print(f"Сумма всех введенных чисел: {total_sum}")
