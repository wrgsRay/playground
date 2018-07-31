if __name__ == '__main__':
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 15, 28, 34, 20, 23, 18, 45]
    check = input('Give me a number to check')
    while True:
        try:
            check = int(check)
            break
        except ValueError:
            check = input('I said: Give me a number')
    newList = [x for x in a if x < check]
    print(newList)