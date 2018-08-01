if __name__ == '__main__':
    def fibonacci(num):
        fibo = list()
        try:
            num = int(num)
        except ValueError:
            return 'Invalid Input'
        if num <= 1:
            return 'Enter something larger than 1'
        else:
            a = 0
            b = 1
            fibo.append(1)
            while len(fibo) < num:
                fibo.append(a + b)
                a = fibo[-2]
                b = fibo[-1]
            return fibo

    print(fibonacci(input('How many numbers of the Fibonacci Sequence do you want to see?')))