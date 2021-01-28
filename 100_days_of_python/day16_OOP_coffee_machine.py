from day16_menu import Menu, MenuItem
from day16_coffee_maker import CoffeeMaker
from day16_money_machine import MoneyMachine


def main():
    menu = Menu()
    machine = CoffeeMaker()
    cashier = MoneyMachine()
    while True:
        choice = input(f" What would you like? ({menu.get_items()}):")
        if choice == 'report':
            machine.report()
            cashier.report()
        elif menu.find_drink(choice):
            for i in range(len(menu.menu) - 1):
                if choice == menu.menu[i].name:
                    drink = menu.menu[i]
                    if machine.is_resource_sufficient(drink):
                        if cashier.make_payment(drink.cost):
                            machine.make_coffee(drink)


if __name__ == "__main__":
    main()
