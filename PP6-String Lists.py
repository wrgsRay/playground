if __name__ == '__main__':
    check = input('Please give me a string')
    if check[::-1] == check:
        print('Your string is palindrome.')
    else:
        print('Your string is not palindrome.')