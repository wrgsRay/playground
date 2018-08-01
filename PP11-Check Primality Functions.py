if __name__ == '__main__':
    def getnumber():
        num = input('Give me a number to check if it is a prime number')
        while True:
            try:
                num = int(num)
                break
            except ValueError:
                num = input('That was not a number')
        return num

    def checkprime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
            elif num % i != 0:
                continue
        return True


    if checkprime(getnumber()) is True:
        print(f'That number was a prime number')
    else:
        print(f'That number was not a prime number.')