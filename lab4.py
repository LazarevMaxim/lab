import random
import statistics
from matplotlib import pyplot as plt

def sma(num, size):  # работа с очередью
    global win

    if len(win) < size:  # если размер очереди меньше установленного окна
        win.append(num)
        return None

    else:  # очередь равна размеру окна
        win = win[1:]
        win.append(num)
        return statistics.mean(win)

def searchNum():  # поиск случайного числа
    return random.randint(1, 100)

def myOutput(origData, answer):  # вывод графика
    fig, ax = plt.subplots()
    ax.plot([i for i in range(30)], origData)
    ax.plot([i for i in range(size, 30)], answer)
    plt.show()
    return None

answer = []
origData = []
win = []
i = 0
size = int(input('Enter size of window: '))

while i < 30:
    num = searchNum()
    origData.append(num)  # добавляем данные о функции

    ans = sma(num, size)  # ищем значение sma
    if ans != None:
        answer.append(ans)  # добавляем ответ, если очередь была заполнена
    i += 1

myOutput(origData, answer)
