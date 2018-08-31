"""
Python 3.6
@Author: wrgsRay
"""
import os
root_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(root_dir)
from name_function import get_formatted_name


def main():
    print(r'enter "q" to quit')
    while True:
        first = input('First name')
        if first == 'q':
            break
        last = input('Last name')
        if last == 'q':
            break

        print(f'Formatted: {get_formatted_name(first, last)}')

if __name__ == '__main__':
    main()

