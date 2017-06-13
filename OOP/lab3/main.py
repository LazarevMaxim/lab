import sys


class Lab3Core():
    def Calculate(self):
        b = []
        k = ''
        a = sys.argv[0]
        l = len(a)
        q = 0
        for i in a[7:]:
            q += 1
            if q == l:
                k = k + i
                b.append(float(k))
                break
            if i == ',':
                b.append(float(k))
                k = ''
            else:
                k = k + i
     
        class Formula:
            def calculation(self, elem):
                if elem == 0:
                    return ZeroDivisionError
                return 1 / (elem * 3)
