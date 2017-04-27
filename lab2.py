import math

def formula (num, tempAnswer):
    answer = (tempAnswer + num / tempAnswer) / 2
    while abs(tempAnswer - answer) > 0.00001:
        tempAnswer = answer
        answer = (tempAnswer + (num / tempAnswer)) / 2
    return answer

if __name__ == '__main__':
    num = float(input('Enter the number in the square root: '))
    answer = formula(num, 3)

    print('Answer is {}'.format(answer))
    print('Correct answer is {}'.format(math.sqrt(num)))
    input('Press any key to exit: ')
