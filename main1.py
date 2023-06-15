result = None
operator = None
wait_for_number = True

while True:
    if wait_for_number:
        try:
            number = float(input("Введіть число: "))
            if result is None:
                result = number
            else:
                if operator == '+':
                    result += number
                elif operator == '-':
                    result -= number
                elif operator == '*':
                    result *= number
                elif operator == '/':
                    try:
                        result /= number
                    except ZeroDivisionError:
                        print("Помилка: ділення на нуль неможливе. Спробуйте ще раз.")
                        continue
            wait_for_number = False
        except ValueError:
            print("Помилка: введено некоректне число. Спробуйте ще раз.")
            continue
    else:
        operator = input("Введіть оператор (+, -, *, /, =): ")

        if operator == '=':
            print("Результат: ", result)
            break

        if operator in ('+', '-', '*', '/'):
            wait_for_number = True
        else:
            print("Помилка: некоректний оператор. Спробуйте ще раз.")
            continue
