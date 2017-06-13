from modules.Modules import Core

class App():
    def __init__(self):
        while 1:
            self.Core = Core()
            print('Введите X:')
            self.Result = self.Core.Calculate(input())
            print('Получаем скользящее среднее: ')
            print(self.Result)
            self.Core.BuildGraphic()
            print('\nДля продолжения введите 1 \nДля выхода введите 0')
            p = input()
            if p == '0':
                break;
