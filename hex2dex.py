"""
Python 3.6
@Author: wrgsRay
"""
dec_values = {}
alpha = 'ABCDEF'
for c, v in enumerate(alpha, 10):
    dec_values[v] = c


def check_value(value):
    if value == '':
        return False
    validinputs = '0123456789ABCDEF'
    for character in value:
        if character not in validinputs:
            return False
    return True


def convert_hex(value):
    power = 0
    result = 0
    for digit in value[::-1]:
        try:
            result += int(digit) * 16 ** power
        except ValueError:
            result += dec_values[digit] * 16 ** power
        power += 1
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
