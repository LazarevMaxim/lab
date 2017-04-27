def calculation(num1, num2, operation):
    # Выбор операции
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    elif operation == '/':
        answer = num1/num2
    else:
        print('Error! Enter operation like +, -, * or /.')
        return None
    strAnswer = str(answer)
    print('Answer is ' + strAnswer)
    return answer

if __name__ == '__main__':
    # Начало работы программы. Первые вычисления
    print('Enter number 1, number 2 and operation:')
    num1 = float(input())
    num2 = float(input())
    operation = str(input())
    answer = calculation(num1, num2, operation)
    signal = 1

    while signal == 1:
        print('Enter 1 for continue calculations, 2 for new calculations and 3 for exit:')
        choice = int(input())
        if choice == 1 and answer != None:  # Продолжение работы с ответом
            print('Enter number 2 and operation:')
            num2 = float(input())
            operation = str(input())
            calculation(answer, num2, operation)
        elif choice == 1 and answer == None:
            print('Error in first number! Please, try again.')
            continue
        elif choice == 2:  # Новое выражение
            print('Enter number 1, number 2 and operation:')
            num1 = float(input())
            num2 = float(input())
            operation = str(input())
            answer = answer = calculation(num1, num2, operation)
        elif choice == 3:  # Выход
            signal = 0
        else:
            print('Error! Enter 1, 2 or 3')  # Ошибка ввода

    input('Press any key to exit: ')
