class AllMails:
    def __init__(self):
        self.__listOfMails__ = []
        self.__dictOfMails__ = {}

    def setMail(self, name):
        self.__listOfMails__.append(name)

    def setDictMail(self):  # Считывание количества отправленных писем
        for i in self.__listOfMails__:
            if i in self.__dictOfMails__:
                self.__dictOfMails__[i] += 1
            else:
                self.__dictOfMails__[i] = 1

    def getListMail(self):
        return self.__listOfMails__

    def getDictMail(self):
        return self.__dictOfMails__

    def showDict(self):
        print(self.__dictOfMails__)
