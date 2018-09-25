"""
Python 3.6
@Author: wrgsRay
"""
dec_values = {}
alpha = 'ABCDEF'
"""Used enumerate to generate a dictionary for ABCDEF in format of {'A': 10} and so on"""
for c, v in enumerate(alpha, 10):
    dec_values[v] = c


def check_value(value):
    if value == '':
        return False  # Return False if input is empty
    validinputs = '0123456789ABCDEF'
    for character in value:
        if character not in validinputs:
            return False  # Return False if any character is not within validinputs
    return True


def convert_hex(value):
    """Convert hex to decimal using this equation:"""
    """x * 16 ** power"""
    power = 0  # Initialize the power as 0 for the first digit
    result = 0  # Initialize the result
    for digit in value[::-1]:  # Grab character in reversed order, eg. 2AFB input would be BFA2
        try:
            result += int(digit) * 16 ** power  # If this character is an integer, do the math
        except ValueError:
            # If this character is not an integer, get value by using dictionary declared
            result += dec_values[digit] * 16 ** power
        power += 1  # Increase power by 1 as the program moves to the next digit
    return result


def main():
    print('*' * 4 + ' Please input a value to convert from Hex to Decimal ' + '*' * 4)
    input_value = input()
    while True:
        if input_value[:1].lower() == 'q':
            print('Thank you for using this program.')
            break
        elif check_value(input_value):
            print(f'The decimal value of {input_value} is {convert_hex(input_value)}. '
                  f'Input another number or type q to quit.')
            input_value = input()
        else:
            print('Invalid Input. Please try again. Type q to quit.')
            input_value = input()


if __name__ == '__main__':
    main()
