from modules.mbox import Mbox
from modules.dspam import Dspam
from modules.allMails import AllMails
from modules.spamRate import SpamRate
from modules.barChart import BarChart

class App:
    def __init__(self):
        self.name = ''
        self.rateOfSpam = {}

        self.mbox = Mbox()
        self.dspam = Dspam()
        self.allMails = AllMails()
        self.spamRate = SpamRate()
        self.barChart = BarChart()

    def run(self):
        mboxData = self.mbox.getMbox()
        for line in mboxData:
            l = line.split(' ')
            if l[0] == 'From':  # Считывание отправителя
                self.allMails.setMail(l[1])
                self.name = l[1]
            if l[0] == 'X-DSPAM-Confidence:':  # Считывание значение спама
                self.dspam.setDspam(float(l[1]))
                if self.name in self.rateOfSpam:
                    self.rateOfSpam[self.name] = (float(self.rateOfSpam[self.name]) + float(
                        l[1])) / 2  # Ищем среднее между имеющимся и новым
                else:
                    self.rateOfSpam[self.name] = float(l[1])

        self.dspam.getAverValue(len(self.allMails.getListMail()))  # Среднее значение спама
        self.allMails.setDictMail()
        self.allMails.showDict()
        self.spamRate.setSpamRate(self.rateOfSpam)  # Сортировка по количеству спама
        self.barChart.createBarChart(self.allMails.getDictMail())
