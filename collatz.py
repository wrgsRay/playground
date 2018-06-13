def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(str(number))
        elif number % 2 == 1:
            number = number * 3 + 1
            print(str(number))
print("Enter number:")
try:
    inputNumber = int(input())
    collatz(inputNumber)
except ValueError:
    print("It's not a number!")
