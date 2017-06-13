from modules.Modules import Core

class Lab2App():
    def __init__(self):
        while 1:

            self.Core = Core()
            print('\nВведите число из которого необходимо извлечь корень:')
            self.Input = input()
            self.Output = self.Core.Sqrt(float(self.Input))
            print(round(self.Output, 5))
            print('\nДля продолжения введите 1 \nДля выхода введите 2')
            p = input()
            if p == '2':
                break;
