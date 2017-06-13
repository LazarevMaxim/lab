from modules.Modules import Core


# Основной класс
class App():
    def __init__(self):
        while 1:
            self.Core = Lab5Core()
            print('Инициализация информции...')
            self.Core.DataBind()
            self.Core.SpamCheck()
            print('Среднее значение спамеров = ' + str(self.Core.SR_Spam))
            print('Спамеры - ' + self.Core.BanUser.name)
            self.Core.BuildGraph()
            print('\nДля продолжения нажмите 1 \nДля закрытия 2')
            p = input()
            if p == '2':
                break;
