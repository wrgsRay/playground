MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0.0
}

coins = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickle": 0.05,
    "penny": 0.01,
}


def payment_processor(quarter, dime, nickle, penny):
    return quarter * coins["quarter"] + dime * coins['dime'] + nickle * coins["nickle"] + penny * coins["penny"]


def check_resources(current_resources, customer_choice):
    for item in customer_choice['ingredients']:
        if customer_choice['ingredients'][item] > current_resources[item]:
            return f" Sorry there is not enough {item}"
        return 'ok'


def deduct_resources(current_resources, customer_choice):
    for item in customer_choice['ingredients']:
        current_resources[item] -= customer_choice['ingredients'][item]


def main():
    while True:
        choice = input(" What would you like? (espresso/latte/cappuccino):")
        if choice == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}")
            print(f'Coffee: {resources["coffee"]}g')
            print(f'Money: ${resources["Money"]}')
        else:
            choice = MENU[choice]
            if check_resources(resources, choice) == 'ok':
                print("Please insert coins.")
                quarter_amount = int(input('how many quarters?:'))
                dime_amount = int(input('how many dimes?:'))
                nickle_amount = int(input('how many nickles?:'))
                penny_amount = int(input('how many pennies?:'))
                payment = payment_processor(quarter_amount, dime_amount, nickle_amount, penny_amount)
                if payment == choice['cost']:
                    print('Here is your espresso ☕️. Enjoy!')
                    resources["Money"] += payment
                    deduct_resources(resources, choice)
                elif payment > choice['cost']:
                    change = payment - choice['cost']
                    print(f"Here's ${change} in change.")
                    print('Here is your espresso ☕️. Enjoy!')
                    resources["Money"] += payment - change
                    deduct_resources(resources, choice)
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print(check_resources(resources, choice))


if __name__ == '__main__':
    main()
