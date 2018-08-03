import random


def cowsbulls(guess, answer):
    cows = 0
    bulls = 0
    print(f'DEBUG: user input: {guess}')
    print(f'DEBUG: answer is:  {answer}')
    if guess == answer:
        return True
    else:
        guess = list(str(guess))
        answer = list(str(answer))
        for i in range(4):
            if guess[i] in answer:
                if guess[i] == answer[i]:
                    print(f'current: {i} DEBUG: cows + 1')
                    cows += 1
                    continue
                else:
                    print(f'current: {i} DEBUG: bulls + 1')
                    bulls += 1
                    continue

        return cows, bulls


def main():
    # answer = random.randint(1000, 9999)
    answer = '1025'
    print(f'DEBUG: answer is {answer}')
    check = input('enter 4-digit(please input 5551)')
    while True:
        result = cowsbulls(check, answer)
        if result is True:
            print(f'Congrats, the answer was {answer}!')
            break
        else:
            check = input(f'You got {result[0]} cows and {result[1]} bulls.')


if __name__ == '__main__':
    main()
