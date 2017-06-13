from matplotlib import pyplot as plt

class BarChart:
    def __init__(self):
        self.names = []

    def createBarChart(self, dictOfMails):
        for name in dictOfMails:
            self.names.append(name)

        # Создание гистограммы
        plt.bar(range(len(dictOfMails)), dictOfMails.values(), align='center')
        plt.xticks(range(len(dictOfMails)), self.names)
        plt.show()
