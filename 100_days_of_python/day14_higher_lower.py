from day14_game_data import data
from day14_art import logo, vs
from random import choice
import os


def compare_score(score_a, score_b):
    if score_a > score_b:
        return 'a'
    elif score_a < score_b:
        return 'b'


def assign_answers(previous_answer):
    global guess_a
    global guess_b
    if previous_answer == 'a':
        guess_b = choice(data)
    elif previous_answer == 'b':
        guess_a = guess_b
        guess_b = choice(data)


def main(entry_a, entry_b, score_input):
    os.system('clear')
    print(logo)
    if score_input > 0:
        print(f"You're right! Current score: {score_input}")
    print(f"Compare A: {entry_a['name']}, a {entry_a['description']}, from {entry_a['country']}")
    print(vs)
    print(f"Against B: {entry_b['name']}, a {entry_b['description']}, from {entry_b['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess[0] == compare_score(entry_a['follower_count'], entry_b['follower_count']):
        return guess
    else:
        return False


guess_a = choice(data)
guess_b = choice(data)
score = 0

if __name__ == "__main__":
    while True:
        answer = main(guess_a, guess_b, score)
        if answer:
            prev_answer = answer
            score += 1
            assign_answers(answer)
        else:
            os.system('clear')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            break
