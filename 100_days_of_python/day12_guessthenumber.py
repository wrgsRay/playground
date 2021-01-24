from random import randint

logo = r"""
   _____ _    _ ______  _____ _____   _______ _    _ ______   _   _ _    _ __  __ ____  ______ _____  
  / ____| |  | |  ____|/ ____/ ____| |__   __| |  | |  ____| | \ | | |  | |  \/  |  _ \|  ____|  __ \ 
 | |  __| |  | | |__  | (___| (___      | |  | |__| | |__    |  \| | |  | | \  / | |_) | |__  | |__) |
 | | |_ | |  | |  __|  \___ \\___ \     | |  |  __  |  __|   | . ` | |  | | |\/| |  _ <|  __| |  _  / 
 | |__| | |__| | |____ ____) |___) |    | |  | |  | | |____  | |\  | |__| | |  | | |_) | |____| | \ \ 
  \_____|\____/|______|_____/_____/     |_|  |_|  |_|______| |_| \_|\____/|_|  |_|____/|______|_|  \_\
  """
starting_range = 1
ending_range = 100
difficulty_attempts = {
    'e': 10,
    'h': 5
}


def check_answer(answer_input, guess):
    if guess == answer_input:
        return 'correct'
    elif guess > answer_input:
        return 'high'
    else:
        return 'low'


answer = randint(starting_range, ending_range)
print(logo)
print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {starting_range} and {ending_range}.")
print(f"Pssst, the correct answer is {answer}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()[0]
attempts = difficulty_attempts[difficulty]
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess:"))
    if check_answer(answer_input=answer, guess=guess) == 'high':
        print("Too high")
        print('Guess again.')
        attempts -= 1
    elif check_answer(answer_input=answer, guess=guess) == 'low':
        print("Too low")
        print('Guess again.')
        attempts -= 1
    else:
        print(f"You got it! The answer was {answer}.")
        break
