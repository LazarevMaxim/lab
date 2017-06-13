import math

class Number:
    def __init__(self, s):
        self.__s__ = s

    def getNumber(self):
        return self.__s__
class Answer:
    def __init__(self):
        self.__x__ = 3

    def getLA(self):
        return self.__x__

    def setLA(self, ans):
        self.__x__ = ans
class sqrt :
    def setAns(self, x, s):
        self.__ans__ = (x + (s / x)) /2

    def getAns(self):
        return self.__ans__

if __name__ == '__main__':
    print('Enter the number: ')
    s = Number(float(input()))
    x = Answer()
    answer = sqrt ()
    answer.setAns(x.getLA(), s.getNumber())
    while abs(x.getLA() - answer.getAns()) > 0.00005:
        x.setLA(answer.getAns())
        answer.setAns(x.getLA(), s.getNumber())

    print('Answer = {}'.format(answer.getAns()))
