from random import choice
import string

if __name__ == '__main__':
    def makepass(digit):
        passwordpool = string.ascii_letters + '!#$%*+_-@'
        passlist = list()
        while len(passlist) < digit:
            passlist.append(choice(passwordpool))
        newpass = ''.join(passlist)
        return newpass

    print(makepass(20))