if __name__ == '__main__':
    num = input('Give me a number')
    check = input('Give me another number')
    while True:
        try:
            num = int(num)
            break
        except ValueError:
            num = input('I said: Give me a number')
    while True:
        try:
            check = int(check)
            break
        except ValueError:
            check = input('I said: Give me a number')
    if num % 2 == 0:
        print(f'{num} is an even number.')
    else:
        print(f'{num} is an odd number.')
    if num % 4 == 0:
        print(f'Extra: {num} can be divided by 4')
    if num % check == 0:
        print(f'Extra 2: {num} can be divided by {check}')
    else:
        print(f'Extra 2: {num} can NOT be divided by {check}')