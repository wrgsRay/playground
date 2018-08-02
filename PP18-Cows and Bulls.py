import random


def cowsbulls(guess, answer):
    cows = 0
    bulls = 0
    missed = list()
    print(f'DEBUG: user input: {guess}')
    print(f'DEBUG: answer is:  {answer}')
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


def main():
    answer = random.randint(1000, 9999)
    print(f'DEBUG: answer is {answer}')
    check = input('enter 4-digit')
    while True:
        result = cowsbulls(check, answer)
        if result is True:
            print(f'Congrats, the answer was {answer}!')
            break
        else:
            check = input(f'You got {result[0]} cows and {result[1]} bulls.')


if __name__ == '__main__':
    main()
