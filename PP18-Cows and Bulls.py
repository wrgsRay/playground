import random


def cowsbulls(guess, answer):
    cows = 0
    bulls = 0
    missed = list()
    print(guess)
    print(answer)
    if guess == answer:
        return True
    else:
        guess = list(str(guess))
        answer = list(str(answer))
        for i in range(4):
            if guess[i] == answer[i]:
                cows += 1
            else:
                missed.append(answer[i])
        for b in guess:
            if b in missed:
                bulls += 1
        return cows, bulls

'''
def validate():
    userinput = input('Input a 4-digit number')
    while True:
        if len(userinput) == 4 and userinput.isdecimal():
            break
            return int(userinput)
        else:
            userinput = input('Try again')
'''



def main():
    answer = random.randint(1000, 9999)
    print(answer)
    check = int(input('enter 4-digit'))
    while True:
        result = cowsbulls(check, answer)
        if result is True:
            print(f'Congrats, the answer was {answer}!')
            break
        else:
            check = input(f'You got {result[0]} cows and {result[1]} bulls.')


if __name__ == '__main__':
    main()
