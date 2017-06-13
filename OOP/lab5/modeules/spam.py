class Dspam():
    def __init__(self):
        self.__dspam__ = 0

    def setDspam(self, num):
        self.__dspam__ += num

    def getAverValue(self, size):  # Среднее значение спама
        print('Average value: {}'.format(self.__dspam__ / size))
