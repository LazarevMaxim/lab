import sys

def formula(elem): # Решение формулы
    if elem == 0:
        return ZeroDivisionError
    return 1 / (elem*3)

if __name__ == '__main__':
    # Считывание аргумента командной строки
    string = sys.argv[1]
    string = string.split('--poly=')
    string = string[1].split(',')

    summ = 0
    for elem in string:
        summ += formula(float(elem))
    print(string)
    print(summ)
