class Mbox:
    def __init__(self):
        f = open('mbox.txt', 'r')  # Взятие данных из файла
        self.__mboxData__ = f.readlines()
        f.close()

    def getMbox(self):
        return self.__mboxData__
