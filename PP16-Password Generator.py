from random import choice
import string

if __name__ == '__main__':
    def makepass(digit):
        passwordpool = string.ascii_letters + '!#$%*+_-@1234567890'
        passlist = list()
        while len(passlist) < digit:
            passlist.append(choice(passwordpool))
        newpass = ''.join(passlist)
        return newpass

    passdigit = input('How many digits do you want the pass word to be?')
    while True:
        try:
            passdigit = int(passdigit)
            break
        except ValueError:
            passdigit = input('Please use numbers only. How many digits?')

    print(f'Your new passwords:')
    print(makepass(passdigit))
    print(makepass(passdigit))
    print(makepass(passdigit))
    print(makepass(passdigit))
    print(makepass(passdigit))