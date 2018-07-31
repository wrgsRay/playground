if __name__ == '__main__':
    num = input('Give me a number and I will find the divisor(s)')
    newList = list()
    while True:
        try:
            num = int(num)
            break
        except ValueError:
            num = input('I said: Give me a number')
    for i in range(1, num):
        if num % i == 0:
            newList.append(i)
    print(newList)
