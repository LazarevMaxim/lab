from modules.lab3Modules import Lab3Core

class App():
    def __init__(self):
        while 1:
            self.Core = Lab3Core()
            self.Result = self.Core.Calculate()
            print(self.Core.Poly)
            print('Answer')
            print(self.Result)
            print('\nПродолжить введите 1 \nЗавершить введите 2')
            p = input()
            if p == '2':
                break;
