import random
if __name__ == '__main__':
    answer = random.randint(1, 9)
    guesses = 0
    num = input('Guess a number between 1 and 9. Type exit to exit.')
    while True:
        try:
            num = int(num)
            break
        except ValueError:
            if num == 'exit':
                print('goodbye!')
                break
            else:
                num = input('I said: Give me a number')
    while num != answer:
        if num > answer:
            num = input('Your answer was too high. Try again?')
            guesses += 1
        else:
            num = input('Your answer was too low. Try again?')
            guesses += 1
        while True:
            try:
                num = int(num)
                break
            except ValueError:
                if num == 'exit':
                    print('goodbye!')
                    break
                else:
                    num = input('I said: Give me a number')

    print(f'Congrats! You got it! The answer was {answer}! It took you {guesses} guesses!')
