# -*- coding: UTF-8 -*-
import pylab


class Core():
    def BuildGraphic(self):
        pylab.plot(self.B)
        pylab.plot(self.Bglide)
        pylab.show()

    def Calculate(self, X):
        count = 0
        sb = ''
        B = []
        l = len(X)
        for i in X:
            count += 1
            if count == l:
                sb = sb + i
                B.append(float(sb))
                break
            if i == ',':
                B.append(float(sb))
                sb = ''
            else:
                sb += i
        s = 1
        Bglide = []
        for i in range(len(B) - 1):
            if i != 0 and (i + s != len(B) - 1):
                Bglide.append(int((B[i - 1] + B[i] + B[i + 1]) / 3))
            else:
                Bglide.append(B[i])
        self.Bglide = Bglide
        self.B = B

        return Bglide
