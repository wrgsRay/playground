if __name__ == '__main__':
    rules = {'r': 's', 's': 'p', 'p': 'r'}

    def rps(a, b):
        if a.lower()[:1] == b.lower()[:1]:
            return "Draw!"
        elif rules[a] == b:
            return "Player 1 wins"
        else:
            return "Player 2 wins!"


    # print(rps(h, i))
    while True:
        print('=' * 5 + 'Welcome to Rock Paper Scissor!' + '=' * 5)
        print('To play to game, simply type rock, paper or scissor when it is your turn.')
        print('Or you can type r, p or s if you\'re lazy!')
        while True:
            p1 = input('Player 1! Your turn! Type in your input! (Or you can use r, p or s)')
            if p1.lower()[:1] in rules.keys():
                p1 = p1.lower()[:1]
                break
        while True:
            p2 = input('Player 2! Your turn! Type in your input! (Or you can use r, p or s)')
            if p2.lower()[:1] in rules.keys():
                p2 = p2.lower()[:1]
                break
        print(rps(p1, p2))
        if input('Would you like to play another one? type \'no\' to stop and anything to play again').lower() == 'no':
            break
