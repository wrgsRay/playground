from datetime import datetime

if __name__ == '__main__':
    userName = input('What is your name?')
    userAge = input('What is your age?')
    while True:
        try:
            userAge = int(userAge)
            break
        except ValueError:
            userAge = input('What is your age?(a whole number please)')
    thisYear = datetime.now().year
    year100 = int(thisYear) + (100 - userAge)
    print(f'You will be 100 on the year of {year100}')
    repeatTimes = input('How many times should I repeat this message?')
    while True:
        try:
            repeatTimes = int(repeatTimes)
            break
        except ValueError:
            repeatTimes = input('How many times should I repeat this message?(a whole number please)')
    print(f'You will be 100 on the year of {year100}\n' * repeatTimes)
