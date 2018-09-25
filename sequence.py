"""
Python 3.6
@Author: wrgsRay
"""


def is_valid_phone_number(txt):
    import re
    regex = re.compile(r'\(\d{3}\) \d{3}-\d{4}')
    return True if regex.findall(txt) else False


def main():
    txt = '(123) 456-7890'
    print(is_valid_phone_number(txt))


if __name__ == '__main__':
    main()
