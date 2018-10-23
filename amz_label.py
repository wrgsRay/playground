"""
Python 3.6
@Author: wrgsRay
"""
import time


def main():
    last_page = 1064
    pallet_total = 24
    pallet_list = [49, 49, 36, 36, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 48, 44, 30, 15, 35, 48, 56, 30]
    current = 1
    print(len(pallet_list))
    print(sum(pallet_list))
    for pallet in pallet_list:
        print(f'{current}-{current + pallet - 1}')
        current += pallet

    print('Window is closing in 30 seconds...')
    time.sleep(30)

if __name__ == '__main__':
    main()
