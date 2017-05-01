from matplotlib import pyplot as plt

listOfMails = []
dictOfMails = {}
rateOfSpam = {}

def spamRate():  # Сортировка по количеству спама
    i = 0
    l = lambda x: x[1]
    sortRat = sorted(rateOfSpam.items(), key=l, reverse=True)
    print('Top-5 spammers:')
    for elem in sortRat:
        if i < 5:  # Первые пять спаммеров
            print('{}. {} with rating of spam: {}'.format(i+1, elem[0], elem[1]))
            i += 1
        else:
            break

def firstSort():   # Считывание количества отправленных писем
    for i in listOfMails:
        if i in dictOfMails:
            dictOfMails[i] += 1
        else:
            dictOfMails[i] = 1

def averValue(dspam, size):
    return dspam/size

def createBarChart():
    names = []
    for name in dictOfMails:
        names.append(name)

    # Создание гистограммы
    plt.bar(range(len(dictOfMails)), dictOfMails.values(), align='center')
    plt.xticks(range(len(dictOfMails)), names)
    plt.show()

if __name__ == '__main__':
    dspam = 0
    name = ''

    f = open('mbox.txt', 'r')  # Взятие данных из файла
    mboxData = f.readlines()
    f.close()

    for line in mboxData:
        l = line.split(' ')
        if l[0] == 'From':  # Считывание отправителя
            listOfMails.append(l[1])
            name = l[1]
        if l[0] == 'X-DSPAM-Confidence:':  # Считывание значение спама
            dspam += float(l[1])
            if name in rateOfSpam:
                rateOfSpam[name] = (float(rateOfSpam[name]) + float(l[1])) / 2  # Ищем среднее между имеющимся и новым
            else:
                rateOfSpam[name] = float(l[1])

    dspam_data = averValue(dspam, len(listOfMails))   # Среднее значение спама
    firstSort()
    print('Average value: {}'.format(dspam_data))
    print(dictOfMails)
    spamRate()
    createBarChart()
