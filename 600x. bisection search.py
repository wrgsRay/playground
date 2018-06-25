# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 21:28:30 2018

@author: raymond
"""
'''
x = 256
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))
'''

'''
x = 27
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high + low)/2.0

while abs(ans**3 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans** 3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to cube root of ' + str(x))


x = int(input('Please think of a number between 0 and 100!'))
low = 0
high = 100
ans = (high + low)//2
userInput = ''
print('Is your secret number ' + str(ans) + '?')
userInput = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to')

while userInput != 'c':
    if userInput == 'h':
        high = ans
        userInput = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to')
        print('Is your secret number ' + str(ans) + '?')
    elif userInput == 'l':
        low = ans
        userInput = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to')
        print('Is your secret number ' + str(ans) + '?')
    ans = (high + low)//2
print('Game over. Your secret number was: ' + str(ans))
'''

x = int(input('Please think of a number between 0 and 100!'))
low = 0
high = 101
ans = (high + low)//2
userInput = ''
print('Is your secret number ' + str(ans) + '?')
userInput = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to')

while userInput != 'c':
    if userInput == 'h':
        high = ans
        ans = (high + low)//2
        print('Is your secret number ' + str(ans) + '?')
        userInput = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to')
    elif userInput == 'l':
        low = ans
        ans = (low + high)//2
        print('is your secret number ' + str(ans) + '?')
        userInput = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to')
print('Game over. Your secret number was: '+ str(ans))