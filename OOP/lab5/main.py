# -*- coding: utf-8 -*-
import urllib.request
import matplotlib.pyplot




class Sender:
    def __init__(self, n):
        self.name = n
        self.Kmail = 0
        self.spa = []
        self.srspam = None

class Core():
    
    def __init__(self):
        self.Senders = []
        self.ikk = []
    def BuildGraph(self):
        X = []
        for i in self.Senders:
            X.append(i.Kmail)
        Y = range(len(X))
        matplotlib.pyplot.bar(Y, X, align='center')
        matplotlib.pyplot.xticks(Y)
        matplotlib.pyplot.show()

    def name(self, z, spom):
        n = self.Senders[z]
        flag = False
        n.Kmail += + 1
        n.spa.append(spom)

    def SpamCheck(self):
        SR_Spam = 0
        count = 0
        for i in self.Senders:
            for j in i.spa:
                count += 1
                SR_Spam += j
        SR_Spam /= count
        self.Senders.pop()
        for i in self.Senders:
            sm = 0
            sk = len(i.spa)
            for j in i.spa:
                sm = sm + j
            i.srspam = sm / sk
        maxx = 0
        count = 0
        for i in self.Senders:
            if i.srspam > self.Senders[maxx].srspam:
                maxx = count
            count += 1
        self.SR_Spam = SR_Spam
        self.BanUser = self.Senders[maxx]

    def DataBind(self):
        s = urllib.request.urlopen('http://www.pythonlearn.com/code3/mbox.txt')
        f = str(s.read())
        pos = 0
        R = 'Author: '
        LR = len(R)
        Spam = 'X-DSPAM-Confidence: '
        Lspam = len(Spam)
        Name = ''
        while f.find(Spam, pos) != -1:
            count = 0
            pos = f.find(Spam, pos) + Lspam
            sPm = float(f[pos:(pos + 6)])
            pos = f.find(R, pos) + LR
            for i in range(1000):
                if (f[(pos + i + 3):pos + i + 3 + 4]) == 'Date':
                    Name = f[pos:(pos + i + 1)]
                    break
            otp = self.Senders
            flag = False
            for x in self.Senders:
                if x.name == Name:
                    flag = True
                    break
                count += 1
            if not flag:
                otp.append(Sender(Name))
            self.Senders = otp
            self.name(count - 1, sPm)


