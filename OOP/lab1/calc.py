class Calc:

    def __init__(self, x, y):
        self.value=x
        self.value2=y

    def summ(self):
        return self.value+self.value2

    def divide(self):
        return self.value / self.value2

    def diff(self):
        return self.value - self.value2

    def multi(self):
        return self.value * self.value2

def main():
    while True:
        s = input("Выбыерите действие (Сложение,Вычитание,Умножение,Деление): ")
        if s == '0': break
        if s in ('+', '-', '*', '/'):
            x = (float(input("x=")))
            y = float(input("y="))
            calculator=Calc(x,y)
            if s == '+':
                print(calculator.summ())
            elif s == '-':
                print(calculator.diff())
            elif s == '*':
                print(calculator.multi())
            elif s == '/':
                if y != 0:
                    print(calculator.divide())
                else:
                    print("/0=error!")
            else:
                print("error!")


if __name__ == "__main__":
    main()
