#Рассчет квадратного корня по формуле Герона 
class Core():
    def Sqrt(self, a):
        c = 1
        b = 0
        while (round(b, 5)) != (round(c, 5)):
            b = c
            c = (c + a / c) * 0.5
        return c
