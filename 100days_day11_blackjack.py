############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
from random import choice
import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


result = {
    'win': 'You win 😃',
    'lose': 'You lose 😤',
    'draw': 'Draw 🙃',
    'player_over': 'You went over. You lose 😤',
    'pc_over': 'Opponent went over. You win 😁',
}


def deal_cards(hand, num_of_cards):
    for _ in range(num_of_cards):
        hand.append(choice(cards))
    return hand


def calculate_score(hand):
    if len(hand) < 3:
        return sum(hand)
    elif 11 in hand:
        hand = [1 if i == 11 else i for i in hand]
        return sum(hand)
    return sum(hand)


def compare_score(score1, score2):
    if score2 > 21:
        return 'pc_over'
    elif score1 > score2:
        return 'win'
    elif score1 < score2:
        return 'lose'
    elif score1 == score2:
        return 'draw'


def pc_hand_operation(pc_hand):
    while calculate_score(pc_hand) < 17:
        deal_cards(pc_hand, 1)
    return pc_hand


def display_current_hands(hands):
    print(f"   Your cards: {hands[0]}, current score: {calculate_score(hands[0])}")
    print(f"   Computer's first card: {hands[1][0]}")


def display_final_hands(hands):
    print(f"   Your final hand: {hands[0]}, final score: {calculate_score(hands[0])}")
    print(f"   Computer's final hand: {hands[1]}, final score: {calculate_score(hands[1])}")


def main():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower().startswith('y'):
        blackjack()
    else:
        exit()


def blackjack():
    cls()
    your_hand = list()
    pc_hand = list()
    print(logo)
    your_hand = deal_cards(your_hand, 2)
    pc_hand = deal_cards(pc_hand, 2)
    # debug
    print(your_hand, pc_hand)
    while True:
        display_current_hands([your_hand, pc_hand])
        current_score = calculate_score(your_hand)
        if current_score > 21:
            pc_hand_operation(pc_hand)
            display_final_hands([your_hand, pc_hand])
            print(f"{result['player_over']}")
            main()
        deal_more_cards = input("Type 'y' to get another card, type 'n' to pass: ")
        if deal_more_cards.lower().startswith('y'):
            deal_cards(your_hand, 1)
        elif deal_more_cards.lower().startswith('n'):
            pc_hand_operation(pc_hand)
            display_final_hands([your_hand, pc_hand])
            print(result[compare_score(current_score, calculate_score(pc_hand))])
            main()


if __name__ == '__main__':
    main()

