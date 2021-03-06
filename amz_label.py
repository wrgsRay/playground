"""
Python 3.6
@Author: wrgsRay
"""
import time


class Shipment:
    def __init__(self, last_page, total_pallet, pallet_list=[], current_pallet):
        self.last_page = last_page
        self.total_pallet = total_pallet
        self.pallet_list = pallet_list
        self.current_pallet = current_pallet

    def get_pallet_input(self):
        while True:
            pallet_input = input(f'Please enter carton number for Pallet {self.current_pallet}, enter nothing to stop ')
            if pallet_input == '':
                break
            else:
                pallet_input = int(pallet_input)
                self.pallet_list.append(pallet_input)
                print(f'Pallet {self.current_pallet}: {pallet_input}')
                self.current_pallet += 1


def amz():
    shipment = Shipment(1, 10, [], 1)
    shipment.get_pallet_input()


def main():
    last_page = int(input('Please enter the last page number(eg. 1064) '))
    pallet_total = int(input('Please enter the total number of pallets(eg. 24) '))
    pallet_list = list()
    current_pallet = 1
    while True:
        pallet_input = input(f'Please enter carton number for Pallet {current_pallet}, enter nothing to stop ')
        if pallet_input == '':
            break
        else:
            pallet_input = int(pallet_input)
            pallet_list.append(pallet_input)
            print(f'Pallet {current_pallet}: {pallet_input}')
            current_pallet += 1

    if len(pallet_list) != pallet_total:
        print(f'Pallet Total mismatch: expected {pallet_total} pallets got {len(pallet_list)} pallets')
    elif sum(pallet_list) != last_page:
        print(f'Carton Total Mismatch expected {last_page} cartons got {sum(pallet_list)} cartons')
    # pallet_list = [49, 49, 36, 36, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 48, 44, 30, 15, 35, 48, 56, 30]
    else:
        current = 1
        print(len(pallet_list))
        print(sum(pallet_list))
        for pallet in pallet_list:
            print(f'{current}-{current + pallet - 1}')
            current += pallet

        print('Window is closing in 30 seconds...')
        time.sleep(30)


if __name__ == '__main__':
    amz()
