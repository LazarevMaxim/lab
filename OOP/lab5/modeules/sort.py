class SpamRate:  # Сортировка по количеству спама
    def __init__(self):
        self.sortRat = []
        self.i = 0
        self.l = lambda x: x[1]

    def setSpamRate(self, rateOfSpam):
        self.sortRat = sorted(rateOfSpam.items(), key=self.l, reverse=True)
        self.showSpamRate()

    def showSpamRate(self):
        print('Top-5 spammers:')
        for elem in self.sortRat:
            if self.i < 5:  # Первые пять спаммеров
                print('{}. {} with rating of spam: {}'.format(self.i + 1, elem[0], elem[1]))
                self.i += 1
            else:
                break
